import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/feature_scaling.csv")
features = ["Age", "Salary", "Experience"]

scaler = StandardScaler()
scaled = scaler.fit_transform(df[features])

result = pd.DataFrame(scaled, columns=features)
result.insert(0, "Feature", df["Feature"])
result.to_csv("outputs/14a_standardized_data.csv", index=False)

print("STANDARDIZATION USING STANDARDSCALER")
print(result.round(3))
print("\nMean after scaling:")
print(result[features].mean().round(3))
print("\nStandard deviation after scaling:")
print(result[features].std(ddof=0).round(3))
