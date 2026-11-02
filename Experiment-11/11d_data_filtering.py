import pandas as pd

df = pd.read_csv("data/employees.csv")

print("EXPERIMENT 11d - DATA SELECTION AND FILTERING")

print("\nSelect Name Column:")
print(df["Name"])

print("\nSelect Multiple Columns:")
print(df[["Name", "Salary"]])

print("\nEmployees with Salary Above 35000:")
print(df[df["Salary"] > 35000])

print("\nEmployees in CSE Department:")
print(df[df["Department"] == "CSE"])
