import pandas as pd

df = pd.read_csv("data/Salary_data.csv")

print("FIRST FIVE RECORDS")
print(df.head())

print("\nDATASET INFORMATION")
df.info()

print("\nMISSING VALUES")
print(df.isnull().sum())

df.dropna(inplace=True)

print("\nDESCRIPTIVE STATISTICS")
print(df.describe())

print("\nDATASET SHAPE:", df.shape)
