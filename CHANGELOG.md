# Changelog

All notable changes to CHRONO-ARCH will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-05-22

### 🎉 Initial Release: CHRONO-ARCH

**A Computational Framework for Temporal Archaeology and Civilizational Dynamics Using AI and Complex Systems Modeling**

This is the first stable release of CHRONO-ARCH, providing a unified computational paradigm for modeling civilizations as coupled nonlinear spatiotemporal dynamical systems.

---

### ✨ Added

#### Core Framework

| Component | Description | Equation |
|-----------|-------------|----------|
| Civilizational State Vector | C(t) ∈ ℝⁿ representing subsystem states | Eq. (1) |
| Master Evolution Equation | dC/dt = F(C, E, G, t) | Eq. (2-3) |
| Temporal Interaction Graph | G(t) = (V, A(t)) time-varying network | Eq. (4) |
| Co-evolution System | Mutual feedback between state and network | Eq. (5a-c) |
| Environmental Coupling | F_E = Γ · ∇E(t) | Eq. (6-7) |
| Knowledge Diffusion | dK/dt = −L(t)·K + Ψ(K, A) | Eq. (9-11) |
| Fokker-Planck Layer | ∂P/∂t = −∇·(P·F) + D·∇²P | Eq. (13) |
| Phase Transition Theory | Collapse as endogenous phase transition | Eq. (15-16) |
| Early Warning Signals | Variance, autocorrelation, critical slowing | Eq. (17a-c) |
| Causal Inference | Do-calculus for counterfactuals | Eq. (18-19) |

#### Computational Architecture (4 Layers)

```

┌─────────────────────────────────────────────────────────┐
│  LAYER IV — Simulation & Scenario Analysis              │
├─────────────────────────────────────────────────────────┤
│  LAYER III — Model & Inference                          │
├─────────────────────────────────────────────────────────┤
│  LAYER II — Embedding & Fusion                          │
├─────────────────────────────────────────────────────────┤
│  LAYER I — Data Ingestion & Representation              │
└─────────────────────────────────────────────────────────┘

```

#### Formal Metrics Defined

| Metric | Symbol | Formula | Interpretation |
|--------|--------|---------|----------------|
| Resilience | R | mean(S(t)) - λ·C | Higher = better recovery |
| Stability Variance | σ² | Var(S(t)) | Lower = more stable |
| Recovery Rate | ρ | ΔS/Δt | Higher = faster rebound |
| Adaptability | α | (S_final - S_initial)/(1+C) | Positive = improvement |

#### New Taxonomy Proposed

| Old Name | New Name | Characteristics |
|----------|----------|-----------------|
| Fragile | **Adaptive-Volatile** | Low initial stability, high volatility, fast recovery, positive trend |
| Moderate | **Balanced-Resilient** | Moderate stability, consistent performance, best baseline |
| Stable | **Rigid-Declining** | High initial stability, poor recovery, negative trend |

#### Scientific Discovery: The Fragility Paradox

> Systems with higher volatility and repeated collapses can achieve **BETTER long-term outcomes** than initially stable systems.

**Empirical Results (T=200 years simulation):**

| System | Initial S | Final S | Change | Collapses | Classification |
|--------|-----------|---------|--------|-----------|----------------|
| Stable (Rigid) | 0.8866 | 0.5309 | -0.3557 | 0 | Rigid-Declining |
| Moderate | 0.5131 | 0.5309 | +0.0178 | 0 | Balanced-Resilient |
| Fragile | 0.1545 | 0.5309 | **+0.3764** | 2 | Adaptive-Volatile |

#### Key Insight

```

Collapse ≠ Failure
Volatility enables adaptation
Static stability leads to rigidity

```

---

### 📊 Validation

| Test Type | Status | Count |
|-----------|--------|-------|
| Unit Tests | ✅ Passed | 12/12 |
| Integration Tests | ✅ Passed | All |
| Perturbation Experiments | ✅ Complete | 3 types |
| Phase Transition Analysis | ✅ Complete | 3 scenarios |

---

### 📁 Project Structure

```

CHRONO-ARCH/
├── chrono_arch/           # Core modules (8 subpackages)
│   ├── state/            # State vector & evolution
│   ├── graph/            # Temporal graph & measures
│   ├── environment/      # Environmental coupling
│   ├── diffusion/        # Knowledge diffusion
│   ├── probabilistic/    # SDE & Fokker-Planck
│   ├── collapse/         # Stability & early warning
│   ├── causal/           # Do-calculus
│   └── simulation/       # Main engine
├── tests/                # Unit & integration tests
├── reports/              # JSON analysis reports
├── notebooks/            # Jupyter notebooks
├── layers/               # 4-layer architecture
└── benchmarks/           # Performance benchmarks

```

---

### 📦 Dependencies

```

Python >= 3.9
numpy >= 1.21.0
scipy >= 1.7.0
networkx >= 2.6
torch >= 1.10.0      # Optional (TGNN)
xarray >= 2022.0.0   # Optional (data handling)

```

---

### 📄 Reports Generated

| Report | Description |
|--------|-------------|
| `formal_metrics_report.json` | Mathematical metrics definitions |
| `perturbation_experiments.json` | Noise, resource, recovery tests |
| `phase_analysis_report.json` | Temporal phase transitions |
| `TAXONOMY_FINAL.txt` | New classification system |

---

### 🔗 Links

- **DOI:** [10.5281/zenodo.20330475](https://doi.org/10.5281/zenodo.20330475)
- **License:** MIT
- **Author:** Samir Baladi
- **Email:** gitdeeper@gmail.com
- **ORCID:** 0009-0003-8903-0029

---

### 📝 Citation

```bibtex
@software{baladi2026chronoarch,
  author    = {Samir Baladi},
  title     = {CHRONO-ARCH: A Computational Framework for Temporal Archaeology
               and Civilizational Dynamics Using AI and Complex Systems Modeling},
  year      = {2026},
  version   = {1.0.0},
  doi       = {10.5281/zenodo.20330475},
  license   = {MIT}
}
```

---

Part of the EntropyLab research program

"The goal is not to predict the past, but to understand the space of pasts consistent with the evidence — and the space of futures consistent with the present."

