"""Particle filter / Sequential Monte Carlo for high-dimensional state spaces
Sequential Bayesian assimilation: P(C,t | data) ∝ L(data | C) · P(C,t | prior)
"""

import numpy as np
from typing import Optional, Callable, Tuple, List
from dataclasses import dataclass

@dataclass
class ParticleFilterConfig:
    """Configuration for particle filter"""
    n_particles: int = 1000          # Number of particles
    resampling_threshold: float = 0.5  # Effective sample size threshold
    random_seed: Optional[int] = None

class ParticleFilter:
    """
    Particle filter for high-dimensional civilizational state estimation
    """
    
    def __init__(self, n_dim: int, config: Optional[ParticleFilterConfig] = None):
        self.n_dim = n_dim
        self.config = config or ParticleFilterConfig()
        
        if self.config.random_seed is not None:
            np.random.seed(self.config.random_seed)
        
        self.particles = None
        self.weights = None
    
    def initialize(self, initial_state: np.ndarray, initial_cov: Optional[np.ndarray] = None):
        """Initialize particle ensemble"""
        n = self.config.n_particles
        
        if initial_cov is None:
            initial_cov = np.eye(self.n_dim) * 0.1
        
        self.particles = np.random.multivariate_normal(initial_state, initial_cov, n)
        self.weights = np.ones(n) / n
    
    def predict(self, transition_function: Callable[[np.ndarray], np.ndarray]):
        """Prediction step: propagate particles through dynamics"""
        if self.particles is None:
            raise ValueError("Filter not initialized. Call initialize() first.")
        
        for i in range(self.config.n_particles):
            self.particles[i] = transition_function(self.particles[i])
    
    def update(self, observation: np.ndarray, 
               likelihood_function: Callable[[np.ndarray, np.ndarray], float]):
        """Update step: reweight particles based on observation"""
        if self.particles is None:
            raise ValueError("Filter not initialized. Call initialize() first.")
        
        # Compute likelihood for each particle
        log_likelihoods = np.zeros(self.config.n_particles)
        for i in range(self.config.n_particles):
            log_likelihoods[i] = likelihood_function(self.particles[i], observation)
        
        # Update weights
        self.weights = self.weights * np.exp(log_likelihoods)
        
        # Normalize
        total = np.sum(self.weights)
        if total > 0:
            self.weights /= total
        else:
            self.weights = np.ones(self.config.n_particles) / self.config.n_particles
        
        # Resample if needed
        n_eff = 1 / np.sum(self.weights**2)
        if n_eff < self.config.resampling_threshold * self.config.n_particles:
            self._resample()
    
    def _resample(self):
        """Systematic resampling"""
        n = self.config.n_particles
        
        # Cumulative distribution
        cumulative = np.cumsum(self.weights)
        
        # New indices
        indices = np.zeros(n, dtype=int)
        u = np.random.uniform(0, 1/n)
        
        j = 0
        for i in range(n):
            while u > cumulative[j]:
                j += 1
            indices[i] = j
            u += 1/n
        
        # Resample
        self.particles = self.particles[indices]
        self.weights = np.ones(n) / n
    
    def get_mean(self) -> np.ndarray:
        """Get weighted mean estimate"""
        if self.particles is None:
            raise ValueError("Filter not initialized")
        return np.average(self.particles, weights=self.weights, axis=0)
    
    def get_covariance(self) -> np.ndarray:
        """Get weighted covariance estimate"""
        if self.particles is None:
            raise ValueError("Filter not initialized")
        mean = self.get_mean()
        centered = self.particles - mean
        weighted_centered = centered * self.weights[:, np.newaxis]
        return weighted_centered.T @ centered
    
    def get_credible_interval(self, alpha: float = 0.05) -> Tuple[np.ndarray, np.ndarray]:
        """Get credible interval (lower, upper) for each dimension"""
        if self.particles is None:
            raise ValueError("Filter not initialized")
        
        lower = np.zeros(self.n_dim)
        upper = np.zeros(self.n_dim)
        
        for d in range(self.n_dim):
            # Weighted quantiles
            sorted_idx = np.argsort(self.particles[:, d])
            sorted_weights = self.weights[sorted_idx]
            cumulative = np.cumsum(sorted_weights)
            
            lower[d] = self.particles[sorted_idx[np.searchsorted(cumulative, alpha/2)], d]
            upper[d] = self.particles[sorted_idx[np.searchsorted(cumulative, 1 - alpha/2)], d]
        
        return lower, upper
    
    def get_ensemble(self) -> np.ndarray:
        """Get particle ensemble"""
        return self.particles.copy()
