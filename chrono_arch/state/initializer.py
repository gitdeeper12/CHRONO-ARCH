"""State initialization utilities"""

import numpy as np
from typing import Optional
from .state_vector import StateVector

def initialize_state(
    n_dimensions: int = 6,
    n_resources: int = 3,
    mode: str = "default",
    random_seed: Optional[int] = None
) -> StateVector:
    """Initialize a civilizational state vector"""
    if random_seed is not None:
        np.random.seed(random_seed)
    
    if mode == "default":
        return StateVector(
            environmental_adaptation=0.6,
            resource_availability=[1.0] * n_resources,
            technological_complexity=0.5,
            sociopolitical_stability=0.6,
            demographic_pressure=0.4,
            economic_integration=0.3
        )
    elif mode == "stable":
        return StateVector(
            environmental_adaptation=0.85,
            resource_availability=[1.5, 1.3, 1.2][:n_resources],
            technological_complexity=0.8,
            sociopolitical_stability=0.9,
            demographic_pressure=0.3,
            economic_integration=0.7
        )
    elif mode == "fragile":
        return StateVector(
            environmental_adaptation=0.3,
            resource_availability=[0.5, 0.4, 0.6][:n_resources],
            technological_complexity=0.4,
            sociopolitical_stability=0.35,
            demographic_pressure=0.8,
            economic_integration=0.1
        )
    elif mode == "collapsing":
        return StateVector(
            environmental_adaptation=0.2,
            resource_availability=[0.3, 0.2, 0.4][:n_resources],
            technological_complexity=0.3,
            sociopolitical_stability=0.25,
            demographic_pressure=0.9,
            economic_integration=-0.2
        )
    elif mode == "random":
        return StateVector(
            environmental_adaptation=np.random.uniform(0, 1),
            resource_availability=list(np.random.uniform(0.3, 1.5, n_resources)),
            technological_complexity=np.random.uniform(0, 1),
            sociopolitical_stability=np.random.uniform(0, 1),
            demographic_pressure=np.random.uniform(0, 1),
            economic_integration=np.random.uniform(-0.5, 0.5)
        )
    else:
        raise ValueError(f"Unknown mode: {mode}")
