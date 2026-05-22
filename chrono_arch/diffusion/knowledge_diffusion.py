"""Knowledge diffusion dynamics
Equation (9): dK_i/dt = Σ_{j≠i} A_ij(t)·(K_j − K_i)
Equation (10): dK/dt = −L(t)·K + Ψ(K, A)
"""

import numpy as np
from typing import Optional, Tuple

def linear_diffusion(
    K: np.ndarray,
    A: np.ndarray,
    dt: float
) -> np.ndarray:
    """
    Linear knowledge diffusion on temporal graph
    Equation (9): dK_i/dt = Σ_{j≠i} A_ij(t)·(K_j − K_i)
    
    Args:
        K: Knowledge levels per node [n_nodes]
        A: Adjacency matrix [n_nodes, n_nodes]
        dt: Time step
    
    Returns:
        Updated knowledge levels
    """
    n = len(K)
    dK_dt = np.zeros(n)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dK_dt[i] += A[i, j] * (K[j] - K[i])
    
    return K + dK_dt * dt

def compute_laplacian(A: np.ndarray) -> np.ndarray:
    """
    Compute graph Laplacian L = D - A
    where D_ii = Σ_j A_ij
    """
    D = np.diag(np.sum(A, axis=1))
    return D - A

def laplacian_diffusion(
    K: np.ndarray,
    L: np.ndarray,
    dt: float
) -> np.ndarray:
    """
    Knowledge diffusion using graph Laplacian
    dK/dt = -L·K (simplified from Eq. 10)
    """
    dK_dt = -L @ K
    return K + dK_dt * dt

def nonlinear_diffusion_full(
    K: np.ndarray,
    A: np.ndarray,
    L: np.ndarray,
    dt: float,
    nonlinear_term: np.ndarray
) -> np.ndarray:
    """
    Generalized nonlinear diffusion
    Equation (10): dK/dt = −L(t)·K + Ψ(K, A)
    
    Args:
        K: Knowledge levels
        A: Adjacency matrix
        L: Graph Laplacian
        dt: Time step
        nonlinear_term: Ψ(K, A) - nonlinear correction
    
    Returns:
        Updated knowledge levels
    """
    linear_part = -L @ K
    dK_dt = linear_part + nonlinear_term
    return K + dK_dt * dt
