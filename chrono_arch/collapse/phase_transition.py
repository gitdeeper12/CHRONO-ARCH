"""Phase transition theory: φ(C) = ∇_C S(C)"""

import numpy as np
from typing import Tuple
from enum import Enum

class Phase(Enum):
    STABLE = "Phase I — Stable"
    CRITICAL = "Phase II — Critical"
    COLLAPSE = "Phase III — Collapse"

def compute_stability_gradient(C: np.ndarray, epsilon: float = 0.01) -> np.ndarray:
    n = len(C)
    gradient = np.zeros(n)
    def stability(C):
        return np.mean(C[:4]) - 0.2 * np.std(C)
    for i in range(n):
        C_plus = C.copy()
        C_plus[i] += epsilon
        C_minus = C.copy()
        C_minus[i] -= epsilon
        gradient[i] = (stability(C_plus) - stability(C_minus)) / (2 * epsilon)
    return gradient

def phase_transition_detector(C: np.ndarray, stability_gradient: np.ndarray, 
                               collapse_threshold: float = 0.35) -> Tuple[Phase, float]:
    stability = np.mean(C[:4])
    grad_norm = np.linalg.norm(stability_gradient)
    if stability > collapse_threshold * 1.5:
        return Phase.STABLE, 0.0
    elif stability > collapse_threshold:
        if grad_norm > 5.0:
            return Phase.CRITICAL, min(grad_norm / 10, 1.0)
        return Phase.STABLE, 0.1
    else:
        return Phase.COLLAPSE, 1.0 - stability / collapse_threshold if stability > 0 else 1.0
