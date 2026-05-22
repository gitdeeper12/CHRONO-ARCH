"""Environmental coupling model F_E = Γ · ∇E(t)"""

import numpy as np
from typing import Optional
from dataclasses import dataclass

@dataclass
class SensitivityTensor:
    matrix: np.ndarray
    
    def __post_init__(self):
        if self.matrix.ndim != 2:
            raise ValueError(f"Sensitivity tensor must be 2D, got {self.matrix.ndim}D")
    
    @property
    def n_dim(self) -> int:
        return self.matrix.shape[0]
    
    @property
    def n_env(self) -> int:
        return self.matrix.shape[1]
    
    def __matmul__(self, other: np.ndarray) -> np.ndarray:
        return self.matrix @ other
    
    @classmethod
    def diagonal(cls, n_dim: int, n_env: int = 3, sensitivity: float = 0.1) -> "SensitivityTensor":
        matrix = np.zeros((n_dim, n_env))
        for i in range(min(n_dim, n_env)):
            matrix[i, i] = sensitivity
        return cls(matrix=matrix)

def gradient_E(E: np.ndarray, dt: float) -> np.ndarray:
    if len(E.shape) == 1:
        return np.zeros_like(E)
    return np.gradient(E, dt, axis=0)

def coupling_force(E: np.ndarray, sensitivity: SensitivityTensor, dt: float = 1.0) -> np.ndarray:
    if len(E.shape) == 1:
        grad = E
    else:
        grad = gradient_E(E, dt)
        grad = grad[-1] if len(grad.shape) > 1 else grad
    if len(grad) < sensitivity.n_env:
        grad_padded = np.zeros(sensitivity.n_env)
        grad_padded[:len(grad)] = grad
        grad = grad_padded
    elif len(grad) > sensitivity.n_env:
        grad = grad[:sensitivity.n_env]
    return sensitivity @ grad
