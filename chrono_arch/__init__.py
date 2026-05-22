"""CHRONO-ARCH: Computational Framework for Temporal Archaeology"""

__version__ = "1.0.0"
__author__ = "Samir Baladi"
__license__ = "MIT"
__doi__ = "10.5281/zenodo.20330475"

from chrono_arch.state.state_vector import StateVector
from chrono_arch.graph.temporal_graph import TemporalGraph
from chrono_arch.simulation.engine import SimulationEngine, SimulationConfig, run_example_simulation
from chrono_arch.environment.env_model import EnvironmentalField

__all__ = [
    "StateVector", "TemporalGraph", "SimulationEngine", 
    "SimulationConfig", "EnvironmentalField", "run_example_simulation"
]
