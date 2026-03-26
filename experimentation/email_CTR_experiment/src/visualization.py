# Visualization functions for the email CTR experiment

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./data/email_campaign.csv') 

# Function to plot the click-through rates (CTR) for control and treatment groups
def plot_ctr(data):
    """
    Plots the click-through rates (CTR) for control and treatment groups.

    Parameters:
    data (pd.DataFrame): A DataFrame containing user interactions, including group assignments and clicks.
    """

    # Calculate CTR for each group
    ctr_data = data.groupby('group')['clicked'].mean().reset_index()

    # Create a bar plot to visualize CTR
    plt.figure(figsize=(8, 6))
    sns.barplot(x='group', y='clicked', data=ctr_data, palette='viridis')
    plt.title('Click-Through Rate (CTR) by Group')
    plt.xlabel('Group')
    plt.ylabel('Click-Through Rate (CTR)')
    plt.ylim(0, 0.15)
    plt.show()

def plot_segment_ctr(df: pd.DataFrame):
    segment_ctr = (
        df.groupby(["segment", "group"])["clicked"]
        .mean()
        .unstack() * 100
    )

    plt.figure()
    segment_ctr.plot(kind="bar")
    plt.ylabel("CTR (%)")
    plt.title("CTR by Segment and Group")
    plt.xticks(rotation=0)

    plt.savefig("results/ctr_by_segment.png", dpi=300)
    plt.show()

if __name__ == "__main__":

    # Load the simulated data
    campaign_data = pd.read_csv('./data/email_campaign.csv')

    # Plot the CTR for control and treatment groups
    plot_ctr(campaign_data)

    plot_segment_ctr(campaign_data)