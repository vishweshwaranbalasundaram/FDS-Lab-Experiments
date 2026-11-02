import pandas as pd

df = pd.read_csv("data/employees.csv")

print("EXPERIMENT 11b - DATA INSPECTION")

print("\nFirst five records:")
print(df.head())

print("\nLast five records:")
print(df.tail())

print("\nDataset information:")
df.info()

print("\nData types:")
print(df.dtypes)

print("\nDataset shape:")
print(df.shape)
