"""Temporal Interaction Graph G(t) = (V, A(t))
Equation (4): Temporal interaction graph with multi-dimensional edge weights
"""

import numpy as np
from typing import List, Tuple, Optional, Dict, Any
from dataclasses import dataclass, field

@dataclass
class TemporalGraph:
    """Time-varying weighted graph representing inter-civilizational interactions"""
    n_nodes: int
    node_labels: List[str] = field(default_factory=list)
    adjacency_history: List[np.ndarray] = field(default_factory=list)
    time_steps: List[float] = field(default_factory=list)
    
    def __post_init__(self):
        if not self.node_labels:
            self.node_labels = [f"Civ_{i}" for i in range(self.n_nodes)]
    
    def add_adjacency(self, A: np.ndarray, t: float):
        if A.shape != (self.n_nodes, self.n_nodes):
            raise ValueError(f"Adjacency shape must be ({self.n_nodes},{self.n_nodes}), got {A.shape}")
        self.adjacency_history.append(A.copy())
        self.time_steps.append(t)
    
    def get_adjacency(self, t: float, method: str = "nearest") -> np.ndarray:
        if not self.time_steps:
            return np.zeros((self.n_nodes, self.n_nodes))
        
        if method == "nearest":
            idx = np.argmin(np.abs(np.array(self.time_steps) - t))
            return self.adjacency_history[idx].copy()
        elif method == "linear":
            times = np.array(self.time_steps)
            if t <= times[0]:
                return self.adjacency_history[0].copy()
            if t >= times[-1]:
                return self.adjacency_history[-1].copy()
            idx = np.searchsorted(times, t)
            t1, t2 = times[idx-1], times[idx]
            A1, A2 = self.adjacency_history[idx-1], self.adjacency_history[idx]
            alpha = (t - t1) / (t2 - t1)
            return (1 - alpha) * A1 + alpha * A2
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def compute_degree_matrix(self, A: Optional[np.ndarray] = None) -> np.ndarray:
        if A is None:
            A = self.get_adjacency(self.time_steps[-1] if self.time_steps else 0)
        return np.diag(np.sum(A, axis=1))
    
    def compute_laplacian(self, A: Optional[np.ndarray] = None) -> np.ndarray:
        if A is None:
            A = self.get_adjacency(self.time_steps[-1] if self.time_steps else 0)
        D = self.compute_degree_matrix(A)
        return D - A
    
    @classmethod
    def from_edge_list(cls, n_nodes: int, edges: List[Tuple[int, int, float]], 
                       node_labels: Optional[List[str]] = None) -> "TemporalGraph":
        graph = cls(n_nodes=n_nodes, node_labels=node_labels or [f"Civ_{i}" for i in range(n_nodes)])
        A = np.zeros((n_nodes, n_nodes))
        for i, j, w in edges:
            A[i, j] = w
            A[j, i] = w
        graph.add_adjacency(A, t=0.0)
        return graph
    
    def __repr__(self) -> str:
        return f"TemporalGraph(n_nodes={self.n_nodes}, n_snapshots={len(self.adjacency_history)})"
