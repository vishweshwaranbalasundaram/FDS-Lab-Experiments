import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/tips.csv")

print("RELATIONSHIP ANALYSIS")

print("\nAverage bill and tip:")
print(df[["total_bill", "tip"]].mean())

# Jointplot
g = sns.jointplot(data=df, x="tip", y="total_bill", kind="hex")
g.fig.suptitle("Jointplot: Tip vs Total Bill", y=1.02)
g.savefig("outputs/16d_jointplot.png", bbox_inches="tight")
plt.close("all")

# Pairplot for numerical columns
g = sns.pairplot(df[["total_bill", "tip", "size"]])
g.fig.suptitle("Pairplot of Numerical Features", y=1.02)
g.savefig("outputs/16d_pairplot.png", bbox_inches="tight")
plt.close("all")

# Pairplot grouped by time
if df["time"].nunique() > 1:
    g = sns.pairplot(df, vars=["total_bill", "tip", "size"], hue="time")
    g.savefig("outputs/16d_pairplot_by_time.png", bbox_inches="tight")
    plt.close("all")

# Pairplot grouped by day
if df["day"].nunique() > 1:
    g = sns.pairplot(df, vars=["total_bill", "tip", "size"], hue="day")
    g.savefig("outputs/16d_pairplot_by_day.png", bbox_inches="tight")
    plt.close("all")

print("\nRelationship analysis charts saved successfully.")
