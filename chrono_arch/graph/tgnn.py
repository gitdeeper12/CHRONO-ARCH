"""Temporal Graph Neural Network (TGNN)"""

import numpy as np
from typing import Optional
from dataclasses import dataclass

@dataclass
class TGNNConfig:
    hidden_dim: int = 32
    output_dim: int = 32
    n_layers: int = 2
    dropout: float = 0.1
    activation: str = "relu"

class TemporalGNN:
    def __init__(self, input_dim: int, config: Optional[TGNNConfig] = None):
        self.input_dim = input_dim
        self.config = config or TGNNConfig()
        self._initialize_weights()
    
    def _initialize_weights(self):
        self.W_self = np.random.randn(self.input_dim, self.config.hidden_dim) * 0.01
        self.W_nb = np.random.randn(self.input_dim, self.config.hidden_dim) * 0.01
        self.W_out = np.random.randn(self.config.hidden_dim, self.config.output_dim) * 0.01
        self.b = np.zeros(self.config.hidden_dim)
        self.b_out = np.zeros(self.config.output_dim)
    
    def _activation(self, x: np.ndarray) -> np.ndarray:
        if self.config.activation == "relu":
            return np.maximum(0, x)
        elif self.config.activation == "tanh":
            return np.tanh(x)
        return x
    
    def forward(self, H: np.ndarray, A: np.ndarray, training: bool = True) -> np.ndarray:
        h = H
        for _ in range(self.config.n_layers):
            self_term = h @ self.W_self
            neighbor_term = A @ (h @ self.W_nb)
            combined = self_term + neighbor_term + self.b
            h = self._activation(combined)
        return h @ self.W_out + self.b_out
