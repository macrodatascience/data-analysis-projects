"""
Analyze push notification experiment results.
"""

import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

def load_data(path="data/push_notification_data.csv") -> pd.DataFrame:
    return pd.read_csv(path)

def summary_stats(df: pd.DataFrame):
    """Compute sum, count, and open rates by group"""
    
    summary = df.groupby("group")["opened"].agg(["sum","count"])
    summary["open_rate"] = summary["sum"]/summary["count"]
    return summary

def z_test(summary):
    """Compute two-proportion z-test (control - treatment)"""
    
    clicks = summary["sum"].values      # clicks
    nobs = summary["count"].values      # number of observations
    stat, pval = proportions_ztest(count=clicks, nobs=nobs)
    return stat, pval

def segment_analysis(df: pd.DataFrame):
    """Compute open rate per segment and group"""
    
    return df.groupby(["segment","group"])["opened"].mean().reset_index()

def main():
    df = load_data()
    summary = summary_stats(df)
    print("\n=== Overall Open Rate ===")
    print(summary)
    
    # Step 2: Run Z-test to determine if the observed difference is significant.
    stat, pval = z_test(summary)
    print(f"\nZ-statistic: {stat:.3f}, p-value: {pval:.4f}")

    # Step 3: Calculate the absolute and relative lift to see if it meets the business goals
    
    ctr_c = summary.loc["control", "open_rate"]
    ctr_t = summary.loc["treatment", "open_rate"]
    abs_lift = ctr_t - ctr_c
    rel_lift = abs_lift/ctr_c

    # compare the observed relative lift to the 10% business target.
    
    print(f"\nControl Open Rate: {ctr_c:.3%}")
    print(f"Treatment Open Rate: {ctr_t:.3%}")
    print(f"Absolute Lift: {abs_lift:.3%}")
    print(f"Relative Lift: {rel_lift:.2%}")

    if pval < 0.05 and abs_lift >= 0.04 and rel_lift >= 0.20:
        print("✅ Statistically significant AND meets business goal (≥4% absolute lift and ≥20% relative lift)")
    else:
        print("❌ Either not statistically significant or does not meet the set business goals")
    
    # “The experiment both has a statistically significant effect **and meets our business goal.”
    print("\n=== Segment Analysis ===")
    print(segment_analysis(df))

if __name__ == "__main__":
    main()