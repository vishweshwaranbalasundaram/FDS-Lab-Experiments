import pandas as pd

df = pd.read_csv("data/website_traffic.csv")
df["Date"] = pd.to_datetime(df["Date"])

print("EXPERIMENT 6a - WEBSITE TRAFFIC EXPLORATION")

print("\nFirst five records:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDataset shape:")
print(df.shape)
