# Push Notification Send-Time Experiment

## Overview
This project simulates an A/B test for a mobile app to optimize **push notification send times**.  
It demonstrates end-to-end experimentation, including hypothesis formulation, simulation, statistical testing, and insight generation.

---

## Problem Statement
Random notification times result in low engagement.  
**Question:** Does sending notifications at each user's predicted active time increase open rates compared to a fixed time?

---

## Business/Engineering Hypothesis
> Personalized notification send times will increase user open rates by at least 20% relative to a fixed time.

**Interpretation:** We care not just about statistical significance, but also about a meaningful effect size for the business.

---

## Statistical Hypothesis
- **Null Hypothesis \(H_0\):** The treatment (personalized timed notifications) has **no effect** on open rates.  
- **Alternative Hypothesis \(H_1\):** The treatment **increases open rates**.  

The Z-test is used to determine whether the observed difference is statistically significant.

---

## Experiment Design
- **Population:** 10,000 users  
- **Groups:**
  - Control → Fixed send time  
  - Treatment → Personalized predicted active time  
- **Metrics:**
  - Primary → Open rate  
  - Secondary → Click-through rate  

**Methodology:**
- Randomized controlled experiment  
- Bernoulli simulation for user engagement  
- Two-proportion z-test for significance  
- Segment-level analysis (new, active, dormant users)

---

## Project Structure
```text
push_notification_experiment/
│
├── data/                   # Simulated dataset
├── notebooks/              # Exploration and insights
├── src/
│   ├── simulate_data.py
│   ├── analysis.py
│   └── visualization.py
├── results/                # Charts and figures
├── requirements.txt
└── README.md
```

## Install dependencies
```
mkdir push_notification_experiment && cd push_notification_experiment
mkdir data notebooks src results
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or .venv\Scripts\activate for Windows
pip install numpy pandas matplotlib seaborn statsmodels jupyter
pip freeze > requirements.txt
```

## How to Run

```
# 1. Generate data
python src/simulate_data.py

# 2. Run analysis
python src/analysis.py

# 3. Generate visualizations
python src/visualization.py
```

**Results**

Example outcomes:

- Control Open Rate: ~20%
- Treatment Open Rate: ~25%
- Absolute Lift: 4 pp (~20% relative lift)
- Statistical significance: p < 0.05

**Segment insights:**

- Treatment is particularly effective for dormant users, suggesting re-engagement potential.

**Tasks Performed**

- Experiment design and hypothesis testing
- Product analytics and metric evaluation
- Segment-level analysis
- Statistical inference (z-test)
- Data simulation and visualization
- Translating analytics into actionable product decisions

**Extensions / Future Work**

- Confidence intervals for open rate lift
- Bayesian A/B testing approach
- Multi-variant tests: send time + notification content
- Integration with real app analytics logs