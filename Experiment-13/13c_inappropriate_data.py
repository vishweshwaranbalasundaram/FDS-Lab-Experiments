import pandas as pd

df = pd.read_csv("data/hotel.csv")

print("EXPERIMENT 13c - HANDLE INAPPROPRIATE DATA")

print("\nOriginal Data:")
print(df)

# Replace invalid ratings
df["Rating"] = df["Rating"].where(
    df["Rating"].between(1, 5)
)

# Replace invalid passenger counts
df["NoOfPax"] = df["NoOfPax"].where(
    df["NoOfPax"] > 0
)

# Standardize hotel names
df["Hotel"] = df["Hotel"].replace({
    "Ibys": "Ibis"
})

# Standardize food preferences
df["FoodPreference"] = df["FoodPreference"].replace({
    "veg": "Veg",
    "Vegetarian": "Veg"
})

print("\nCorrected Data:")
print(df)

df.to_csv("outputs/13c_corrected_data.csv", index=False)
