import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/feature_scaling.csv")
features = ["Age", "Salary", "Experience"]

scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[features])

result = pd.DataFrame(scaled, columns=features)
result.insert(0, "Feature", df["Feature"])
result.to_csv("outputs/14b_normalized_data.csv", index=False)

print("NORMALIZATION USING MINMAXSCALER")
print(result.round(3))
print("\nMinimum values:")
print(result[features].min())
print("\nMaximum values:")
print(result[features].max())
