import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

df["Species"] = df["target"].map(
    dict(enumerate(iris.target_names))
)

print("EXPERIMENT 9a - COUNT PLOT")
print("\nFirst five records:")
print(df.head())

print("\nSpecies counts:")
print(df["Species"].value_counts())

sns.countplot(data=df, x="Species")
plt.title("Count of Iris Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/9a_count_plot.png")
plt.show()
