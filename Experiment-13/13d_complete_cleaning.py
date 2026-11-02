import pandas as pd

df = pd.read_csv("data/hotel.csv")

print("EXPERIMENT 13d - COMPLETE DATA CLEANING")

# Remove duplicate records
df = df.drop_duplicates()

# Correct inappropriate values
df["Rating"] = df["Rating"].where(
    df["Rating"].between(1, 5)
)

df["NoOfPax"] = df["NoOfPax"].where(
    df["NoOfPax"] > 0
)

df["Hotel"] = df["Hotel"].replace({
    "Ibys": "Ibis"
})

df["FoodPreference"] = df["FoodPreference"].replace({
    "veg": "Veg",
    "Vegetarian": "Veg"
})

# Fill missing values
for column in ["Rating", "Bill", "NoOfPax"]:
    df[column] = df[column].fillna(df[column].median())

for column in ["Hotel", "FoodPreference"]:
    df[column] = df[column].fillna(df[column].mode()[0])

print("\nCleaned Dataset:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_csv("outputs/13d_cleaned_hotel.csv", index=False)

print("\nCleaned dataset saved successfully!")
