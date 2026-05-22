"""Layer III: Model and Inference
Temporal GNN, SDE simulator, Fokker-Planck solver, causal graph learner
"""

import sys
sys.path.append('../..')

import numpy as np
from typing import Optional, Dict, Any

class ModelInterface:
    """Unified interface for CHRONO-ARCH models"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self._initialize_models()
    
    def _initialize_models(self):
        """Initialize sub-models"""
        from chrono_arch.graph.tgnn import TemporalGNN, TGNNConfig
        from chrono_arch.probabilistic.sde import SDESimulator, SDEParameters
        from chrono_arch.probabilistic.fokker_planck import FokkerPlanckSolver
        
        self.tgnn = TemporalGNN(
            input_dim=self.config.get('input_dim', 6),
            config=TGNNConfig(
                hidden_dim=self.config.get('hidden_dim', 32),
                output_dim=self.config.get('output_dim', 6)
            )
        )
        
        self.sde_sim = SDESimulator(
            SDEParameters(diffusion_coefficient=self.config.get('diffusion', 0.1))
        )
        
        self.fp_solver = FokkerPlanckSolver()
    
    def predict_state(self, C: np.ndarray, A: np.ndarray) -> np.ndarray:
        """Predict next state using TGNN"""
        return self.tgnn.forward(C, A, training=False)
    
    def simulate_sde(self, C0: np.ndarray, drift_fn, dt: float, n_steps: int):
        """Simulate SDE trajectory"""
        return self.sde_sim.simulate_trajectory(C0, drift_fn, dt, n_steps)
    
    def get_model_info(self) -> Dict[str, Any]:
        return {
            'tgnn_ready': hasattr(self, 'tgnn'),
            'sde_ready': hasattr(self, 'sde_sim'),
            'fp_ready': hasattr(self, 'fp_solver')
        }
