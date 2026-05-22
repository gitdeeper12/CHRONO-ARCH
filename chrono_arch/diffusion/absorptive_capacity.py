"""Absorptive capacity model
Equation (11): Ψ_i(K, A) = α·K_iᵝ·Σ_j A_ij·max(K_j − K_i, 0)
"""

import numpy as np
from typing import Optional, Tuple
from dataclasses import dataclass

@dataclass
class DiffusionParameters:
    """Parameters for knowledge diffusion model"""
    alpha: float = 0.7          # Institutional openness parameter α ∈ (0,1]
    beta: float = 1.5           # Superlinear absorptive capacity β > 1
    base_diffusion_rate: float = 0.05
    
    def validate(self):
        if not 0 < self.alpha <= 1:
            raise ValueError(f"alpha must be in (0,1], got {self.alpha}")
        if self.beta <= 1:
            raise ValueError(f"beta must be > 1, got {self.beta}")

def absorptive_capacity_term(
    K: np.ndarray,
    A: np.ndarray,
    params: DiffusionParameters
) -> np.ndarray:
    """
    Nonlinear absorptive capacity term Ψ(K, A)
    Equation (11): Ψ_i(K, A) = α·K_iᵝ·Σ_j A_ij·max(K_j − K_i, 0)
    
    Captures three phenomena:
    1. Absorptive capacity: higher K leads to faster incorporation
    2. Institutional resistance: α represents openness
    3. Knowledge saturation: diminishing returns from β > 1
    
    Args:
        K: Knowledge levels per node
        A: Adjacency matrix
        params: Diffusion parameters (α, β)
    
    Returns:
        Ψ(K, A) nonlinear term
    """
    n = len(K)
    psi = np.zeros(n)
    
    for i in range(n):
        # Avoid division by zero and handle negative K
        K_i = max(K[i], 1e-6)
        
        # Absorptive capacity factor: α·K_iᵝ
        absorptive_factor = params.alpha * (K_i ** params.beta)
        
        # Knowledge inflow from neighbors (only positive differences)
        inflow = 0
        for j in range(n):
            if i != j and A[i, j] > 0:
                diff = K[j] - K[i]
                if diff > 0:
                    inflow += A[i, j] * diff
        
        psi[i] = absorptive_factor * inflow
    
    return psi

def nonlinear_diffusion(
    K: np.ndarray,
    A: np.ndarray,
    dt: float,
    params: Optional[DiffusionParameters] = None
) -> np.ndarray:
    """
    Complete nonlinear diffusion model
    dK/dt = -L·K + Ψ(K, A)
    """
    if params is None:
        params = DiffusionParameters()
    
    params.validate()
    
    # Compute Laplacian
    D = np.diag(np.sum(A, axis=1))
    L = D - A
    
    # Linear term: -L·K
    linear = -L @ K
    
    # Nonlinear term: Ψ(K, A)
    nonlinear = absorptive_capacity_term(K, A, params)
    
    # Total change
    dK_dt = linear + nonlinear
    
    # Update with clamping to prevent negative knowledge
    K_new = K + dK_dt * dt
    K_new = np.maximum(K_new, 0)
    
    return K_new

def create_diffusion_scenario(
    scenario: str = "default"
) -> DiffusionParameters:
    """Create diffusion parameters for different scenarios"""
    scenarios = {
        "default": DiffusionParameters(alpha=0.7, beta=1.5),
        "open_society": DiffusionParameters(alpha=0.9, beta=1.3),
        "closed_society": DiffusionParameters(alpha=0.3, beta=1.8),
        "high_absorptive": DiffusionParameters(alpha=0.95, beta=2.0),
        "resistant": DiffusionParameters(alpha=0.2, beta=1.2),
    }
    
    if scenario not in scenarios:
        raise ValueError(f"Unknown scenario: {scenario}. Available: {list(scenarios.keys())}")
    
    return scenarios[scenario]
