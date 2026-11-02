import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

df["Species"] = df["target"].map(
    dict(enumerate(iris.target_names))
)

print("EXPERIMENT 9c - PAIR PLOT")
print("\nDataset description:")
print(df.describe())

pair = sns.pairplot(
    df,
    hue="Species",
    diag_kind="hist"
)

pair.fig.suptitle("Pair Plot of Iris Dataset", y=1.02)
pair.savefig("outputs/9c_pair_plot.png")
plt.show()
