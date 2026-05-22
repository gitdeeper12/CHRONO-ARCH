"""Causal inference framework
Equation (18): G_causal = (V_causal, E_causal)
Directed acyclic causal graph structure
"""

import numpy as np
from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass, field

@dataclass
class CausalGraph:
    """Directed acyclic causal graph for civilizational variables"""
    
    variables: List[str]
    edges: List[Tuple[int, int]] = field(default_factory=list)  # (from, to) directed edges
    
    def __post_init__(self):
        self._validate_no_cycles()
    
    def _validate_no_cycles(self):
        """Ensure graph is acyclic (simplified check)"""
        # Build adjacency
        adj = {i: [] for i in range(len(self.variables))}
        for u, v in self.edges:
            adj[u].append(v)
        
        # DFS cycle detection
        visited = set()
        stack = set()
        
        def has_cycle(node):
            visited.add(node)
            stack.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if has_cycle(neighbor):
                        return True
                elif neighbor in stack:
                    return True
            stack.remove(node)
            return False
        
        for i in range(len(self.variables)):
            if i not in visited:
                if has_cycle(i):
                    raise ValueError("Causal graph must be acyclic")
    
    def add_edge(self, cause: str, effect: str):
        """Add causal edge from cause to effect"""
        if cause not in self.variables:
            raise ValueError(f"Unknown variable: {cause}")
        if effect not in self.variables:
            raise ValueError(f"Unknown variable: {effect}")
        
        u = self.variables.index(cause)
        v = self.variables.index(effect)
        
        self.edges.append((u, v))
        self._validate_no_cycles()
    
    def get_parents(self, variable: str) -> List[str]:
        """Get direct causes of a variable"""
        idx = self.variables.index(variable)
        return [self.variables[u] for u, v in self.edges if v == idx]
    
    def get_children(self, variable: str) -> List[str]:
        """Get direct effects of a variable"""
        idx = self.variables.index(variable)
        return [self.variables[v] for u, v in self.edges if u == idx]
    
    def markov_blanket(self, variable: str) -> Set[str]:
        """
        Get Markov blanket: parents, children, and parents of children
        """
        idx = self.variables.index(variable)
        blanket = set()
        
        # Parents
        for u, v in self.edges:
            if v == idx:
                blanket.add(self.variables[u])
        
        # Children and their parents
        for u, v in self.edges:
            if u == idx:
                blanket.add(self.variables[v])
                # Parents of children
                for u2, v2 in self.edges:
                    if v2 == v and u2 != idx:
                        blanket.add(self.variables[u2])
        
        blanket.discard(variable)
        return blanket
    
    def to_adjacency_matrix(self) -> np.ndarray:
        """Convert to adjacency matrix"""
        n = len(self.variables)
        A = np.zeros((n, n))
        for u, v in self.edges:
            A[u, v] = 1.0
        return A

def create_default_causal_graph() -> CausalGraph:
    """Create default causal graph for civilizational dynamics"""
    variables = [
        'climate', 'precipitation', 'temperature',
        'agricultural_yield', 'population', 'resource_availability',
        'technological_complexity', 'economic_integration',
        'sociopolitical_stability', 'knowledge_level', 'trade_volume',
        'conflict_intensity', 'collapse_event'
    ]
    
    graph = CausalGraph(variables=variables)
    
    # Environmental causes
    graph.add_edge('climate', 'precipitation')
    graph.add_edge('climate', 'temperature')
    graph.add_edge('precipitation', 'agricultural_yield')
    graph.add_edge('temperature', 'agricultural_yield')
    
    # Economic/demographic causes
    graph.add_edge('agricultural_yield', 'population')
    graph.add_edge('agricultural_yield', 'resource_availability')
    graph.add_edge('population', 'resource_availability')
    graph.add_edge('resource_availability', 'economic_integration')
    graph.add_edge('resource_availability', 'sociopolitical_stability')
    
    # Technology and knowledge
    graph.add_edge('knowledge_level', 'technological_complexity')
    graph.add_edge('technological_complexity', 'economic_integration')
    graph.add_edge('technological_complexity', 'agricultural_yield')
    
    # Social dynamics
    graph.add_edge('economic_integration', 'sociopolitical_stability')
    graph.add_edge('sociopolitical_stability', 'conflict_intensity')
    graph.add_edge('trade_volume', 'economic_integration')
    graph.add_edge('conflict_intensity', 'sociopolitical_stability')
    
    # Collapse
    graph.add_edge('sociopolitical_stability', 'collapse_event')
    graph.add_edge('resource_availability', 'collapse_event')
    graph.add_edge('conflict_intensity', 'collapse_event')
    
    return graph
