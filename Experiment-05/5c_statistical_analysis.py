import pandas as pd

df = pd.read_csv("data/diabetes.csv")

print("EXPERIMENT 5c - STATISTICAL ANALYSIS")

print("\nStatistical summary:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDiabetes outcome distribution:")
print(df["Outcome"].value_counts())
