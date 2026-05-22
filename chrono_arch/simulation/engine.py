"""Main simulation engine implementing Algorithm 1"""

import numpy as np
import random
from typing import List, Dict, Optional, Any
from dataclasses import dataclass, field

from ..state.state_vector import StateVector
from ..state.evolution import evolve_state, EvolutionParameters, create_default_parameters
from ..graph.temporal_graph import TemporalGraph
from ..graph.graph_measures import compute_all_measures
from ..collapse.stability import stability_functional, StabilityWeights, compute_environmental_volatility
from ..collapse.early_warning import compute_all_ews, collapse_alert

@dataclass
class SimulationResult:
    states: List[np.ndarray]
    stabilities: List[float]
    knowledge_levels: List[np.ndarray]
    times: List[float]
    collapse_events: List[Dict]
    early_warnings: Dict[str, List[float]]
    graph_measures: List[Dict]

@dataclass
class SimulationConfig:
    dt: float = 1.0
    n_civilizations: int = 1
    n_dimensions: int = 6
    collapse_threshold: float = 0.35
    use_stochastic: bool = True
    use_graph_dynamics: bool = True
    record_every: int = 1
    random_seed: Optional[int] = None

class SimulationEngine:
    def __init__(self, config: Optional[SimulationConfig] = None):
        self.config = config or SimulationConfig()
        if self.config.random_seed is not None:
            np.random.seed(self.config.random_seed)
            random.seed(self.config.random_seed)
        self._initialize_components()
    
    def _initialize_components(self):
        n = self.config.n_dimensions
        self.evolution_params = create_default_parameters(n)
        self.stability_weights = StabilityWeights()
    
    def _compute_drift(self, C: np.ndarray, E: np.ndarray, A: np.ndarray, t: float) -> np.ndarray:
        n = len(C)
        drift = -0.1 * (C - 0.5)
        for i in range(min(len(E), n)):
            drift[i] += 0.05 * E[i]
        if self.config.n_civilizations > 1 and A.shape[0] == n:
            degrees = np.sum(A, axis=1)
            for i in range(n):
                if degrees[i] > 0:
                    neighbor_sum = np.sum(A[i] * C)
                    drift[i] += 0.02 * (neighbor_sum / degrees[i] - C[i])
        return drift
    
    def simulate(self, C0: StateVector, E0, G0: Optional[TemporalGraph] = None, T: float = 1000.0) -> SimulationResult:
        n_steps = int(T / self.config.dt)
        C = C0.to_array()
        E = np.array([E0.climate, E0.temperature, E0.precipitation])
        K = np.ones(self.config.n_civilizations) * 0.5
        stability_history = []
        
        states, stabilities, knowledge_levels, times = [], [], [], []
        collapse_events = []
        graph_measures_list = []
        ews_signals = {'variance': [], 'autocorrelation_lag1': [], 'critical_slowing_down': []}
        
        if G0 is not None and self.config.use_graph_dynamics:
            A = G0.get_adjacency(0)
        else:
            A = np.zeros((self.config.n_civilizations, self.config.n_civilizations))
        
        for step in range(n_steps):
            t = step * self.config.dt
            if self.config.use_stochastic:
                E = E + np.random.randn(len(E)) * 0.01 * np.sqrt(self.config.dt)
            if self.config.use_graph_dynamics and self.config.n_civilizations > 1:
                for i in range(self.config.n_civilizations):
                    for j in range(self.config.n_civilizations):
                        if i != j:
                            diff = abs(C[i] - C[j]) if i < len(C) and j < len(C) else 0
                            A[i, j] = min(1.0, A[i, j] + 0.001 * (1 - diff) * self.config.dt)
                            A[j, i] = A[i, j]
            drift = self._compute_drift(C, E, A, t)
            C = C + drift * self.config.dt
            if self.config.use_stochastic:
                C = C + np.random.randn(len(C)) * 0.05 * np.sqrt(self.config.dt)
            if self.config.n_civilizations > 1:
                for i in range(self.config.n_civilizations):
                    degree = np.sum(A[i])
                    if degree > 0:
                        neighbor_influence = np.sum(A[i] * K) / degree
                        K[i] += 0.05 * (neighbor_influence - K[i]) * self.config.dt
                        K[i] = max(0.0, min(1.0, K[i]))
            E_volatility = compute_environmental_volatility([E], window=1)
            stability = stability_functional(C[:min(len(C), 6)], E_volatility, self.stability_weights)
            stability_history.append(stability)
            if stability < self.config.collapse_threshold:
                collapse_events.append({'time': t, 'stability': stability, 'state': C.copy()})
            if len(stability_history) > 20:
                ews = compute_all_ews(stability_history, window=20)
                for key in ews_signals:
                    if ews[key]:
                        ews_signals[key].append(ews[key][-1])
            if step % self.config.record_every == 0:
                states.append(C.copy())
                stabilities.append(stability)
                knowledge_levels.append(K.copy())
                times.append(t)
                if self.config.n_civilizations > 1:
                    graph_measures_list.append(compute_all_measures(A))
        
        return SimulationResult(
            states=states, stabilities=stabilities, knowledge_levels=knowledge_levels,
            times=times, collapse_events=collapse_events, early_warnings=ews_signals,
            graph_measures=graph_measures_list
        )

def run_example_simulation() -> SimulationResult:
    from ..environment.env_model import EnvironmentalField
    config = SimulationConfig(dt=1.0, n_civilizations=3, n_dimensions=6, 
                              collapse_threshold=0.35, use_stochastic=True)
    engine = SimulationEngine(config)
    C0 = StateVector(environmental_adaptation=0.7, resource_availability=[1.0, 1.0, 1.0],
                     technological_complexity=0.5, sociopolitical_stability=0.6,
                     demographic_pressure=0.4, economic_integration=0.3)
    E0 = EnvironmentalField(climate=0.0, temperature=0.0, precipitation=0.0)
    result = engine.simulate(C0, E0, T=100.0)
    print(f"Simulation completed: {len(result.times)} steps, {len(result.collapse_events)} collapses")
    return result
