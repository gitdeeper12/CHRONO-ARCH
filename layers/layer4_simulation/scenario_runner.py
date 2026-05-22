"""Layer IV: Simulation and Scenario Analysis
Agent-based modeling, counterfactual scenario generation, collapse risk assessment
"""

import sys
sys.path.append('../..')

import numpy as np
from typing import List, Dict, Any, Optional

class ScenarioRunner:
    """Layer IV: Simulation and scenario analysis"""
    
    def __init__(self, engine=None):
        from chrono_arch.simulation.engine import SimulationEngine
        self.engine = engine or SimulationEngine()
        self.scenarios = []
    
    def create_counterfactual(self, interventions: Dict[str, float]) -> Dict[str, Any]:
        """Create counterfactual scenario with interventions"""
        scenario = {
            'type': 'counterfactual',
            'interventions': interventions,
            'description': f"Modified: {interventions}"
        }
        self.scenarios.append(scenario)
        return scenario
    
    def create_climate_scenario(self, temperature_anomaly: float, 
                                  precipitation_anomaly: float) -> Dict[str, Any]:
        """Create climate change scenario"""
        return self.create_counterfactual({
            'temperature': temperature_anomaly,
            'precipitation': precipitation_anomaly
        })
    
    def run_scenario(self, scenario: Dict[str, Any], 
                     C0, E0, T: float = 500.0):
        """Run a specific scenario"""
        # Apply interventions to environment
        if 'interventions' in scenario:
            for var, value in scenario['interventions'].items():
                if hasattr(E0, var):
                    setattr(E0, var, value)
        
        return self.engine.simulate(C0, E0, T)
    
    def ensemble_run(self, C0, E0, T: float, n_ensemble: int = 10) -> List:
        """Run ensemble of simulations"""
        results = []
        for i in range(n_ensemble):
            self.engine.config.random_seed = i
            result = self.engine.simulate(C0, E0, T)
            results.append(result)
        return results
    
    def risk_assessment(self, results: List) -> Dict[str, float]:
        """Assess collapse risk from ensemble results"""
        collapse_count = sum(1 for r in results if r.collapse_events)
        collapse_probability = collapse_count / len(results)
        
        avg_stability = np.mean([r.stabilities[-1] for r in results if r.stabilities])
        
        return {
            'collapse_probability': collapse_probability,
            'avg_final_stability': avg_stability,
            'ensemble_size': len(results)
        }
