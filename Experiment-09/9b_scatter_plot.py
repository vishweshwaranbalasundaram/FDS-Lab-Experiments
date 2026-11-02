import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

df["Species"] = df["target"].map(
    dict(enumerate(iris.target_names))
)

print("EXPERIMENT 9b - SCATTER PLOT")

print("\nSepal length and width:")
print(df[["sepal length (cm)", "sepal width (cm)", "Species"]].head())

sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="sepal width (cm)",
    hue="Species"
)

plt.title("Iris Sepal Length vs Width")
plt.tight_layout()
plt.savefig("outputs/9b_scatter_plot.png")
plt.show()
