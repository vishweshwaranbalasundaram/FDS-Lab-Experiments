import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("data/Mall_Customers.csv")

# Manual: Annual Income and Spending Score
features = df.iloc[:, [3, 4]].values

model = KMeans(n_clusters=5, random_state=42, n_init=10)
model.fit(features)

Final = df.iloc[:, [3, 4]].copy()
Final["label"] = model.predict(features)

print("K-MEANS CLUSTERING")
print("\nCluster counts:")
print(Final["label"].value_counts().sort_index())

print("\nCluster centers:")
print(model.cluster_centers_)

Final.to_csv("outputs/20c_clustered_customers.csv", index=False)

plt.figure(figsize=(10, 6))
plt.scatter(
    Final.iloc[:, 0],
    Final.iloc[:, 1],
    c=Final["label"],
    cmap="viridis",
    s=50
)
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker="X",
    s=250,
    edgecolors="black",
    label="Centroids"
)
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("K-Means Customer Segmentation")
plt.legend()
plt.savefig("outputs/20c_kmeans_clusters.png", bbox_inches="tight")
plt.close()

print("\nClustered dataset and visualization saved!")
