# CHRONO-ARCH

> **A Computational Framework for Temporal Archaeology and Civilizational Dynamics Using AI and Complex Systems Modeling**

<div align="center">

| Badge | Status |
|-------|--------|
| Version | ![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square) |
| License | ![License](https://img.shields.io/badge/license-MIT-green?style=flat-square) |
| Status | ![Status](https://img.shields.io/badge/status-stable-brightgreen?style=flat-square) |
| Python | ![Python](https://img.shields.io/badge/python-3.9%2B-yellow?style=flat-square) |
| PyPI | ![PyPI](https://img.shields.io/badge/PyPI-chrono--arch-orange?style=flat-square) |
| DOI | ![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20330475-blue?style=flat-square) |
| OSF | ![OSF](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2F2BWZD-purple?style=flat-square) |
| Website | [![Website](https://img.shields.io/badge/Website-chronoarch.netlify.app-4a7fa5?style=flat-square)](https://chronoarch.netlify.app) |

</div>

---

## Table of Contents

1. [Overview](#1-overview)
2. [Abstract](#2-abstract)
3. [OSF Preregistration](#3-osf-preregistration)
4. [Official Website](#4-official-website)
5. [Core Formalism](#5-core-formalism)
   - [Civilizational State Vector](#51-civilizational-state-vector)
   - [Master Evolution Equation](#52-master-evolution-equation)
   - [Temporal Interaction Graph](#53-temporal-interaction-graph)
   - [Environmental Coupling](#54-environmental-coupling)
   - [Knowledge Diffusion](#55-knowledge-diffusion)
   - [Fokker-Planck Probabilistic Layer](#56-fokker-planck-probabilistic-layer)
   - [Collapse and Phase Transition Theory](#57-collapse-and-phase-transition-theory)
   - [Causal Inference Framework](#58-causal-inference-framework)
6. [Computational Architecture](#6-computational-architecture)
7. [Simulation Algorithm](#7-simulation-algorithm)
8. [Variable Index](#8-variable-index)
9. [Project Structure](#9-project-structure)
10. [Installation](#10-installation)
11. [Quick Start](#11-quick-start)
12. [Applications](#12-applications)
13. [Limitations and Assumptions](#13-limitations-and-assumptions)
14. [Distribution Platforms](#14-distribution-platforms)
15. [Citation](#15-citation)
16. [Author](#16-author)
17. [License](#17-license)

---

## 1. Overview

CHRONO-ARCH treats civilizations as **coupled nonlinear spatiotemporal dynamical systems** embedded in evolving environmental and interaction fields. Rather than producing static reconstructions of the past, it formulates civilizational evolution as a set of computable, probabilistic, and graph-theoretic mathematical structures that enable:

- **Simulation** of long-term civilizational trajectories under varied conditions
- **Inference** of hidden historical structures from fragmentary archaeological evidence
- **Collapse modeling** as endogenous phase transitions with early-warning signal diagnostics
- **Counterfactual analysis** of historical what-if questions via formal do-calculus

The framework is simultaneously a theoretical specification, a computational architecture, and an open-source Python implementation.

> *"The goal is not to predict the past, but to understand the space of pasts consistent with the evidence — and the space of futures consistent with the present."*

---

## 2. Abstract

CHRONO-ARCH introduces a computational framework for modeling civilizations as nonlinear, temporally evolving dynamical systems embedded in environmental, economic, and networked interaction fields. Unlike traditional archaeological approaches that rely on static reconstruction, the framework formulates civilizations as coupled spatiotemporal systems governed by **differential dynamics**, **probabilistic state transitions**, and **evolving interaction graphs**.

The core system is expressed as a nonlinear operator-valued ordinary differential equation over a time-dependent graph, augmented with a **Fokker-Planck probabilistic layer** and a **causal inference module**. All components are formally specified, computationally interpretable, and grounded in measurable variables.

**Keywords:** Civilizational Dynamics · Temporal Graph Networks · Dynamical Systems · Complex Systems · Causal Inference · Probabilistic Modeling · Environmental Coupling · Collapse Theory · Archaeological AI · Phase Transitions · Knowledge Diffusion · Fokker-Planck Equation

---

## 3. OSF Preregistration

This project has been formally preregistered on the Open Science Framework (OSF).

| Field | Value |
|-------|-------|
| **Registration Type** | OSF Preregistration |
| **Registry** | OSF Registries |
| **Associated Project** | [https://osf.io/bfd8g](https://osf.io/bfd8g) |
| **Date Created** | May 22, 2026, 6:12 AM |
| **Date Registered** | May 22, 2026, 6:12 AM |
| **License** | MIT License |
| **Internet Archive** | [archive.org/details/osf-registrations-2bwzd-v1](https://archive.org/details/osf-registrations-2bwzd-v1) |
| **Registration DOI** | [10.17605/OSF.IO/2BWZD](https://doi.org/10.17605/OSF.IO/2BWZD) |

<div align="center">
  <a href="https://doi.org/10.17605/OSF.IO/2BWZD">
    <img src="https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2F2BWZD-purple?style=for-the-badge" alt="OSF Registration">
  </a>
</div>

---

## 4. Official Website

The CHRONO-ARCH framework has an official documentation website with live dashboard, results, and full documentation.

| Page | URL |
|------|-----|
| 🏠 Home | [https://chronoarch.netlify.app](https://chronoarch.netlify.app) |
| ⚙️ Dashboard | [https://chronoarch.netlify.app/dashboard](https://chronoarch.netlify.app/dashboard) |
| 📊 Results | [https://chronoarch.netlify.app/results](https://chronoarch.netlify.app/results) |
| 🐝 Documentation | [https://chronoarch.netlify.app/documentation](https://chronoarch.netlify.app/documentation) |
| 📋 OSF Registration | [https://chronoarch.netlify.app/registration](https://chronoarch.netlify.app/registration) |

<div align="center">
  <a href="https://chronoarch.netlify.app">
    <img src="https://img.shields.io/badge/Website-chronoarch.netlify.app-4a7fa5?style=for-the-badge" alt="Official Website">
  </a>
</div>

---

## 5. Core Formalism

### 5.1 Civilizational State Vector

A civilization at time `t` is represented as a real-valued state vector:

```

C(t) ∈ ℝⁿ

```

| Component | Domain     | Description                           |
|-----------|------------|---------------------------------------|
| `C₁(t)`   | `[0, 1]`   | Environmental adaptation index        |
| `C₂(t)`   | `ℝ₊ᵐ`      | Resource availability (vector)        |
| `C₃(t)`   | `ℝ₊`       | Technological complexity scalar       |
| `C₄(t)`   | `[0, 1]`   | Sociopolitical stability index        |
| `C₅(t)`   | `ℝ₊`       | Demographic pressure                  |
| `C₆(t)`   | `ℝ`        | Economic integration measure          |
| `Cₙ(t)`   | —          | n-th subsystem state variable         |

---

### 5.2 Master Evolution Equation

The fundamental dynamics of the state vector:

```

dC(t)/dt = F( C(t), E(t), G(t), t )                  (Eq. 2)

```

Nonlinear expansion:

```

dC/dt = A·C + Cᵀ·B·C + G(E, G_graph)                  (Eq. 3)

```

| Term         | Symbol    | Description                                    |
|--------------|-----------|------------------------------------------------|
| Linear       | `A·C`     | Linear growth or decay (stability matrix)      |
| Quadratic    | `Cᵀ·B·C`  | Nonlinear interaction amplification            |
| Coupling     | `G(E,G)`  | Environmental and network coupling             |

The operator `F` is Lipschitz-continuous in `C` for theoretical well-posedness. Numerical integration via Runge-Kutta or Euler-Maruyama is required for all but the most idealized cases.

---

### 5.3 Temporal Interaction Graph

Civilizations interact through a time-varying weighted graph:

```

G(t) = ( V, A(t) )                                     (Eq. 4)

A_ij(t) = f( trade_ij(t), conflict_ij(t), migration_ij(t), κ_ij(t) )

```

The adjacency matrix `A(t)` **co-evolves** with the state vector `C(t)`:

```

dC/dt = F( C(t), E(t), G(t) )     ← state dynamics     (Eq. 5a)
dA/dt = Φ( A(t), C(t) )           ← graph dynamics     (Eq. 5b)
dE/dt = ξ(t)                       ← environmental      (Eq. 5c)

```

**Graph-theoretic diagnostic measures:**

| Measure               | Expression                    | Interpretation                              |
|-----------------------|-------------------------------|---------------------------------------------|
| Degree Centrality     | `k_i(t) = Σ_j A_ij(t)`       | Influence of civilization `i`               |
| Clustering Coefficient| `f(triangles, A)`             | Regional cohesion and alliance density      |
| Betweenness Centrality| `Σ σ_jk(i)/σ_jk`             | Intermediary role in trade and information  |
| Fiedler Eigenvalue    | `λ₂(L(t))`                   | Algebraic connectivity; fragmentation risk  |
| Spectral Radius       | `ρ(A(t)) = max|λᵢ(A)|`       | Maximum rate of influence propagation       |

---

### 5.4 Environmental Coupling

```

E(t) = [ climate(t),  temperature(t),  precipitation(t) ]ᵀ   (Eq. 6)

F_E = Γ · ∇E(t)                                               (Eq. 7)

```

**Vulnerability index:**

```

V_env(t) = ‖ Γ · ∇E(t) ‖₂                                    (Eq. 8)

```

- `Γ ∈ ℝⁿˣᵏ` — environmental sensitivity tensor (calibrated via MLE against known collapse events)
- High `V_env(t)` with low stability `S(t)` → elevated collapse risk

---

### 5.5 Knowledge Diffusion

**Linear diffusion on temporal graph:**

```

dK_i/dt = Σ_{j≠i} A_ij(t) · ( K_j − K_i )                   (Eq. 9)

```

**Generalized nonlinear form:**

```

dK/dt = −L(t)·K + Ψ(K, A)                                    (Eq. 10)

L(t) = D(t) − A(t)     (graph Laplacian)

```

**Absorptive capacity model:**

```

Ψᵢ(K, A) = α · Kᵢᵝ · Σ_j A_ij · max(K_j − K_i, 0)          (Eq. 11)

β > 1        superlinear absorptive capacity
α ∈ (0, 1]   institutional openness parameter

```

---

### 5.6 Fokker-Planck Probabilistic Layer

Archaeological data is inherently incomplete. CHRONO-ARCH operates at the level of **probability distributions** over state trajectories.

**Stochastic evolution (Itô SDE):**

```

dC = F(C, E, G) dt + σ(C) dW                                  (Eq. 12)

```

**Fokker-Planck equation:**

```

∂P(C,t)/∂t = −∇·(P·F) + D·∇²P                               (Eq. 13)

drift:     −∇·(P·F)   deterministic dynamics
diffusion: D·∇²P       uncertainty / stochasticity

```

**Sequential Bayesian assimilation:**

```

P(C,t | data_{1:t}) ∝ L(data_t | C) · P(C,t | data_{1:t-1})  (Eq. 14)

```

---

### 5.7 Collapse and Phase Transition Theory

Collapse is modeled as an **endogenous phase transition**, not an exogenous shock.

**Stability functional:**

```

S(t) = Σᵢ wᵢ · Cᵢ(t) − λ · σ(E(t))                          (Eq. 15)

Collapse criterion: S(t) < θ_c

```

**Phase transition condition:**

```

φ(C) = ∇_C S(C)                                               (Eq. 16)

Criticality: ‖φ(C)‖ → ∞  as  C → C_crit

```

**Phase classification:**

| Phase              | Condition           | Behavior                           | Resilience                            |
|--------------------|---------------------|------------------------------------|---------------------------------------|
| Phase I — Stable   | `S(t) >> θ_c`       | Converges to attractor             | Resilient to moderate shocks          |
| Phase II — Critical| `S(t) ≈ θ_c`        | Sensitivity diverges; rising variance | Fragile; elevated collapse risk    |
| Phase III — Collapse| `S(t) < θ_c`       | Transition to new attractor        | Recovery requires strong shocks       |

**Early warning signals:**

```

Var[C(t)]  ↑  as  t → t_collapse    rising variance           (Eq. 17a)
AC₁(t)     ↑  as  t → t_collapse    lag-1 autocorrelation     (Eq. 17b)
τ_relax(t) ↑  as  t → t_collapse    critical slowing down     (Eq. 17c)

```

---

### 5.8 Causal Inference Framework

Three levels of causal knowledge following Pearl's causal ladder:

**Causal graph:**

```

G_causal = (V_causal, E_causal)                                (Eq. 18)

```

**Causal effect via do-calculus:**

```

P( C | do(X = x) ) = ∫ P(C | X=x, Z=z) · P(Z=z) dz           (Eq. 19)

```

**Counterfactual query:** `E[ C_t | do(X = x), C_{1:t-1} = c ]`

Answers questions of the form: *"What would have happened to civilization i had the climate event at time t not occurred?"*

---

## 6. Computational Architecture

CHRONO-ARCH is organized as a **four-layer architecture**:

```

┌─────────────────────────────────────────────────────────┐
│  LAYER IV — Simulation & Scenario Analysis              │
│  Agent-based modeling · Counterfactual scenarios ·      │
│  Phase diagrams · Collapse risk assessment              │
├─────────────────────────────────────────────────────────┤
│  LAYER III — Model & Inference                          │
│  Temporal GNN · SDE Simulator ·                         │
│  Fokker-Planck Solver · Causal Graph Learner            │
├─────────────────────────────────────────────────────────┤
│  LAYER II — Embedding & Fusion                          │
│  Temporal embeddings · Graph embeddings ·               │
│  Multimodal fusion · Missing data imputation            │
├─────────────────────────────────────────────────────────┤
│  LAYER I — Data Ingestion & Representation              │
│  Archaeological datasets · Paleoclimate proxies ·       │
│  Geospatial data · Textual corpora · Trade/conflict     │
└─────────────────────────────────────────────────────────┘

```

**Temporal Graph Neural Network (TGNN) update rule:**

```

hᵢ^(t+1) = σ( W_self · hᵢᵗ + Σ_j A_ij(t) · W_nb · hⱼᵗ + b )  (Eq. 20)

```

---

## 7. Simulation Algorithm

```

Algorithm 1 — CHRONO-ARCH Simulation Loop

INPUT:   C₀, E₀, G₀, T (time horizon), θ_c, dt
OUTPUT:  { C(t), S(t), K(t), P(C,t), events } for t ∈ [0, T]

INITIALIZE:
C ← C₀ ;  E ← E₀ ;  G ← G₀ ;  events ← []

FOR t = 1 TO T:

RETURN { C, S, K, P, events, EWS }

```

---

## 8. Variable Index

| Symbol      | Domain        | Description                       | Data Source                    |
|-------------|---------------|-----------------------------------|-------------------------------|
| `C(t)`      | `ℝⁿ`          | Civilizational state vector       | Inferred / reconstructed       |
| `E(t)`      | `ℝᵏ`          | Environmental forcing field       | Paleoclimate proxy data        |
| `G(t)`      | Graph         | Inter-civilizational network      | Trade / conflict records       |
| `A(t)`      | `ℝᴺˣᴺ`        | Weighted adjacency matrix         | Derived from G(t)              |
| `K_i(t)`    | `ℝ₊`          | Knowledge level of node i         | Textual corpus inference       |
| `L(t)`      | `ℝᴺˣᴺ`        | Graph Laplacian at time t         | Computed from A(t)             |
| `S(t)`      | `ℝ`           | Stability functional              | Derived quantity               |
| `P(C,t)`    | `[0,1]`       | State probability density         | Fokker-Planck solution         |
| `Γ`         | `ℝᵏˣⁿ`        | Environmental sensitivity tensor  | Model parameter (calibrated)   |
| `θ_c`       | `ℝ`           | Collapse threshold                | Calibrated from case studies   |

---

## 9. Project Structure

```

CHRONO-ARCH/
│
├── chrono_arch/                      # Core Python package
│   ├── init.py
│   ├── state/
│   │   ├── init.py
│   │   ├── state_vector.py           # Civilizational state vector C(t)
│   │   ├── evolution.py              # Master evolution equation (Eq. 2–3)
│   │   └── initializer.py            # State initialization utilities
│   │
│   ├── graph/
│   │   ├── init.py
│   │   ├── temporal_graph.py         # Temporal interaction graph G(t) (Eq. 4)
│   │   ├── co_evolution.py           # Co-evolving system Φ (Eq. 5a–5c)
│   │   ├── graph_measures.py         # Centrality, Laplacian, Fiedler value
│   │   └── tgnn.py                   # Temporal GNN update rule (Eq. 20)
│   │
│   ├── environment/
│   │   ├── init.py
│   │   ├── env_model.py              # Environmental forcing E(t) (Eq. 6)
│   │   ├── coupling.py               # Sensitivity tensor Γ (Eq. 7)
│   │   └── vulnerability.py          # Vulnerability index V_env (Eq. 8)
│   │
│   ├── diffusion/
│   │   ├── init.py
│   │   ├── knowledge_diffusion.py    # Linear diffusion (Eq. 9–10)
│   │   └── absorptive_capacity.py    # Nonlinear Ψ model (Eq. 11)
│   │
│   ├── probabilistic/
│   │   ├── init.py
│   │   ├── sde.py                    # Stochastic SDE (Eq. 12)
│   │   ├── fokker_planck.py          # Fokker-Planck PDE (Eq. 13)
│   │   ├── particle_filter.py        # SMC/particle filter for high-dim
│   │   └── bayesian_assimilation.py  # Sequential Bayesian update (Eq. 14)
│   │
│   ├── collapse/
│   │   ├── init.py
│   │   ├── stability.py              # Stability functional S(t) (Eq. 15)
│   │   ├── phase_transition.py       # Phase detection (Eq. 16)
│   │   └── early_warning.py          # EWS signals Var, AC1, τ (Eq. 17)
│   │
│   ├── causal/
│   │   ├── init.py
│   │   ├── causal_graph.py           # DAG structure (Eq. 18)
│   │   ├── do_calculus.py            # Intervention estimator (Eq. 19)
│   │   └── counterfactual.py         # Counterfactual query engine
│   │
│   └── simulation/
│       ├── init.py
│       ├── engine.py                 # Algorithm 1 — main simulation loop
│       ├── agent_based.py            # Agent-based layer
│       ├── scenario.py               # Counterfactual scenario builder
│       └── phase_diagram.py          # Bifurcation / phase space analysis
│
├── layers/                           # Four-layer architecture
│   ├── layer1_ingestion/
│   │   ├── archaeological.py         # Site inventories, radiocarbon dates
│   │   ├── paleoclimate.py           # Isotope records, pollen, speleothems
│   │   ├── geospatial.py             # Settlement maps, territorial data
│   │   ├── textual_nlp.py            # NLP encoding of textual corpora
│   │   └── trade_conflict.py         # Network edge data reconstruction
│   │
│   ├── layer2_embedding/
│   │   ├── temporal_embed.py         # Gaussian process interpolation
│   │   ├── graph_embed.py            # node2vec + temporal embeddings
│   │   ├── fusion_encoder.py         # Multimodal late-fusion architecture
│   │   └── imputation.py             # MICE / VAE missing data imputation
│   │
│   ├── layer3_inference/
│   │   ├── model_interface.py        # Unified model API
│   │   └── parameter_calibration.py  # MLE / Bayesian parameter estimation
│   │
│   └── layer4_simulation/
│       ├── forward_sim.py            # Ensemble forward simulation
│       ├── counterfactual_sim.py     # Do-calculus scenario simulation
│       └── viz.py                    # Phase diagrams, trajectory plots
│
├── data/
│   ├── examples/                     # Example datasets for quick start
│   │   ├── bronze_age_collapse.csv
│   │   ├── maya_classic_terminal.csv
│   │   └── roman_network.json
│   ├── schemas/                      # Data format specifications
│   └── README.md
│
├── benchmarks/
│   ├── collapse_detection/           # Phase transition detection benchmarks
│   ├── diffusion_accuracy/           # Knowledge diffusion validation
│   └── probabilistic_calibration/    # Fokker-Planck calibration tests
│
├── tests/
│   ├── unit/
│   │   ├── test_state_vector.py
│   │   ├── test_temporal_graph.py
│   │   ├── test_fokker_planck.py
│   │   ├── test_stability.py
│   │   └── test_causal_graph.py
│   └── integration/
│       ├── test_simulation_loop.py
│       └── test_full_pipeline.py
│
├── notebooks/
│   ├── 01_quickstart.ipynb           # Getting started walkthrough
│   ├── 02_bronze_age_collapse.ipynb  # 4.2 kya event case study
│   ├── 03_maya_collapse.ipynb        # Terminal Classic Maya case study
│   ├── 04_knowledge_diffusion.ipynb  # Diffusion dynamics demo
│   ├── 05_phase_diagrams.ipynb       # Phase space visualization
│   └── 06_counterfactuals.ipynb      # Do-calculus counterfactual queries
│
├── docs/
│   ├── theory.md                     # Extended theoretical documentation
│   ├── api_reference.md              # Full API reference
│   ├── assumptions.md                # Formal assumption register A1–A6
│   └── limitations.md                # Systematic limitation analysis
│
├── config/
│   ├── default.yaml                  # Default simulation parameters
│   ├── collapse_thresholds.yaml      # Calibrated θ_c values by region/era
│   └── sensitivity_tensors.yaml      # Pre-calibrated Γ tensors
│
├── Netlify/                          # Official website source
│   ├── index.html                    # Home page
│   ├── dashboard.html                # Live dashboard
│   ├── results.html                  # Benchmark results
│   ├── documentation.html            # Documentation
│   └── registration.html             # OSF registration
│
├── THEORETICAL_FRAMEWORK.md          # Full mathematical specification
├── CHANGELOG.md                      # Version history
├── REPRODUCIBILITY.md                # Reproducibility guide
├── AUTHORS.md                        # Author information
├── EVALUATION_PROTOCOL.md            # Validation and evaluation protocol
├── REAL_WORLD_BENCHMARK_PLAN.md      # Planned benchmark datasets
├── requirements.txt                  # Python dependencies
├── setup.py                          # Package setup
├── pyproject.toml                    # Build configuration
├── LICENSE                           # MIT License
└── README.md                         # This file

```

---

## 10. Installation

**From PyPI (recommended):**

```bash
pip install chrono-arch
```

From source:

```bash
git clone https://github.com/gitdeeper12/CHRONO-ARCH.git
cd CHRONO-ARCH
pip install -e .
```

Dependencies:

```
numpy >= 1.24
scipy >= 1.10
networkx >= 3.0
torch >= 2.0          # TGNN component
torch-geometric >= 2.3
pandas >= 2.0
matplotlib >= 3.7
scikit-learn >= 1.3
pgmpy >= 0.1.21       # Causal graph learning
```

---

11. Quick Start

```python
from chrono_arch.simulation import Engine
from chrono_arch.state import StateVector
from chrono_arch.graph import TemporalGraph

# Initialize civilizational state
C0 = StateVector(
    environmental_adaptation=0.7,
    resource_availability=[1.2, 0.8, 1.5],
    technological_complexity=0.45,
    sociopolitical_stability=0.6,
    demographic_pressure=0.4,
    economic_integration=0.55
)

# Define initial interaction network
G0 = TemporalGraph.from_edge_list([
    ("CivA", "CivB", {"trade": 0.8, "conflict": 0.1}),
    ("CivB", "CivC", {"trade": 0.5, "migration": 0.3}),
])

# Run simulation
engine = Engine(collapse_threshold=0.25, dt=1.0)
results = engine.simulate(C0=C0, G0=G0, T=500)

# Check for collapse events
for event in results.events:
    print(f"[t={event.t}] {event.type} detected — S(t) = {event.stability:.4f}")

# Plot early warning signals
results.plot_early_warning_signals()
```

Counterfactual query (do-calculus):

```python
from chrono_arch.causal import DoCalculus

do = DoCalculus(results.causal_graph)

# What if the 4.2 kya drought had not occurred?
counterfactual = do.intervene(
    variable="precipitation",
    value=1.0,           # Normal precipitation level
    time_range=(4200, 4100)
)
print(counterfactual.expected_stability())
```

---

12. Applications

Application Domain Key Framework Component Primary Equations
Computational Archaeology Bayesian state inference Eq. 13–14
Climate-Civilization Modeling Environmental sensitivity tensor Γ Eq. 6–8
Historical Simulation Full simulation loop Algorithm 1
Cultural Diffusion Analysis Knowledge diffusion on temporal graph Eq. 9–11
Collapse Prediction Research Phase transition + EWS Eq. 15–17
Digital Humanities AI Multimodal fusion + TGNN Eq. 20

---

13. Limitations and Assumptions

Formal assumption register:

ID Assumption
A1 F is Lipschitz-continuous in C (ensures ODE well-posedness)
A2 E(t) is exogenous — no feedback from civilizational state to climate
A3 Civilizational node boundaries are resolvable in the data (identifiability)
A4 Archaeological proxies are conditionally independent given C(t)
A5 Collapse is a low-probability absorbing state (not guaranteed recovery)
A6 The causal graph G_causal is acyclic within each time-slice

Known limitations:

Limitation Impact Mitigation
Data incompleteness Wide credible intervals Marginalization; missing data models
Temporal uncertainty Inflated trajectory variance Bayesian date calibration; IntCal23
Non-identifiability Multiple configs fit observations Regularization; informative priors
Historical non-determinism No unique prediction Ensemble forecasting; do-calculus
High-dim Fokker-Planck Analytically intractable Particle filters; variational inference
Over-interpretation risk Precision may exceed epistemic warrant Mandatory uncertainty reporting

Note: CHRONO-ARCH is a descriptive and inferential framework. Numeric outputs carry formal uncertainty bounds and should not be interpreted as deterministic historical predictions.

---

14. Distribution Platforms

# Platform Link Status
1 GitHub (Primary) https://github.com/gitdeeper12/CHRONO-ARCH ✅
2 GitLab (Mirror) https://gitlab.com/gitdeeper12/CHRONO-ARCH ✅
3 Bitbucket (Mirror) https://bitbucket.org/gitdeeper-12/CHRONO-ARCH ✅
4 Codeberg (Mirror) https://codeberg.org/gitdeeper12/CHRONO-ARCH ✅
5 PyPI https://pypi.org/project/chrono-arch ✅
6 Zenodo Archive https://doi.org/10.5281/zenodo.20330475 ✅
7 Official Website https://chronoarch.netlify.app ✅

---

15. Citation

General Citation

If you use CHRONO-ARCH in your research, please cite:

```bibtex
@software{baladi2026chronoarch,
  author    = {Baladi, Samir},
  title     = {CHRONO-ARCH: A Computational Framework for Temporal Archaeology
               and Civilizational Dynamics Using AI and Complex Systems Modeling},
  year      = {2026},
  version   = {1.0.0},
  doi       = {10.5281/zenodo.20330475},
  url       = {https://github.com/gitdeeper12/CHRONO-ARCH},
  license   = {MIT}
}
```

OSF Preregistration Citation

```bibtex
@misc{baladi2026chronoarchprereg,
  author    = {Baladi, Samir},
  title     = {CHRONO-ARCH: Preregistration of Computational Framework for Temporal Archaeology},
  year      = {2026},
  doi       = {10.17605/OSF.IO/2BWZD},
  url       = {https://osf.io/bfd8g}
}
```

DOI: 10.5281/zenodo.20330475

Related Projects: ENTRO-PATH · DSFT / IKPS-CORE · EntropyLab Series

---

16. Author

Samir Baladi
Independent Researcher — Ronin Institute / Rite of Renaissance

· ORCID: 0009-0003-8903-0029
· Email: gitdeeper@gmail.com
· GitHub: gitdeeper12
· GitLab: gitdeeper12
· Zenodo: 10.5281/zenodo.20330475

---

17. License

This project is released under the MIT License.

```
MIT License

Copyright (c) 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

CHRONO-ARCH v1.0.0 · MIT License · May 2026

📄 Paper · 🐙 GitHub · ⛓ GitLab · 🐍 PyPI · 🌐 Website · 📋 OSF · 👤 ORCID

Preprint — Not Peer-Reviewed

</div>
