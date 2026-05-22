"""Co-evolving system: dA/dt = Φ(A(t), C(t))"""

import numpy as np
from typing import Dict, Any, Optional

def co_evolve_graph(
    A: np.ndarray,
    C: np.ndarray,
    dt: float,
    params: Optional[Dict[str, Any]] = None
) -> np.ndarray:
    if params is None:
        params = {
            'tech_diffusion_rate': 0.05,
            'stability_influence': 0.03,
            'trade_sensitivity': 0.04,
            'max_weight': 1.0
        }
    
    n = len(C)
    dA_dt = np.zeros((n, n))
    
    tech_C = C[1] if len(C) > 1 else 0.5
    stability = C[2] if len(C) > 2 else 0.5
    economy = C[5] if len(C) > 5 else 0.0
    
    for i in range(n):
        for j in range(n):
            if i != j:
                dA_dt[i, j] += params['tech_diffusion_rate'] * (1 - A[i, j])
    
    dA_dt += params['stability_influence'] * stability * (1 - A)
    dA_dt += params['trade_sensitivity'] * max(0, economy) * (1 - A)
    
    dA_dt = (dA_dt + dA_dt.T) / 2
    A_new = A + dA_dt * dt
    A_new = np.clip(A_new, 0, params['max_weight'])
    np.fill_diagonal(A_new, 0)
    
    return A_new

def update_state_from_graph(C: np.ndarray, A: np.ndarray, dt: float, influence_rate: float = 0.01) -> np.ndarray:
    n = len(C)
    dC_from_graph = np.zeros(n)
    degrees = np.sum(A, axis=1)
    for i in range(n):
        if degrees[i] > 0:
            neighbor_sum = np.sum(A[i] * C)
            dC_from_graph[i] = influence_rate * (neighbor_sum / degrees[i] - C[i])
    return C + dC_from_graph * dt
