# Email CTR Experiment (A/B Test)

## Overview

This project simulates and analyzes a real-world **A/B test** to evaluate whether **personalized email subject lines** improve user engagement.

It is designed to reflect how product and marketing experiments are conducted in practice, including:
- Hypothesis formulation  
- Experiment design  
- Statistical testing  
- Insight generation  

## Problem Statement

Email campaigns are a key growth channel, but engagement is often low.

**Question:**  
Does personalizing email subject lines increase click-through rates (CTR)?

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
Personalized subject lines will increase CTR by at least **10% relative lift** compared to generic subject lines.

## Experiment Design

- **Population:** 10,000 users  
- **Groups:**
  - Control → Generic subject line  
  - Treatment → Personalized subject line  
- **Primary Metric:** Click-through rate (CTR)  
- **Secondary Analysis:** Segment-level performance  

**Methodology:**
- Randomized controlled experiment
- Bernoulli simulation for click behavior  
- Two-proportion z-test for statistical significance 
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

```
email_ctr_experiment/
│
├── data/                   # simulated datasets
├── notebooks/              # Exploratory analysis in Jupyter notebooks
├── src/
│   ├── simulate_data.py    # Data generation script to generate synthetic email campaign data
│   ├── analysis.py         # Statistical testing script for experiment analysis
│   └── visualization.py    # plotting scripts
├── results/                # Output visualizations, charts, tables
├── requirements.txt
└── README.md
```
## How to Run

```bash

# 1. Generate data
python src/simulate_data.py

# 2. Run analysis
python src/analysis.py

# 3. Generate visualizations
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

```
**Results**

Example output:

- Control CTR: ~10%
- Treatment CTR: ~12%
- Absolute Lift: ~1.7%
- Relative Lift: ~17%
- Statistical Significance: p < 0.05

**Interpretation:**

- Personalized subject lines significantly improve engagement
- The observed lift exceeds the target hypothesis

**Segment-Level Insights**

The analysis includes user segmentation:

- Active users
- Dormant users
- New users

**Key insight:**

The strongest impact is observed in dormant users, suggesting personalization is particularly effective for re-engagement.

**Key Takeaways**

- Personalization is a high-impact, low-cost optimization lever
- A/B testing provides a reliable framework for decision-making
- Segment-level analysis is critical for uncovering hidden effects
- Statistical significance alone is not enough — business impact matters

**Skills Demonstrated**

- Experiment design and hypothesis testing
- Statistical inference (z-test)
- Data simulation and modeling
- Product and marketing analytics
- Translating data into actionable insights

**Extensions / Future Work**

- Confidence intervals for CTR lift
- Power analysis and sample size estimation
- Bayesian A/B testing approach
- Multi-variant testing (subject line + send time)
- Real-world dataset integration

**Why This Project Matters**

This project demonstrates the ability to:

- Think like a product scientist
- Design and evaluate experiments rigorously
- Connect statistical results to business decisions