"""Benchmark for probabilistic calibration"""

import sys
sys.path.append('../..')

import numpy as np
from chrono_arch.probabilistic.particle_filter import ParticleFilter, ParticleFilterConfig
from chrono_arch.probabilistic.fokker_planck import FokkerPlanckSolver

def test_particle_filter_convergence():
    """Test that particle filter converges to true state"""
    n_dim = 2
    config = ParticleFilterConfig(n_particles=1000)
    pf = ParticleFilter(n_dim, config)
    
    true_state = np.array([0.5, 0.5])
    pf.initialize(true_state, np.eye(n_dim) * 0.1)
    
    def transition_fn(x):
        return x + 0.01 * np.random.randn(n_dim)
    
    def likelihood_fn(x, obs):
        return -np.sum((x - obs)**2) / 0.1
    
    for _ in range(50):
        pf.predict(transition_fn)
        obs = true_state + np.random.randn(n_dim) * 0.05
        pf.update(obs, likelihood_fn)
    
    estimated_mean = pf.get_mean()
    error = np.linalg.norm(estimated_mean - true_state)
    
    return error

if __name__ == '__main__':
    error = test_particle_filter_convergence()
    print(f"Particle filter estimation error: {error:.4f}")
