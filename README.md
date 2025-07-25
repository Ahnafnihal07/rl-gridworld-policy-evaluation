# Reinforcement Learning Assignment 2: Gridworld Policy Evaluation

This repository contains the code and report for Assignment 2 in the Reinforcement Learning course (Summer 2025).

## 📁 Project Structure

```
rl-gridworld-policy-evaluation/
│
├── code/                  # Python scripts
│   ├── gridworld_env.py
│   ├── monte_carlo_methods.py
│   ├── policy_iteration.py
│   └── rl_assignment2.py     # Main driver script
│
├── report/
│   ├── report.tex         # LaTeX source file
│   └── figures/           # All figures generated in the report
│
└── README.md              # This file
```

## ✅ Features

- **Model-based methods** for value estimation and policy improvement (Part 1)
- **Monte Carlo control** with and without exploring starts (Part 2.1)
- **Off-policy Monte Carlo control** with importance sampling (Part 2.2)
- Reproducible plots and value/policy heatmaps for each method
- Complete LaTeX report with referenced figures

## 📦 Requirements

- Python 3.8+
- `matplotlib`, `numpy`

Install dependencies:
```bash
pip install matplotlib numpy
```

## 🚀 How to Run

To reproduce the results and generate all visualizations:
```bash
cd code
python rl_assignment2.py
```

All figures will be saved in `report/figures/` and referenced in the LaTeX report.

## 📄 Report Compilation

Navigate to the `report/` directory and run:
```bash
pdflatex report.tex
```

## 👨‍💻 Author

Ahnaf Nihal  
Memorial University of Newfoundland  
Reinforcement Learning - Summer 2025
