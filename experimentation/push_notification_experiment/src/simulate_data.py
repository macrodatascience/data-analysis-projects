"""
Simulate push notification experiment data.

Control: fixed send time
Treatment: personalized predicted active time
"""

import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Experiment parameters
N_USERS = 10000
CONTROL_OPEN_RATE = 0.20
TREATMENT_OPEN_RATE = 0.25

def simulate_users(n_users: int) -> pd.DataFrame:
    """Generate users with group assignments and segments."""
    df = pd.DataFrame({
        "user_id": np.arange(1, n_users + 1),
        "group": np.random.choice(["control", "treatment"], size=n_users),
        "segment": np.random.choice(["new", "active", "dormant"], size=n_users, p=[0.2,0.5,0.3])
    })
    return df

def simulate_engagement(df: pd.DataFrame) -> pd.DataFrame:
    """Simulate open and click behavior."""
    df["opened"] = df.apply(
        lambda row: np.random.binomial(1, CONTROL_OPEN_RATE if row["group"]=="control" else TREATMENT_OPEN_RATE),
        axis=1
    )
    # Assume that 30% of the users clicks after the notifications are opened
    df["clicked"] = df.apply(
        lambda row: np.random.binomial(1, 0.3 if row["opened"]==1 else 0),
        axis=1
    )
    return df

def main():
    
    df = simulate_users(N_USERS)
    df = simulate_engagement(df)
    df.to_csv("data/push_notification_data.csv", index=False)
    print("✅ Data saved to data/push_notification_data.csv")

if __name__ == "__main__":
    main()
