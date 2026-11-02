import pandas as pd

df = pd.read_csv("data/diabetes.csv")

print("EXPERIMENT 5b - DATASET INFORMATION")

print("\nDataset information:")
df.info()

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nDataset dimensions:")
print(df.shape)
