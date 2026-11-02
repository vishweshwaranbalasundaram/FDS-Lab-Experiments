import pandas as pd
import numpy as np

rng = np.random.default_rng(42)

# Illustrative 200-customer dataset following the manual's structure
df = pd.DataFrame({
    "CustomerID": range(1, 201),
    "Gender": rng.choice(["Male", "Female"], 200),
    "Age": rng.integers(18, 71, 200),
    "Annual Income (k$)": rng.integers(15, 138, 200),
    "Spending Score (1-100)": rng.integers(1, 101, 200)
})

df.to_csv("data/Mall_Customers.csv", index=False)

print("MALL CUSTOMERS DATASET CREATED")
print("Dataset shape:", df.shape)
print(df.head())
