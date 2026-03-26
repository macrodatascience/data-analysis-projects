# Email CTR Experiment (A/B Test)

## Overview
This project simulates and analyzes an A/B test to evaluate whether
personalized email subject lines improve click-through rates (CTR).

## Install dependencies
```
mkdir email_ctr_experiment && cd email_ctr_experiment
mkdir data notebooks src results
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or venv\Scripts\activate for Windows
pip install numpy pandas matplotlib seaborn statsmodels jupyter
pip freeze > requirements.txt
```

## Hypothesis
Personalized subject lines increase CTR by at least 10%.

## Experiment Design
- Population: 10,000 users
- Control: Generic subject line
- Treatment: Personalized subject line
- Metric: Click-through rate (CTR)

## Methodology
- Randomized controlled experiment
- Two-proportion z-test
- Segment-level analysis

## Results
- Treatment CTR > Control CTR
- Statistical significance evaluated via z-test
- Segment analysis reveals heterogeneous effects

## Key Insights
- Personalization improves engagement
- Stronger impact observed in dormant users
- Opportunity for targeted re-engagement campaigns

## Project Structure
- `src/` → core scripts
- `data/` → simulated dataset
- `results/` → charts
- `notebooks/` → exploratory analysis

email_ctr_experiment/
│
├── data/                   # simulated datasets
├── notebooks/              # Jupyter notebooks for exploration
├── src/
│   ├── simulate_data.py    # scripts to generate synthetic email campaign data
│   ├── analysis.py         # scripts for experiment analysis
│   └── visualization.py    # plotting scripts
├── results/                # charts, tables
├── README.md
└── requirements.txt

## How to Run

```bash
python src/simulate_data.py
python src/analysis.py
python src/visualization.py
```

This project simulates an A/B test on email subject lines to demonstrate **hypothesis testing and experimentation** in a product/marketing context.

**Steps:**
1. Simulate email campaign data (`src/simulate_data.py`)
2. Analyze results and run statistical tests (`src/analysis.py`)
3. Visualize CTR by group (`src/visualization.py`)
4. Explore insights in Jupyter notebook (`notebooks/01_experiment.ipynb`)

**Key Metrics:**
- Click-through rate (CTR)
- Statistical significance (z-test)
- Lift between control and treatment groups