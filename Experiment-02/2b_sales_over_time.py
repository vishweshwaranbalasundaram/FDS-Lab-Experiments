import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Experiment-02/data/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

sales_over_time = df.groupby("Date")["Sales"].sum()

print("SALES OVER TIME")
print(sales_over_time)

plt.figure(figsize=(10, 6))
plt.plot(sales_over_time.index, sales_over_time.values, marker="o")

plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.title("Sales Over Time")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("Experiment-02/outputs/2b_sales_over_time.png")
plt.show()
