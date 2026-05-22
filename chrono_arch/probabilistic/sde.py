"""Stochastic differential equation for civilizational evolution
Equation (12): dC = F(C, E, G) dt + σ(C) dW
"""

import numpy as np
from typing import Optional, Callable, Tuple
from dataclasses import dataclass

@dataclass
class SDEParameters:
    """Parameters for stochastic differential equation"""
    diffusion_coefficient: float = 0.1      # σ(C) base value
    use_state_dependent: bool = True        # Whether σ depends on C
    noise_seed: Optional[int] = None

class SDESimulator:
    """
    Simulator for stochastic civilizational dynamics
    Implements Itô SDE: dC = F dt + σ(C) dW
    """
    
    def __init__(self, params: Optional[SDEParameters] = None):
        self.params = params or SDEParameters()
        if self.params.noise_seed is not None:
            np.random.seed(self.params.noise_seed)
    
    def diffusion_coefficient(self, C: np.ndarray) -> np.ndarray:
        """
        State-dependent diffusion coefficient σ(C)
        """
        if not self.params.use_state_dependent:
            return np.ones_like(C) * self.params.diffusion_coefficient
        
        # Higher diffusion near boundaries (more uncertainty)
        base = self.params.diffusion_coefficient
        # Increase uncertainty when state is extreme
        uncertainty_factor = 1 + np.abs(C - 0.5) * 0.5
        return base * uncertainty_factor
    
    def euler_maruyama(
        self,
        C: np.ndarray,
        drift: np.ndarray,
        dt: float
    ) -> np.ndarray:
        """
        Euler-Maruyama integration for SDE
        
        Args:
            C: Current state
            drift: Deterministic drift term F(C, E, G)
            dt: Time step
        
        Returns:
            Updated state C(t+dt)
        """
        # Diffusion term: σ(C) dW
        sigma = self.diffusion_coefficient(C)
        dW = np.random.randn(len(C)) * np.sqrt(dt)
        
        # Euler-Maruyama update
        dC = drift * dt + sigma * dW
        C_new = C + dC
        
        return C_new
    
    def simulate_trajectory(
        self,
        C0: np.ndarray,
        drift_function: Callable[[np.ndarray, float], np.ndarray],
        dt: float,
        n_steps: int,
        record_every: int = 1
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Simulate full SDE trajectory
        
        Args:
            C0: Initial state
            drift_function: Function that returns drift F(C, t)
            dt: Time step
            n_steps: Number of steps
            record_every: Record every N steps
        
        Returns:
            trajectory: Array of states (n_recorded, n_dim)
            times: Array of times
        """
        n_dim = len(C0)
        n_recorded = n_steps // record_every + 1
        
        trajectory = np.zeros((n_recorded, n_dim))
        times = np.zeros(n_recorded)
        
        C = C0.copy()
        trajectory[0] = C
        times[0] = 0
        
        record_idx = 1
        for step in range(n_steps):
            t = step * dt
            drift = drift_function(C, t)
            C = self.euler_maruyama(C, drift, dt)
            
            if (step + 1) % record_every == 0:
                trajectory[record_idx] = C
                times[record_idx] = (step + 1) * dt
                record_idx += 1
        
        return trajectory[:record_idx], times[:record_idx]
    
    def ensemble_simulation(
        self,
        C0: np.ndarray,
        drift_function: Callable,
        dt: float,
        n_steps: int,
        n_ensemble: int = 100
    ) -> np.ndarray:
        """
        Run ensemble of SDE simulations for uncertainty quantification
        
        Returns:
            Ensemble trajectories (n_ensemble, n_steps+1, n_dim)
        """
        ensemble = np.zeros((n_ensemble, n_steps + 1, len(C0)))
        
        for i in range(n_ensemble):
            # Reset random seed for each ensemble member
            self.params.noise_seed = None
            traj, _ = self.simulate_trajectory(C0, drift_function, dt, n_steps)
            ensemble[i, :len(traj)] = traj
            # Pad if needed
            if len(traj) < n_steps + 1:
                ensemble[i, len(traj):] = traj[-1]
        
        return ensemble
