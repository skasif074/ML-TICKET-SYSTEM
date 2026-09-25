# eda.py
# Purpose: Performs exploratory data analysis on the cleaned ticket dataset
# and generates the charts required by Task 2 (category distribution,
# priority distribution, status distribution), saving them as PNG files
# so they can be included as screenshots in the final report.

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import clean_dataframe_column
from train import load_data, clean_missing_and_duplicates, DATA_PATH

SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "screenshots")


def run_eda():
    df = load_data(DATA_PATH)
    df = clean_missing_and_duplicates(df)
    df = clean_dataframe_column(df, column="ticket_description")

    os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

    print("\n--- Basic Dataset Info ---")
    print(f"Total tickets: {len(df)}")
    print("\nTickets per category:")
    print(df["category"].value_counts())
    print("\nTickets per priority:")
    print(df["priority"].value_counts())
    print("\nTickets per status:")
    print(df["status"].value_counts())

    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="category", order=df["category"].value_counts().index)
    plt.title("Ticket Count by Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Tickets")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(os.path.join(SCREENSHOTS_DIR, "category_distribution.png"))
    plt.close()

    plt.figure(figsize=(6, 5))
    sns.countplot(data=df, x="priority", order=["High", "Medium", "Low"])
    plt.title("Ticket Count by Priority")
    plt.xlabel("Priority")
    plt.ylabel("Number of Tickets")
    plt.tight_layout()
    plt.savefig(os.path.join(SCREENSHOTS_DIR, "priority_distribution.png"))
    plt.close()

    plt.figure(figsize=(6, 5))
    sns.countplot(data=df, x="status")
    plt.title("Ticket Count by Status")
    plt.xlabel("Status")
    plt.ylabel("Number of Tickets")
    plt.tight_layout()
    plt.savefig(os.path.join(SCREENSHOTS_DIR, "status_distribution.png"))
    plt.close()

    print(f"\nCharts saved to {SCREENSHOTS_DIR}")


if __name__ == "__main__":
    run_eda()