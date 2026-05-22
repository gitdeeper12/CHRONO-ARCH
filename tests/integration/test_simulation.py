import sys
import unittest
sys.path.append('../..')

from chrono_arch import StateVector, SimulationEngine, SimulationConfig, EnvironmentalField

class TestSimulation(unittest.TestCase):
    
    def setUp(self):
        self.config = SimulationConfig(
            dt=1.0, n_civilizations=1, n_dimensions=6,
            collapse_threshold=0.35, use_stochastic=False, random_seed=42
        )
        self.engine = SimulationEngine(self.config)
        self.C0 = StateVector(
            environmental_adaptation=0.7, resource_availability=[1.0, 1.0, 1.0],
            technological_complexity=0.5, sociopolitical_stability=0.6,
            demographic_pressure=0.4, economic_integration=0.3
        )
        self.E0 = EnvironmentalField(climate=0.0, temperature=0.0, precipitation=0.0)
    
    def test_simulation_runs(self):
        result = self.engine.simulate(self.C0, self.E0, T=50.0)
        self.assertGreater(len(result.times), 0)
        self.assertEqual(len(result.states), len(result.times))
    
    def test_stability_tracking(self):
        result = self.engine.simulate(self.C0, self.E0, T=50.0)
        for s in result.stabilities:
            self.assertGreaterEqual(s, 0)
            self.assertLessEqual(s, 1)

if __name__ == '__main__':
    unittest.main()
