# Analysis code for the email CTR experiment
# This script analyzes the simulated data from the email click-through rate (CTR) experiment.

import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

def load_data(file_path):
    """
    Loads the simulated data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the simulated data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """

    return pd.read_csv(file_path)

def analyze_ctr(data):
    """
    Analyzes the click-through rates (CTR) for the control and treatment groups.

    Parameters:
    data (pd.DataFrame): A DataFrame containing user interactions, including group assignments and clicks.

    Returns:
    dict: A dictionary containing the CTR for both groups and the p-value from the z-test.
    """

    # Step 1: Aggregate clicks - Calculate the number of clicks and total users in each group

    group_summary = data.groupby('group')['clicked'].agg(['sum', 'count']).reset_index()
    print(group_summary)

    # Step 2: Performing an A/B test using a z-test for proportions

    # This is a two-proportion Z-test, which answers: 
    # "Is there a statistically significant difference in click-through rates between the control and treatment groups?"
    # "Are these two conversion rates statistically different, or just random noise"

    clicks = group_summary['sum'].values   # Number of successes (clicks) in each group
    nobs = group_summary['count'].values   # Total number of observations (trials) in each group

    stat, p_value = proportions_ztest(count = clicks, nobs = nobs)
    print(f"Z-statistic: {stat:.3f}, p-value: {p_value:.3f}")

    # Step 3: Interpretation of results:

    if p_value < 0.05:
        print("✅ The difference in CTR between the groups is statistically significant.")
    else:
        print("❌ The difference in CTR between the groups is not statistically significant.")

    # Step 4: Calculate the CTR and Lift

    control_ctr = clicks[0] / nobs[0] if nobs[0] != 0 else 0
    treatment_ctr = clicks[1] / nobs[1] if nobs[1] != 0 else 0

    absolute_lift = (treatment_ctr - control_ctr)
    relative_lift = absolute_lift / control_ctr if control_ctr != 0 else 0

    return {
        'control_ctr': control_ctr,
        'treatment_ctr': treatment_ctr,
        'p_value': p_value,
        'absolute_lift': absolute_lift,
        'relative_lift': relative_lift
    }

def segment_analysis(df: pd.DataFrame):
    """Breakdown by user segment """
    segment_ctr = (
        df.groupby(["segment", "group"])["clicked"]
        .mean()
        .reset_index()
    )
    return segment_ctr

if __name__ == "__main__":

    # Load the simulated data
    campaign_data = load_data('./data/email_campaign.csv')

    # Analyze the CTR
    results = analyze_ctr(campaign_data)

    # Print the results
    print(f"Control Group CTR: {results['control_ctr']:.2%}")
    print(f"Treatment Group CTR: {results['treatment_ctr']:.2%}")
    print(f"P-value from z-test: {results['p_value']:.4f}")
    print(f"Absolute Lift: {results['absolute_lift']:.3%}")
    print(f"Relative Lift: {results['relative_lift']:.3%}")

    print(f"The p-value indicates that the observed difference in CTR is {'statistically significant' if results['p_value'] < 0.05 else 'not statistically significant'} at the 5% significance level.")
    print(f"Based on the results, we can conclude that the treatment group has a {'higher' if results['absolute_lift'] > 0 else 'lower'} CTR compared to the control group.")

    print("\n==== Segment Analysis ===")
    print(segment_analysis(campaign_data))