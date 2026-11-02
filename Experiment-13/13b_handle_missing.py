import pandas as pd

df = pd.read_csv("data/hotel.csv")

print("EXPERIMENT 13b - HANDLE MISSING VALUES")

print("\nBefore Cleaning:")
print(df.isnull().sum())

for column in ["Rating", "Bill", "NoOfPax"]:
    df[column] = df[column].fillna(df[column].median())

for column in ["Hotel", "FoodPreference"]:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nAfter Filling Missing Values:")
print(df)

print("\nRemaining Missing Values:")
print(df.isnull().sum())

df.to_csv("outputs/13b_missing_values_handled.csv", index=False)
