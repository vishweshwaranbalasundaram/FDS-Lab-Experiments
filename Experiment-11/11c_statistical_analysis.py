import pandas as pd

df = pd.read_csv("data/employees.csv")

print("EXPERIMENT 11c - STATISTICAL ANALYSIS")

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nMaximum Salary:")
print(df["Salary"].max())

print("\nMinimum Salary:")
print(df["Salary"].min())

print("\nDepartment Count:")
print(df["Department"].value_counts())
