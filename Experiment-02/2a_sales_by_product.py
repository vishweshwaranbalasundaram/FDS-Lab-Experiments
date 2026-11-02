import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Experiment-02/data/sales_data.csv")

product_summary = df.groupby("Product")["Sales"].sum()

print("TOTAL SALES BY PRODUCT")
print(product_summary)

plt.figure(figsize=(10, 6))
plt.bar(product_summary.index, product_summary.values)

plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.tight_layout()

plt.savefig("Experiment-02/outputs/2a_sales_by_product.png")
plt.show()
