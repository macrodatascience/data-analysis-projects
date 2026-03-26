# This script is to simulate data for an email click-through rate (CTR) experiment. 
# It generates a dataset with user interactions, including whether they clicked on the email or not.

import numpy as np
import pandas as pd 

#set random seed for reproducibility
np.random.seed(42)

# parameters for the simulation
NUM_USERS = 10000
CONTROL_GROUP_CLICK_THROUGH_RATE = 0.1      # 10% click-through rate for the control group
TREATMENT_GROUP_CLICK_THROUGH_RATE = 0.115   # 11.5% click-through rate for the treatment group

# Assign users randomly to control or treatment groups
def assign_groups(num_users=NUM_USERS):
    """
    Assigns users to control and treatment groups.

    Parameters:
    num_users (int): The total number of users to assign.

    Returns:
    pd.DataFrame: A DataFrame containing user IDs and their assigned groups.
    """
    user_ids = np.arange(1, num_users + 1)
    groups = np.random.choice(['control', 'treatment'], size=num_users, p=[0.5, 0.5])
    
    return pd.DataFrame({
        'user_id': user_ids,
        'group': groups
    })

def simulate_email_ctr_data(users_df, control_ctr=CONTROL_GROUP_CLICK_THROUGH_RATE, treatment_ctr=TREATMENT_GROUP_CLICK_THROUGH_RATE):
    """
    Simulates email click-through rate (CTR) data.

    Parameters:
    users_df (pd.DataFrame): A DataFrame containing user IDs and their assigned groups.
    control_ctr (float): The click-through rate for the control group.
    treatment_ctr (float): The click-through rate for the treatment group.
    """

    # Simulate clicks based on the assigned groups and their respective CTRs

    users_df['clicked'] = users_df['group'].apply(
        lambda x: np.random.binomial(1, control_ctr if x=='control' else treatment_ctr)
    )

    return users_df

def add_user_segments(df: pd.DataFrame) -> pd.DataFrame:
    """Optional: add user segmentation (important for senior-level analysis)."""
    df["segment"] = np.random.choice(
        ["active", "dormant", "new"],
        size=len(df),
        p=[0.5, 0.3, 0.2]
    )
    return df

if __name__ == "__main__":

    # Assign users to groups
    users_df = assign_groups()

    # Simulate email CTR data
    simulated_data_df = simulate_email_ctr_data(users_df)

    # Add user segments 
    segmented_data_df = add_user_segments(simulated_data_df)

    # Save the simulated data to a CSV file
    segmented_data_df.to_csv('data/email_campaign.csv', index=False)

    print("Simulated data has been saved to 'data/email_campaign.csv'")