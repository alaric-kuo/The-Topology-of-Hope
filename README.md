# The Topology of Hope (希望的拓樸學)
### Project IQD (I-Ching Quantum Dynamics): A 6-Qubit Framework for Modeling Social Phase Transitions
### (基於六量子位元的社會相變建模架構)

![Qiskit](https://img.shields.io/badge/Quantum-Qiskit-blueviolet) ![System](https://img.shields.io/badge/System-Complexity%20Science-orange) ![Status](https://img.shields.io/badge/Status-Research%20MVP-green)

> **"This is not fortune-telling. This is the geometry of our will to live."**
> **「這不是算命。這是我們求生意志的幾何學。」**
> — Dr. Alaric Kuo, Creator of The Topology of Hope

---

## 📖 The Manifesto: Why "Topology of Hope"?

In mathematics, **Topology** studies properties that remain unchanged even when shapes are distorted by immense tension. In life, we call that **Resilience**. Or simply, **Hope**.

We live in a world of high-tension fields—geopolitics, climate crisis, and technological singularity. The old maps are tearing apart. **Project IQD** was born from a simple question: *Can we calculate the path to survival in a collapsing system?*

Through the lens of **Quantum Mechanics** and the ancient binary wisdom of the **I-Ching (Book of Changes)**, we can see the invisible structure beneath the chaos. My model doesn't just predict the collapse; it maps the escape route. It proves that even in the darkest entanglement, there is always a mathematical probability for survival.

---

## ⚙️ The Technology: Project IQD

**Project IQD (I-Ching Quantum Dynamics)** is the core engine behind *The Topology of Hope*. It is an experimental framework that maps ancient binary logic onto modern **6-Qubit Quantum Circuits**.

### The Core Logic (AI 4.0)
Unlike traditional linear models, we treat social structures as quantum states:

1.  **The Qubit-Yao Mapping:**
    * **Hexagram (卦象)** = **6-Qubit Circuit** ($q_0$ to $q_5$).
    * **Yang (—)** = State $|0\rangle$ (Energy/Expansion).
    * **Yin (-- )** = State $|1\rangle$ (Matter/Collapse).
2.  **Tension Fields (Hamiltonian):**
    * External pressures (e.g., COVID-19, Trade War) are modeled as **Rotation Gates ($R_x, R_y$)**.
    * Higher tension ($\theta$) increases the probability of state collapse.
3.  **Entanglement (Non-locality):**
    * We use **CNOT Gates** to simulate how a decision in one node (e.g., a lockdown in China) instantaneously alters the state of a distant node (e.g., US Supply Chain), respecting the principle of quantum non-locality.

---

## 📊 Experimental Verification (Backtesting)

We utilized **IBM Qiskit** to backtest the model against major historical phase transitions (2008-2024).

### 1. The Tale of Two Eras: 2008 vs. 2024
*Visualizing the shift from "Deterministic Collapse" to "Quantum Bifurcation".*

<img width="100%" alt="2008_2024_chart" src="https://github.com/user-attachments/assets/9ad3e7dc-036b-4f66-bb9a-b3edbcc5656c" />

* **2008 (Financial Crisis):** A single dominant collapse state (`000001`). The world was "coherent" in its failure.
* **2024 (AI Singularity):** The graph splits into two distinct peaks. This visualizes a **"Bifurcated Reality"**—a world splitting into parallel operating systems. This is the "Topology" of our current chaos.

### 2. Sensitivity Test: The "What-If" of COVID-19
*Simulating parallel universes to verify model sensitivity.*

<img width="100%" alt="covid_chart png" src="https://github.com/user-attachments/assets/5751299f-b29c-4af2-9c05-d758de4769e9" />


* **Universe A (History):** The model correctly predicted the confusion of 2020 (`101011`) with **69.0%** probability.
* **Universe B & C (Counterfactuals):** When we altered the "Lockdown" or "Supply Chain" parameters, the quantum state shifted significantly. This proves the model is not memorizing history, but calculating **causality**.

---

## 🚀 Quick Start: Run the Simulation

You can replicate our "Tension Field Simulation" using Python and Qiskit.

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np

# Project IQD: 6-Qubit Initialization
qc = QuantumCircuit(6)

# 1. Superposition (The State of Chaos)
qc.h(range(6))

# 2. Inject Tension (The Bias of Reality)
# Example: Simulating a high-tension event like a Pandemic
tension = np.pi / 2.5
qc.rx(tension, 0) # Public Health Stress
qc.rx(tension, 5) # Governance Stress

# 3. Entanglement (The Connection)
qc.cx(5, 2) # Governance impacts Supply Chain

# 4. Observation (The Collapse)
qc.measure_all()

# Run on Quantum Simulator
simulator = AerSimulator()
job = simulator.run(transpile(qc, simulator), shots=5000)
print("Simulation Result:", job.result().get_counts())

## 🔗 Citation
If you use this model or code in your research, please cite the white paper:

> **Kuo, A. (2025). Project IQD: A 6-Qubit Framework for Modeling Social Phase Transitions via I-Ching Binary Logic. ResearchGate. DOI: 10.13140/RG.2.2.20595.80160**

[ResearchGate Link](https://dx.doi.org/10.13140/RG.2.2.20595.80160)
