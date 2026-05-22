"""Counterfactual analysis for historical what-if questions
E[C_t | do(X=x), C_{1:t-1} = c]
"""

import numpy as np
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass
from .do_calculus import DoCalculusSimple

@dataclass
class CounterfactualResult:
    """Result of a counterfactual query"""
    original_outcome: float
    counterfactual_outcome: float
    effect: float
    confidence: float
    details: Dict[str, Any]

class CounterfactualAnalyzer:
    """
    Counterfactual analysis for civilizational dynamics
    Answers: "What would have happened if X had been different?"
    """
    
    def __init__(self):
        self.do_calc = DoCalculusSimple()
        self.history = None
    
    def fit(self, historical_data: np.ndarray, variable_names: List[str]):
        """Fit with historical data"""
        self.do_calc.fit(historical_data, variable_names)
        self.history = historical_data
        self.variable_names = variable_names
    
    def query(self, intervention: str, original_value: float, 
              counterfactual_value: float, outcome: str) -> CounterfactualResult:
        """
        Run counterfactual query
        
        Args:
            intervention: Variable to intervene on
            original_value: What actually happened
            counterfactual_value: What if it had been this value?
            outcome: Outcome variable of interest
        
        Returns:
            CounterfactualResult with effect estimate
        """
        # Estimate original outcome (observed)
        out_idx = self.variable_names.index(outcome)
        original_outcome = np.mean(self.history[:, out_idx])
        
        # Estimate counterfactual outcome
        cf_outcome = self.do_calc.intervene(intervention, counterfactual_value, outcome)
        
        # Compute effect
        effect = cf_outcome - original_outcome
        
        # Confidence (based on data support)
        tx_idx = self.variable_names.index(intervention)
        unique_tx = np.unique(self.history[:, tx_idx])
        support = 1.0 - min(1.0, abs(counterfactual_value - np.mean(unique_tx)) / np.std(unique_tx)) if np.std(unique_tx) > 0 else 0.5
        confidence = max(0.1, min(0.95, support))
        
        return CounterfactualResult(
            original_outcome=original_outcome,
            counterfactual_outcome=cf_outcome,
            effect=effect,
            confidence=confidence,
            details={
                'intervention': intervention,
                'original_value': original_value,
                'counterfactual_value': counterfactual_value,
                'outcome': outcome
            }
        )
    
    def climate_counterfactual(self, precipitation_change: float, 
                                outcome: str = 'sociopolitical_stability') -> CounterfactualResult:
        """Specific counterfactual: What if precipitation had been different?"""
        # Get historical precipitation average
        prec_idx = self.variable_names.index('precipitation') if 'precipitation' in self.variable_names else 0
        original_prec = np.mean(self.history[:, prec_idx])
        
        return self.query('precipitation', original_prec, 
                         original_prec + precipitation_change, outcome)
    
    def technological_counterfactual(self, tech_boost: float,
                                      outcome: str = 'economic_integration') -> CounterfactualResult:
        """What if technological development had been faster?"""
        tech_idx = self.variable_names.index('technological_complexity') if 'technological_complexity' in self.variable_names else 2
        original_tech = np.mean(self.history[:, tech_idx])
        
        return self.query('technological_complexity', original_tech,
                         min(1.0, original_tech + tech_boost), outcome)

def create_counterfactual_analyzer_from_csv(data_path: str) -> CounterfactualAnalyzer:
    """Create analyzer from CSV data"""
    import pandas as pd
    df = pd.read_csv(data_path)
    
    variable_names = list(df.columns)
    data = df.values
    
    analyzer = CounterfactualAnalyzer()
    analyzer.fit(data, variable_names)
    
    return analyzer
