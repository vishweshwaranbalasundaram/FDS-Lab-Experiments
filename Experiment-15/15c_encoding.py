import pandas as pd

df = pd.read_csv("outputs/15b_missing_values_handled.csv")

print("DATA BEFORE ENCODING")
print(df)

# Convert Country into dummy variables
country_dummies = pd.get_dummies(df["Country"])

# Combine dummy variables with remaining columns
updated_dataset = pd.concat(
    [country_dummies, df[["Age", "Salary", "Purchased"]]],
    axis=1
)

# Encode Purchased: No = 0, Yes = 1
updated_dataset["Purchased"] = updated_dataset["Purchased"].map({
    "No": 0,
    "Yes": 1
})

print("\nFINAL PREPROCESSED DATASET")
print(updated_dataset)

updated_dataset.to_csv("outputs/15c_final_preprocessed_data.csv", index=False)

print("\nSaved: outputs/15c_final_preprocessed_data.csv")
