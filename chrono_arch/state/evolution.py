"""Master evolution equation dC/dt = F(C, E, G, t)
Equation (2): dC(t)/dt = F(C(t), E(t), G(t), t)
Equation (3): dC/dt = A·C + Cᵀ·B·C + G(E, G_graph)
"""

import numpy as np
from typing import Optional, Tuple
from dataclasses import dataclass

@dataclass
class EvolutionParameters:
    """Parameters for the evolution equation"""
    A_matrix: np.ndarray          # Linear stability matrix A ∈ ℝⁿˣⁿ
    B_tensor: np.ndarray          # Bilinear interaction tensor B ∈ ℝⁿˣⁿˣⁿ
    coupling_weight: float = 1.0
    
    def __post_init__(self):
        n = self.A_matrix.shape[0]
        if self.B_tensor.shape != (n, n, n):
            raise ValueError(f"B_tensor shape must be ({n},{n},{n}), got {self.B_tensor.shape}")

def linear_term(C: np.ndarray, A: np.ndarray) -> np.ndarray:
    """Linear term A·C from Eq. (3)"""
    return A @ C

def quadratic_term(C: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Quadratic term Cᵀ·B·C from Eq. (3)"""
    n = len(C)
    result = np.zeros(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i] += B[i, j, k] * C[j] * C[k]
    return result

def coupling_term(C: np.ndarray, E: np.ndarray, A: np.ndarray, 
                  sensitivity: Optional[np.ndarray] = None) -> np.ndarray:
    """Environmental and network coupling term G(E, G_graph)"""
    n = len(C)
    result = np.zeros(n)
    
    if sensitivity is not None and len(E) > 0:
        n_env = min(sensitivity.shape[1] if sensitivity.ndim > 1 else 1, len(E))
        for i in range(min(n, sensitivity.shape[0] if sensitivity.ndim > 1 else n)):
            for j in range(n_env):
                gamma = sensitivity[i, j] if sensitivity.ndim > 1 else sensitivity[i]
                result[i] += gamma * E[j] * 0.1
    
    if A is not None and A.shape[0] == n:
        degrees = np.sum(A, axis=1)
        for i in range(n):
            if degrees[i] > 0:
                neighbor_sum = np.sum(A[i] * C)
                result[i] += 0.05 * (neighbor_sum / degrees[i])
    
    return result

def evolve_state(
    C: np.ndarray,
    E: np.ndarray,
    A: np.ndarray,
    dt: float,
    params: EvolutionParameters,
    sensitivity: Optional[np.ndarray] = None,
    method: str = "euler"
) -> np.ndarray:
    """Integrate the master evolution equation (Eq. 2-3)"""
    def dC_dt(t: float, C_t: np.ndarray) -> np.ndarray:
        lin = linear_term(C_t, params.A_matrix)
        quad = quadratic_term(C_t, params.B_tensor)
        coup = coupling_term(C_t, E, A, sensitivity)
        return lin + quad + coup
    
    if method == "euler":
        return C + dC_dt(0, C) * dt
    elif method == "rk4":
        k1 = dC_dt(0, C)
        k2 = dC_dt(dt/2, C + dt/2 * k1)
        k3 = dC_dt(dt/2, C + dt/2 * k2)
        k4 = dC_dt(dt, C + dt * k3)
        return C + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)
    else:
        raise ValueError(f"Unknown method: {method}")

def create_default_parameters(n_dim: int) -> EvolutionParameters:
    """Create default parameters for an n-dimensional system"""
    A = -np.eye(n_dim) * 0.1
    for i in range(n_dim):
        for j in range(n_dim):
            if i != j:
                A[i, j] = 0.02 * np.random.randn()
    
    B = np.random.randn(n_dim, n_dim, n_dim) * 0.01
    return EvolutionParameters(A_matrix=A, B_tensor=B)
