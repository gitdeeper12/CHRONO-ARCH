"""Causal effect estimation via do-calculus
Equation (19): P(C | do(X=x)) = ∫ P(C | X=x, Z=z)·P(Z=z) dz
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Callable
from scipy.stats import gaussian_kde
from .causal_graph import CausalGraph

class DoCalculus:
    """
    Implementation of do-calculus for causal inference
    Enables counterfactual analysis of historical scenarios
    """
    
    def __init__(self, causal_graph: CausalGraph):
        self.graph = causal_graph
    
    def adjustment_set(self, treatment: str, outcome: str) -> List[str]:
        """
        Find adjustment set Z for causal effect identification
        P(C | do(X=x)) = ∫ P(C | X=x, Z=z)·P(Z=z) dz
        """
        # Simplified: use parents of outcome minus descendants of treatment
        outcome_parents = self.graph.get_parents(outcome)
        treatment_descendants = self._get_descendants(treatment)
        
        adjustment = [v for v in outcome_parents if v not in treatment_descendants]
        return adjustment
    
    def _get_descendants(self, node: str) -> List[str]:
        """Get all descendants of a node"""
        idx = self.graph.variables.index(node)
        adj = self.graph.to_adjacency_matrix()
        
        descendants = set()
        stack = [idx]
        
        while stack:
            current = stack.pop()
            for j in range(len(self.graph.variables)):
                if adj[current, j] > 0 and j not in descendants:
                    descendants.add(j)
                    stack.append(j)
        
        return [self.graph.variables[i] for i in descendants]
    
    def estimate_causal_effect(
        self,
        data: np.ndarray,
        variable_names: List[str],
        treatment: str,
        outcome: str,
        treatment_value: float,
        background_data: Optional[np.ndarray] = None
    ) -> float:
        """
        Estimate causal effect using adjustment formula
        
        Args:
            data: Observed data matrix (samples × variables)
            variable_names: Names of variables in data
            treatment: Name of treatment variable
            outcome: Name of outcome variable
            treatment_value: Value to intervene on
            background_data: Additional background data
        
        Returns:
            Estimated causal effect E[C | do(X=x)]
        """
        treatment_idx = variable_names.index(treatment)
        outcome_idx = variable_names.index(outcome)
        
        # Find adjustment set
        adj_set = self.adjustment_set(treatment, outcome)
        adj_indices = [variable_names.index(v) for v in adj_set if v in variable_names]
        
        if not adj_indices:
            # No adjustment needed - simple conditional expectation
            treated_data = data[data[:, treatment_idx] == treatment_value]
            if len(treated_data) > 0:
                return np.mean(treated_data[:, outcome_idx])
            else:
                # Interpolation
                return self._interpolate_effect(data, treatment_idx, outcome_idx, treatment_value)
        
        # Adjust by conditioning on Z
        # P(Y|do(X=x)) = Σ_z P(Y|X=x, Z=z) P(Z=z)
        
        # Discretize Z if continuous
        z_values = data[:, adj_indices]
        
        # Use kernel density for continuous Z
        effect = 0
        total_weight = 0
        
        for i in range(len(data)):
            z = z_values[i]
            weight = self._compute_weight(z, z_values)
            
            # Find samples with same treatment and similar Z
            mask = (np.abs(data[:, treatment_idx] - treatment_value) < 0.1)
            if np.any(mask):
                similar = data[mask]
                if len(similar) > 0:
                    # Weight by similarity in Z
                    z_distances = np.linalg.norm(similar[:, adj_indices] - z, axis=1)
                    z_weights = np.exp(-z_distances / np.std(z_distances)) if np.std(z_distances) > 0 else np.ones(len(similar))
                    conditional_mean = np.average(similar[:, outcome_idx], weights=z_weights)
                    
                    effect += conditional_mean * weight
                    total_weight += weight
        
        return effect / total_weight if total_weight > 0 else 0
    
    def _compute_weight(self, z: np.ndarray, all_z: np.ndarray) -> float:
        """Compute weight P(Z=z)"""
        # Use Gaussian kernel density estimation
        try:
            kde = gaussian_kde(all_z.T)
            return kde.pdf(z)[0]
        except:
            return 1.0 / len(all_z)
    
    def _interpolate_effect(self, data: np.ndarray, tx_idx: int, out_idx: int, tx_value: float) -> float:
        """Interpolate causal effect for unseen treatment values"""
        unique_tx = np.unique(data[:, tx_idx])
        unique_effects = []
        
        for tx in unique_tx:
            mask = data[:, tx_idx] == tx
            if np.any(mask):
                unique_effects.append(np.mean(data[mask, out_idx]))
        
        if len(unique_tx) < 2:
            return np.mean(unique_effects) if unique_effects else 0
        
        # Linear interpolation
        return np.interp(tx_value, unique_tx, unique_effects)

class DoCalculusSimple:
    """Simplified do-calculus for quick estimation"""
    
    def __init__(self):
        self.data = None
        self.variable_names = None
    
    def fit(self, data: np.ndarray, variable_names: List[str]):
        """Fit with observed data"""
        self.data = data
        self.variable_names = variable_names
    
    def intervene(self, treatment: str, value: float, outcome: str) -> float:
        """Estimate P(outcome | do(treatment=value))"""
        tx_idx = self.variable_names.index(treatment)
        out_idx = self.variable_names.index(outcome)
        
        # Find matching samples
        mask = np.abs(self.data[:, tx_idx] - value) < 0.1
        
        if np.any(mask):
            return np.mean(self.data[mask, out_idx])
        else:
            # Linear regression for extrapolation
            unique_tx = np.unique(self.data[:, tx_idx])
            unique_means = [np.mean(self.data[self.data[:, tx_idx] == tx, out_idx]) for tx in unique_tx]
            
            if len(unique_tx) > 1:
                slope, intercept = np.polyfit(unique_tx, unique_means, 1)
                return slope * value + intercept
            
            return np.mean(self.data[:, out_idx])
