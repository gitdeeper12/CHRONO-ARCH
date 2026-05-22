"""Environmental forcing model E(t) = [climate, temperature, precipitation]ᵀ"""

import numpy as np
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class EnvironmentalField:
    climate: float = 0.0
    temperature: float = 0.0
    precipitation: float = 0.0
    additional_fields: Optional[np.ndarray] = None
    
    def to_array(self) -> np.ndarray:
        base = np.array([self.climate, self.temperature, self.precipitation])
        if self.additional_fields is not None:
            return np.concatenate([base, self.additional_fields])
        return base
    
    @classmethod
    def from_array(cls, arr: np.ndarray) -> "EnvironmentalField":
        if len(arr) < 3:
            raise ValueError(f"Array too short: need at least 3 dimensions, got {len(arr)}")
        return cls(
            climate=float(arr[0]),
            temperature=float(arr[1]),
            precipitation=float(arr[2]),
            additional_fields=arr[3:] if len(arr) > 3 else None
        )

def generate_stochastic_environment(dt: float, n_steps: int, seed: Optional[int] = None) -> np.ndarray:
    if seed is not None:
        np.random.seed(seed)
    E = np.random.randn(n_steps, 3) * 0.1
    trend = np.linspace(0, 0.2, n_steps)
    E[:, 0] += trend
    return E
