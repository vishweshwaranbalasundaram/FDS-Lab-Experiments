import pandas as pd

df = pd.read_csv("data/Iris.csv")
print("DATASET INFORMATION")
print(df.info())
print("\nVARIETY COUNTS")
print(df["variety"].value_counts())
print("\nFIRST FIVE ROWS")
print(df.head())
print("\nSTATISTICAL SUMMARY")
print(df.describe())
