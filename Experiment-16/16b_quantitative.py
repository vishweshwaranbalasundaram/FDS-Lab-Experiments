import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/tips.csv")

print("QUANTITATIVE ANALYSIS")
print("\nFirst five rows:")
print(df.head())

print("\nDescriptive statistics:")
print(df[["total_bill", "tip", "size"]].describe())

print("\nTotal bill distribution:")
print(df["total_bill"].value_counts().head(10))

# Distribution with KDE
plt.figure(figsize=(8, 5))
sns.histplot(df["total_bill"], kde=True)
plt.title("Distribution of Total Bill with KDE")
plt.xlabel("Total Bill")
plt.savefig("outputs/16b_total_bill_kde.png", bbox_inches="tight")
plt.close()

# Distribution without KDE
plt.figure(figsize=(8, 5))
sns.histplot(df["total_bill"], kde=False)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.savefig("outputs/16b_total_bill_histogram.png", bbox_inches="tight")
plt.close()

# Boxplot of tips
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["tip"])
plt.title("Boxplot of Tips")
plt.ylabel("Tip")
plt.savefig("outputs/16b_tip_boxplot.png", bbox_inches="tight")
plt.close()

print("\nQuantitative charts saved successfully.")
