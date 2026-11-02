import pandas as pd

df = pd.read_csv("data/hotel.csv")

print("EXPERIMENT 13a - IDENTIFY MISSING VALUES")
print("\nOriginal Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nMissing Value Percentage:")
print((df.isnull().mean() * 100).round(2))
