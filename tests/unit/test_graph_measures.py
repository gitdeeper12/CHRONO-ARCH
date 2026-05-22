import sys
import unittest
sys.path.append('../..')

import numpy as np
from chrono_arch.graph.graph_measures import degree_centrality, clustering_coefficient, average_path_length, compute_all_measures

class TestGraphMeasures(unittest.TestCase):
    
    def setUp(self):
        self.A = np.array([
            [0.0, 0.8, 0.0],
            [0.8, 0.0, 0.6],
            [0.0, 0.6, 0.0]
        ])
        self.A_complete = np.array([
            [0.0, 1.0, 1.0],
            [1.0, 0.0, 1.0],
            [1.0, 1.0, 0.0]
        ])
    
    def test_degree_centrality(self):
        degrees = degree_centrality(self.A)
        self.assertEqual(degrees[0], 0.8)
        self.assertEqual(degrees[1], 1.4)
    
    def test_clustering_coefficient(self):
        clust = clustering_coefficient(self.A_complete)
        for c in clust:
            self.assertEqual(c, 1.0)
    
    def test_compute_all_measures(self):
        measures = compute_all_measures(self.A)
        self.assertIn('degree_centrality', measures)
        self.assertIn('clustering_coefficient', measures)

if __name__ == '__main__':
    unittest.main()
