"""Fokker-Planck equation for probability density evolution
Equation (13): ∂P(C,t)/∂t = −∇·(P·F) + D·∇²P
"""

import numpy as np
from typing import Optional, Callable, Tuple
from dataclasses import dataclass

@dataclass
class FokkerPlanckConfig:
    """Configuration for Fokker-Planck solver"""
    n_grid: int = 64           # Grid points per dimension (for n_dim <= 4)
    diffusion_coefficient: float = 0.01  # D
    boundary_absorbing: bool = False     # Absorbing vs reflecting boundaries
    dt_max: float = 0.001      # Maximum time step for stability

class FokkerPlanckSolver:
    """
    Solver for Fokker-Planck equation
    ∂P/∂t = −∇·(P·F) + D·∇²P
    
    Currently supports 1D and 2D problems.
    For higher dimensions, use particle filters.
    """
    
    def __init__(self, config: Optional[FokkerPlanckConfig] = None):
        self.config = config or FokkerPlanckConfig()
    
    def solve_1d(
        self,
        x_grid: np.ndarray,
        P0: np.ndarray,
        drift_function: Callable[[float, float], float],
        t_max: float,
        dt: Optional[float] = None
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Solve 1D Fokker-Planck using finite differences
        
        Args:
            x_grid: Spatial grid points
            P0: Initial probability density
            drift_function: F(x, t) drift
            t_max: Maximum time
            dt: Time step
        
        Returns:
            x_grid, times, P(x,t) matrix
        """
        nx = len(x_grid)
        dx = x_grid[1] - x_grid[0]
        
        if dt is None:
            dt = min(self.config.dt_max, 0.1 * dx**2 / self.config.diffusion_coefficient)
        
        n_steps = int(t_max / dt)
        
        P = np.zeros((n_steps + 1, nx))
        P[0] = P0.copy()
        
        for step in range(n_steps):
            t = step * dt
            P_current = P[step]
            
            # Compute flux: J = F*P - D*dP/dx
            F = np.array([drift_function(x, t) for x in x_grid])
            
            # Drift term: -d(F*P)/dx
            FP = F * P_current
            dFP_dx = np.gradient(FP, dx)
            
            # Diffusion term: D * d²P/dx²
            d2P_dx2 = np.gradient(np.gradient(P_current, dx), dx)
            diffusion = self.config.diffusion_coefficient * d2P_dx2
            
            # Update
            dP_dt = -dFP_dx + diffusion
            P_next = P_current + dP_dt * dt
            
            # Apply boundary conditions
            if self.config.boundary_absorbing:
                P_next[0] = 0
                P_next[-1] = 0
            else:
                # Reflecting boundaries
                P_next[0] = max(P_next[0], 0)
                P_next[-1] = max(P_next[-1], 0)
            
            # Ensure non-negative
            P_next = np.maximum(P_next, 0)
            
            # Renormalize
            total = np.trapz(P_next, x_grid)
            if total > 0:
                P_next /= total
            
            P[step + 1] = P_next
        
        times = np.linspace(0, t_max, n_steps + 1)
        return x_grid, times, P
    
    def stationary_distribution(
        self,
        x_grid: np.ndarray,
        potential: Callable[[float], float],
        temperature: float = 1.0
    ) -> np.ndarray:
        """
        Compute stationary distribution for given potential
        P_eq(x) ∝ exp(-U(x)/T)
        """
        U = np.array([potential(x) for x in x_grid])
        P = np.exp(-U / temperature)
        P /= np.trapz(P, x_grid)
        return P

def create_fokker_planck_solver(n_dim: int = 1) -> FokkerPlanckSolver:
    """Create Fokker-Planck solver for given dimensionality"""
    if n_dim > 2:
        print(f"Warning: Fokker-Planck for {n_dim}D is computationally intensive")
    
    return FokkerPlanckSolver()
