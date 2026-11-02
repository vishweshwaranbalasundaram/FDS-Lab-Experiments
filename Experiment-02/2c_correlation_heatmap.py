import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Experiment-02/data/sales_data.csv")

correlation_matrix = df[["Sales", "Quantity"]].corr()

print("CORRELATION MATRIX")
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Matrix")
plt.tight_layout()

plt.savefig("Experiment-02/outputs/2c_correlation_heatmap.png")
plt.show()
