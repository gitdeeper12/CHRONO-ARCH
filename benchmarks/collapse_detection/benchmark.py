"""Benchmark for collapse detection accuracy"""

import sys
sys.path.append('../..')

import numpy as np
from chrono_arch import StateVector, SimulationEngine, SimulationConfig, EnvironmentalField

def run_collapse_detection_benchmark(n_runs: int = 10) -> dict:
    """Benchmark collapse detection against known cases"""
    
    results = {
        'detection_rate': [],
        'false_positive_rate': [],
        'lead_time': []
    }
    
    for run in range(n_runs):
        config = SimulationConfig(
            dt=1.0,
            n_civilizations=3,
            n_dimensions=6,
            collapse_threshold=0.35,
            use_stochastic=True,
            random_seed=run
        )
        
        engine = SimulationEngine(config)
        C0 = StateVector(
            environmental_adaptation=0.6,
            resource_availability=[1.0, 1.0, 1.0],
            technological_complexity=0.5,
            sociopolitical_stability=0.5,
            demographic_pressure=0.5,
            economic_integration=0.4
        )
        E0 = EnvironmentalField(climate=0.0, temperature=0.0, precipitation=0.0)
        
        result = engine.simulate(C0, E0, T=300.0)
        
        # Detection metrics
        if result.collapse_events:
            results['detection_rate'].append(1.0)
            first_collapse = result.collapse_events[0]['time']
            # Check if early warning preceded collapse
            if len(result.early_warnings['variance']) > 0:
                results['lead_time'].append(first_collapse - len(result.early_warnings['variance']))
        else:
            results['detection_rate'].append(0.0)
        
        # False positive rate
        n_stable = sum(1 for s in result.stabilities if s > config.collapse_threshold)
        n_collapse_pred = len(result.collapse_events)
        fp_rate = n_collapse_pred / max(1, n_stable)
        results['false_positive_rate'].append(fp_rate)
    
    return {
        'detection_accuracy': np.mean(results['detection_rate']),
        'false_positive_rate': np.mean(results['false_positive_rate']),
        'avg_lead_time': np.mean(results['lead_time']) if results['lead_time'] else 0
    }

if __name__ == '__main__':
    results = run_collapse_detection_benchmark(5)
    print(f"Detection Accuracy: {results['detection_accuracy']:.2%}")
    print(f"False Positive Rate: {results['false_positive_rate']:.2%}")
    print(f"Avg Lead Time: {results['avg_lead_time']:.1f} years")
