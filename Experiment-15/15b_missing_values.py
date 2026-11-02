import pandas as pd

df = pd.read_csv("data/pre-process_datasample.csv")

print("MISSING VALUES BEFORE PREPROCESSING")
print(df.isnull().sum())

# Fill Country with mode
df["Country"] = df["Country"].fillna(df["Country"].mode()[0])

# Fill Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill Salary with rounded mean
df["Salary"] = df["Salary"].fillna(round(df["Salary"].mean()))

print("\nDATA AFTER HANDLING MISSING VALUES")
print(df)

print("\nMISSING VALUES AFTER PREPROCESSING")
print(df.isnull().sum())

df.to_csv("outputs/15b_missing_values_handled.csv", index=False)
print("\nSaved: outputs/15b_missing_values_handled.csv")
