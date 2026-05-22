import sys
import unittest
sys.path.append('../..')

from chrono_arch.collapse.early_warning import compute_variance_ews, compute_autocorrelation_ews, collapse_alert

class TestEarlyWarning(unittest.TestCase):
    
    def setUp(self):
        self.trajectory = [0.8 - i * 0.008 + 0.05 * (i % 10) / 10 for i in range(100)]
    
    def test_variance_ews(self):
        variance = compute_variance_ews(self.trajectory, window=20)
        self.assertEqual(len(variance), len(self.trajectory))
    
    def test_autocorrelation_ews(self):
        ac = compute_autocorrelation_ews(self.trajectory, lag=1, window=20)
        self.assertEqual(len(ac), len(self.trajectory))
    
    def test_collapse_alert(self):
        ews = {
            'variance': [0.1, 0.12, 0.15, 0.2, 0.3, 0.5, 0.8, 1.2],
            'autocorrelation_lag1': [0.2, 0.25, 0.3, 0.4, 0.6, 0.7, 0.8, 0.85],
            'critical_slowing_down': [0.05, 0.06, 0.08, 0.12, 0.2, 0.35, 0.6, 0.9]
        }
        alert, confidence = collapse_alert(ews, threshold_factor=1.5)
        self.assertIsInstance(alert, bool)

if __name__ == '__main__':
    unittest.main()
