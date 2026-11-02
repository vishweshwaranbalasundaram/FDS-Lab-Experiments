import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("data/feature_scaling.csv")
features = ["Age", "Salary", "Experience"]

standard = StandardScaler().fit_transform(df[features])
normalized = MinMaxScaler().fit_transform(df[features])

comparison = pd.DataFrame()
comparison["Feature"] = df["Feature"]

for i, col in enumerate(features):
    comparison[col + "_Standard"] = standard[:, i]
    comparison[col + "_MinMax"] = normalized[:, i]

comparison.to_csv("outputs/14c_scaling_comparison.csv", index=False)

print("COMPARISON OF STANDARDIZATION AND NORMALIZATION")
print(comparison.round(3))
print("\nStandardization: mean approximately 0 and standard deviation 1.")
print("Normalization: values scaled between 0 and 1.")
