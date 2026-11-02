import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from contextlib import redirect_stdout

# Create output directory
output_dir = Path("Experiment-02/outputs")
output_dir.mkdir(parents=True, exist_ok=True)

# Load dataset
file_path = "Experiment-02/data/sales_data.csv"
df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"])

with open(output_dir / "experiment_02_output.txt", "w") as report:
    with redirect_stdout(report):

        print("=" * 55)
        print("EXPERIMENT 2: DATA PREPROCESSING AND VISUALIZATION")
        print("=" * 55)

        # Display first five rows
        print("\n1. FIRST FIVE RECORDS")
        print(df.head())

        # Check missing values
        print("\n2. MISSING VALUES")
        print(df.isnull().sum())

        # Handle missing values
        df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
        df = df.dropna(subset=["Product", "Quantity", "Region"])

        print("\n3. DATA AFTER PREPROCESSING")
        print(df.head())

        # Summary statistics
        print("\n4. SUMMARY STATISTICS")
        print(df.describe())

        # Group by product
        product_summary = df.groupby("Product").agg({
            "Sales": "sum",
            "Quantity": "sum"
        }).reset_index()

        print("\n5. TOTAL SALES AND QUANTITY BY PRODUCT")
        print(product_summary)

        # Bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(product_summary["Product"], product_summary["Sales"])
        plt.xlabel("Product")
        plt.ylabel("Total Sales")
        plt.title("Total Sales by Product")
        plt.tight_layout()
        plt.savefig(output_dir / "2a_sales_by_product.png")
        plt.close()

        # Sales over time
        sales_over_time = df.groupby("Date")["Sales"].sum().reset_index()

        plt.figure(figsize=(10, 6))
        plt.plot(
            sales_over_time["Date"],
            sales_over_time["Sales"],
            marker="o"
        )
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.title("Sales Over Time")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(output_dir / "2b_sales_over_time.png")
        plt.close()

        # Pivot table
        pivot_table = df.pivot_table(
            values="Sales",
            index="Region",
            columns="Product",
            aggfunc=np.sum,
            fill_value=0
        )

        print("\n6. SALES BY REGION AND PRODUCT")
        print(pivot_table)

        # Correlation matrix
        correlation_matrix = df[["Sales", "Quantity"]].corr()

        print("\n7. CORRELATION MATRIX")
        print(correlation_matrix)

        # Heatmap
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            correlation_matrix,
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )
        plt.title("Correlation Matrix")
        plt.tight_layout()
        plt.savefig(output_dir / "2c_correlation_heatmap.png")
        plt.close()

        print("\n8. GRAPHS GENERATED SUCCESSFULLY")
        print("All experiment outputs saved.")

# Display saved report in terminal
print((output_dir / "experiment_02_output.txt").read_text())

print("\nEXPERIMENT 2 COMPLETED SUCCESSFULLY!")
print("Check Experiment-02/outputs/")
