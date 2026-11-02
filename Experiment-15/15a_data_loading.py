import pandas as pd

df = pd.read_csv("data/pre-process_datasample.csv")

print("FIRST FIVE ROWS")
print(df.head())

print("\nDATASET INFORMATION")
df.info()

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDATASET DESCRIPTION")
print(df.describe(include="all"))

print("\nDATASET SHAPE:", df.shape)
