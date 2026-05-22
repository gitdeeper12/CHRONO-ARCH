import sys
import unittest
sys.path.append('../..')

import numpy as np
from chrono_arch.state.state_vector import StateVector

class TestStateVector(unittest.TestCase):
    
    def test_creation(self):
        sv = StateVector(
            environmental_adaptation=0.7,
            resource_availability=[1.2, 0.8, 1.5],
            technological_complexity=0.45,
            sociopolitical_stability=0.6,
            demographic_pressure=0.4,
            economic_integration=0.55
        )
        self.assertEqual(sv.environmental_adaptation, 0.7)
    
    def test_to_array(self):
        sv = StateVector(
            environmental_adaptation=0.7,
            resource_availability=[1.0, 2.0],
            technological_complexity=0.5,
            sociopolitical_stability=0.6,
            demographic_pressure=0.4,
            economic_integration=0.3
        )
        arr = sv.to_array()
        self.assertIsInstance(arr, np.ndarray)
        self.assertEqual(arr[0], 0.7)
    
    def test_roundtrip(self):
        original = StateVector(
            environmental_adaptation=0.7,
            resource_availability=[1.0, 2.0, 1.5],
            technological_complexity=0.5,
            sociopolitical_stability=0.6,
            demographic_pressure=0.4,
            economic_integration=0.3
        )
        arr = original.to_array()
        reconstructed = StateVector.from_array(arr, n_resources=3)
        self.assertEqual(reconstructed.environmental_adaptation, original.environmental_adaptation)
    
    def test_validation(self):
        with self.assertRaises(ValueError):
            StateVector(environmental_adaptation=1.5)
        with self.assertRaises(ValueError):
            StateVector(sociopolitical_stability=-0.1)

if __name__ == '__main__':
    unittest.main()
