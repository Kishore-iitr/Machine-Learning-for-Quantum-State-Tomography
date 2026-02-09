# Project Report: Scalable Machine Learning Pipelines for Quantum Tomography

This repository contains the consolidated research and implementation for a computational framework designed for **Quantum State Tomography (QST)** and **Quantum Channel Classification**, strictly enforcing physical constraints through deep learning.

## 1. Problem Statement
Quantum state reconstruction is a significant bottleneck in quantum computing due to the exponential scaling of the Hilbert space. Traditional linear inversion methods are often computationally expensive and sensitive to statistical noise. This project addresses the need for efficient, noise-robust tomography and automated channel identification to speed up hardware calibration loops.

## 2. Methodology and Workflow

### 2.1 Measurement Strategy
A hybrid measurement model was adopted to balance practical calibration with theoretical optimality:
*   **Pauli Projective Measurements:** Utilized for hardware-native eigenbasis interpretation and debugging.
*   **SIC POVM (Symmetric Informationally Complete):** Utilized for efficient, single-setting tomography with minimal statistical noise.

### 2.2 Model Architecture (DensityNet)
We implemented a multi-layer perceptron (MLP) named **DensityNet** to reconstruct density matrices $\rho$.
*   **Input:** Measurement expectation values $\langle O \rangle = \mathrm{Tr}(\rho O)$.
*   **Physics Enforcement:** The model outputs parameters for a lower-triangular matrix $L$ to ensure $\rho$ is Hermitian, positive semi-definite, and has a unit trace via the Cholesky decomposition:
    $$\rho = \frac{LL^\dagger}{\mathrm{Tr}(LL^\dagger)}$$.

### 2.3 Quantum Channel Classification
For rapid noise diagnostics, a Random Forest classifier was trained on **Choi matrix representations** of various noise families (Depolarizing, Amplitude Damping, Phase Damping, and Bit Flip).

## 3. Repository Structure
The project is organized hierarchically for clarity and reproducibility:
```text
Open_Project_Winter_2025/
|-- data/          # SIC-POVM and Pauli datasets (.npy)
|-- models/        # ML-QST checkpoints (.pkl) and classifiers (.joblib)
|-- notebooks/     # Consistently documented Assignment 1-5 notebooks
|-- src/           # Modular Python scripts for training and generation
|-- results/       # Performance plots (PNG) and LaTeX metric tables
|-- Machine-Learning-for-Quantum-State-Tomography\Final_report_Quantum_Tomography.pdf      # Primary project documentation
```

## 4. Performance Analysis and Results

### 4.1 Scalability Study
Benchmarking across 1–10 qubits (documented in `scalability_analysis.png`) reveals the limits of the current architecture:
*   **Fidelity Decay:** Mean fidelity follows a $1/d$ trend, dropping below the **0.1 threshold** for $n \ge 4$ qubits.
*   **Resource Scaling:** Memory usage grows exponentially with the number of qubits, while runtime remains relatively low (<0.25 ms) with statistical jitter.

### 4.2 Ablation Study (Model Depth)
Tested on a 4-qubit system with layers ranging from 1 to 32 (documented in `ablation_layers.png`):
*   **Depth Impact:** Increased complexity did not significantly improve fidelity for multi-qubit systems, peaking at **~0.089** with a single layer.
*   **Initialization:** "Normal" initialization performed best (**0.1413** fidelity for 3 qubits), while "Zeros" initialization resulted in total failure (**0.0** fidelity).

### 4.3 Channel Classification Accuracy
The Random Forest model achieved **100% accuracy** in identifying noise families from synthetic Choi feature vectors.

| Channel Family | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- |
| Depolarizing | 1.00 | 1.00 | 1.00 |
| Amplitude Damping | 1.00 | 1.00 | 1.00 |
| Phase Damping | 1.00 | 1.00 | 1.00 |

## 5. Replication Guide

### 5.1 Environment Setup
To replicate this environment, run the following commands (Windows PowerShell):
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip wheel
pip install pennylane numpy scipy pandas plotly tqdm scikit-learn joblib
```

### 5.2 Dataset Generation and Training
1.  **Generate Data:** Use `src/data_gen.py` to produce SIC and Pauli expectation values for reference states like $|0\rangle, |1\rangle, |+\rangle$.
2.  **Execute Tomography:** Run `notebooks/Assignment_2.ipynb` to train the DensityNet surrogate.
3.  **Evaluate:** Use `src/metrics.py` to compute Fidelity and Trace Distance.

## 6. Final Reflection
The transition from single-qubit to multi-qubit pipelines highlighted the significant scaling challenges of standard MLP architectures for tomography. While the ML approach is excellent for amortizing reconstruction costs and rapid channel classification, future extensions should explore **Classical Shadows** or **Transformer architectures** to improve the fidelity limit beyond 4 qubits.

## 7. AI Attribution
*   **Tools Used:** ChatGPT/Claude were utilized for code structure optimization and LaTeX verification.
*   **Verification:** All AI-generated density matrices were mathematically verified for **Hermiticity**, **positive semi-definiteness**, and **unit trace**.
