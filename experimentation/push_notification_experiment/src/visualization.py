"""
Visualize push notification experiment results
"""

import pandas as pd
import matplotlib.pyplot as plt

def plot_overall_open_rate(df: pd.DataFrame):
    open_rate = df.groupby("group")["opened"].mean() * 100
    plt.figure()
    open_rate.plot(kind="bar", color=["skyblue","orange"])
    plt.ylabel("Open Rate (%)")
    plt.title("Push Notification Open Rate by Group")
    plt.xticks(rotation=0)
    plt.savefig("results/open_rate_by_group.png", dpi=300)
    plt.show()

def plot_segment_open_rate(df: pd.DataFrame):
    segment_open = df.groupby(["segment","group"])["opened"].mean().unstack() * 100
    plt.figure()
    segment_open.plot(kind="bar")
    plt.ylabel("Open Rate (%)")
    plt.title("Segment-Level Open Rate by Group")
    plt.xticks(rotation=0)
    plt.savefig("results/segment_open_rate.png", dpi=300)
    plt.show()

def main():
    df = pd.read_csv("data/push_notification_data.csv")
    plot_overall_open_rate(df)
    plot_segment_open_rate(df)

if __name__ == "__main__":
    main()