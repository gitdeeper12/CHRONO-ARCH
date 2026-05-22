"""Stability functional S(t) = Σ_i w_i·C_i(t) − λ·σ(E(t))"""

import numpy as np
from typing import Optional
from dataclasses import dataclass

@dataclass
class StabilityWeights:
    environmental_adaptation: float = 0.25
    resource_availability: float = 0.20
    technological_complexity: float = 0.10
    sociopolitical_stability: float = 0.30
    demographic_pressure: float = -0.10
    economic_integration: float = 0.15
    
    def to_array(self, n_resources: int = 3) -> np.ndarray:
        weights = np.array([
            self.environmental_adaptation,
            self.technological_complexity,
            self.sociopolitical_stability,
            self.demographic_pressure,
            self.economic_integration
        ])
        resource_weight = self.resource_availability / n_resources
        weights = np.concatenate([weights, np.full(n_resources, resource_weight)])
        return weights

def stability_functional(C: np.ndarray, E_volatility: float, 
                         weights: Optional[StabilityWeights] = None,
                         lambda_stress: float = 0.2) -> float:
    if weights is None:
        weights = StabilityWeights()
    w = weights.to_array(len(C) - 5)
    if len(w) > len(C):
        w = w[:len(C)]
    elif len(w) < len(C):
        w = np.pad(w, (0, len(C) - len(w)))
    weighted_sum = np.sum(w * C)
    return max(0.0, min(1.0, weighted_sum - lambda_stress * E_volatility))

def stability_category(stability: float, threshold: float = 0.35) -> str:
    if stability > threshold * 1.5:
        return "STABLE"
    elif stability > threshold * 1.2:
        return "MODERATE"
    elif stability > threshold:
        return "FRAGILE"
    elif stability > threshold * 0.5:
        return "COLLAPSING"
    else:
        return "COLLAPSED"

def compute_environmental_volatility(E_history: list, window: int = 10) -> float:
    if len(E_history) < 2:
        return 0.0
    recent = E_history[-window:] if len(E_history) >= window else E_history
    all_values = np.array([val for e in recent for val in (e if hasattr(e, '__iter__') else [e])])
    return np.std(all_values) if len(all_values) > 1 else 0.0
