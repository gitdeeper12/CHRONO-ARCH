"""Graph-theoretic measures for civilizational analysis"""

import numpy as np
from typing import Dict, Any

def degree_centrality(A: np.ndarray) -> np.ndarray:
    """Degree centrality: k_i(t) = Σ_j A_ij(t)"""
    return np.sum(A, axis=1)

def degree_centrality_normalized(A: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    if n <= 1:
        return np.zeros(n)
    return np.sum(A, axis=1) / (n - 1)

def clustering_coefficient(A: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    clustering = np.zeros(n)
    for i in range(n):
        neighbors = np.where(A[i] > 0)[0]
        k = len(neighbors)
        if k < 2:
            continue
        triangles = 0
        for j in range(k):
            for l in range(j+1, k):
                if A[neighbors[j], neighbors[l]] > 0:
                    triangles += 1
        max_triangles = k * (k - 1) / 2
        clustering[i] = triangles / max_triangles if max_triangles > 0 else 0
    return clustering

def fiedler_eigenvalue(A: np.ndarray) -> float:
    """Approximate Fiedler eigenvalue (second smallest eigenvalue of Laplacian)"""
    D = np.diag(np.sum(A, axis=1))
    L = D - A
    eigenvalues = np.linalg.eigvalsh(L)
    eigenvalues_sorted = np.sort(eigenvalues)
    return eigenvalues_sorted[1] if len(eigenvalues_sorted) > 1 else eigenvalues_sorted[0]

def spectral_radius(A: np.ndarray) -> float:
    eigenvalues = np.linalg.eigvals(A)
    return np.max(np.abs(eigenvalues))

def average_path_length(A: np.ndarray) -> float:
    n = A.shape[0]
    INF = 1e9
    dist = np.full((n, n), INF)
    for i in range(n):
        dist[i, i] = 0
        for j in range(n):
            if A[i, j] > 0:
                dist[i, j] = 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
    total = 0
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and dist[i, j] < INF:
                total += dist[i, j]
                count += 1
    return total / count if count > 0 else 0

def compute_all_measures(A: np.ndarray) -> Dict[str, Any]:
    return {
        'degree_centrality': degree_centrality(A),
        'degree_centrality_normalized': degree_centrality_normalized(A),
        'clustering_coefficient': clustering_coefficient(A),
        'fiedler_eigenvalue': fiedler_eigenvalue(A),
        'spectral_radius': spectral_radius(A),
        'average_path_length': average_path_length(A)
    }
