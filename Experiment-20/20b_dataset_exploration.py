import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/Mall_Customers.csv")

print("DATASET INFORMATION")
print(df.info())

print("\nFIRST FIVE ROWS")
print(df.head())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nGENDER DISTRIBUTION")
print(df["Gender"].value_counts())

sns.pairplot(df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]])
plt.suptitle("Mall Customers Pairplot", y=1.02)
plt.savefig("outputs/20b_pairplot.png", bbox_inches="tight")
plt.close()

print("\nPairplot saved successfully!")
