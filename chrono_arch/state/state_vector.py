"""Civilizational State Vector C(t) ∈ ℝⁿ
Definition 2.1 - Civilizational State Vector
"""

import numpy as np
from dataclasses import dataclass, field
from typing import Optional, List

@dataclass
class StateVector:
    """Civilizational state vector C(t) ∈ ℝⁿ"""
    environmental_adaptation: float = 0.5      # C₁ ∈ [0, 1]
    resource_availability: List[float] = field(default_factory=lambda: [1.0])
    technological_complexity: float = 0.5      # C₃ ∈ ℝ₊
    sociopolitical_stability: float = 0.5      # C₄ ∈ [0, 1]
    demographic_pressure: float = 0.5          # C₅ ∈ ℝ₊
    economic_integration: float = 0.0          # C₆ ∈ ℝ
    additional_dimensions: Optional[np.ndarray] = None
    
    def __post_init__(self):
        self._validate()
    
    def _validate(self):
        if not 0 <= self.environmental_adaptation <= 1:
            raise ValueError(f"environmental_adaptation must be in [0,1], got {self.environmental_adaptation}")
        if not 0 <= self.sociopolitical_stability <= 1:
            raise ValueError(f"sociopolitical_stability must be in [0,1], got {self.sociopolitical_stability}")
        if self.technological_complexity < 0:
            raise ValueError(f"technological_complexity must be >= 0, got {self.technological_complexity}")
        if self.demographic_pressure < 0:
            raise ValueError(f"demographic_pressure must be >= 0, got {self.demographic_pressure}")
        for r in self.resource_availability:
            if r < 0:
                raise ValueError(f"resource_availability must be >= 0, got {r}")
    
    def to_array(self) -> np.ndarray:
        """Convert to numpy array ℝⁿ"""
        base = np.array([
            self.environmental_adaptation,
            self.technological_complexity,
            self.sociopolitical_stability,
            self.demographic_pressure,
            self.economic_integration
        ])
        resources = np.array(self.resource_availability)
        if self.additional_dimensions is not None:
            return np.concatenate([base, resources, self.additional_dimensions])
        return np.concatenate([base, resources])
    
    @classmethod
    def from_array(cls, arr: np.ndarray, n_resources: int = 3) -> "StateVector":
        if len(arr) < 5:
            raise ValueError(f"Array too short: need at least 5 dimensions, got {len(arr)}")
        
        return cls(
            environmental_adaptation=float(arr[0]),
            technological_complexity=float(arr[1]),
            sociopolitical_stability=float(arr[2]),
            demographic_pressure=float(arr[3]),
            economic_integration=float(arr[4]),
            resource_availability=list(arr[5:5+n_resources]),
            additional_dimensions=arr[5+n_resources:] if len(arr) > 5+n_resources else None
        )
    
    def copy(self) -> "StateVector":
        return StateVector(
            environmental_adaptation=self.environmental_adaptation,
            resource_availability=self.resource_availability.copy(),
            technological_complexity=self.technological_complexity,
            sociopolitical_stability=self.sociopolitical_stability,
            demographic_pressure=self.demographic_pressure,
            economic_integration=self.economic_integration,
            additional_dimensions=self.additional_dimensions.copy() if self.additional_dimensions is not None else None
        )
    
    def __repr__(self) -> str:
        return f"StateVector(C₁={self.environmental_adaptation:.3f}, C₃={self.technological_complexity:.3f}, C₄={self.sociopolitical_stability:.3f})"
