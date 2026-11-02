import numpy as np
import pandas as pd
from sklearn.datasets import make_classification

# Illustrative dataset with the same structure as the manual
X, y = make_classification(
    n_samples=400, n_features=2, n_informative=2,
    n_redundant=0, n_clusters_per_class=2,
    weights=[257/400, 143/400], random_state=42,
    class_sep=0.9
)

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "User ID": rng.choice(np.arange(15500000, 15900000), 400, replace=False),
    "Gender": rng.choice(["Male", "Female"], 400),
    "Age": np.clip(np.rint(38 + X[:, 0] * 10), 18, 60).astype(int),
    "EstimatedSalary": np.clip(np.rint(65000 + X[:, 1] * 30000), 15000, 150000).astype(int),
    "Purchased": y
})
df.to_csv("data/Social_Network_Ads.csv", index=False)
print("Dataset created successfully!")
print("Dataset shape:", df.shape)
print(df.head())
