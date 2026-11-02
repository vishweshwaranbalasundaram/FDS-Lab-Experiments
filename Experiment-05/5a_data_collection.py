import pandas as pd

df = pd.read_csv("data/diabetes.csv")

print("EXPERIMENT 5a - DATA COLLECTION")
print("\nFirst five records:")
print(df.head())

print("\nLast five records:")
print(df.tail())

print("\nDataset shape:", df.shape)
