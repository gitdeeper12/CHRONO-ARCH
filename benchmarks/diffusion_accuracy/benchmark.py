"""Benchmark for knowledge diffusion accuracy"""

import sys
sys.path.append('../..')

import numpy as np
from chrono_arch.diffusion.knowledge_diffusion import linear_diffusion, compute_laplacian
from chrono_arch.diffusion.absorptive_capacity import nonlinear_diffusion, DiffusionParameters

def test_linear_conservation():
    """Test that linear diffusion conserves total knowledge"""
    n = 5
    A = np.random.rand(n, n) * 0.3
    A = (A + A.T) / 2
    np.fill_diagonal(A, 0)
    
    K = np.random.rand(n)
    total_initial = np.sum(K)
    
    for _ in range(100):
        K = linear_diffusion(K, A, dt=0.1)
    
    total_final = np.sum(K)
    conservation_error = abs(total_final - total_initial) / total_initial
    
    return conservation_error

def test_diffusion_convergence():
    """Test that diffusion converges to uniform distribution"""
    n = 5
    A = np.ones((n, n)) * 0.1
    np.fill_diagonal(A, 0)
    
    K = np.array([1.0, 0.2, 0.8, 0.3, 0.6])
    
    for _ in range(500):
        K = linear_diffusion(K, A, dt=0.1)
    
    final_variance = np.var(K)
    return final_variance

if __name__ == '__main__':
    cons_error = test_linear_conservation()
    print(f"Conservation error: {cons_error:.6f}")
    
    final_var = test_diffusion_convergence()
    print(f"Final variance after convergence: {final_var:.6f}")
