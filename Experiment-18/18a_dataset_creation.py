from sklearn.datasets import load_iris
import pandas as pd
from pathlib import Path

data = load_iris()
df = pd.DataFrame(data.data, columns=["sepal.length","sepal.width","petal.length","petal.width"])
df["variety"] = [data.target_names[i].capitalize() for i in data.target]
Path("data").mkdir(exist_ok=True)
df.to_csv("data/Iris.csv", index=False)
print("Iris dataset created successfully!")
print("Dataset shape:", df.shape)
print(df.head())
