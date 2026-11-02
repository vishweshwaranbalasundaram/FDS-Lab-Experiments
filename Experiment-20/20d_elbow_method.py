import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("data/Mall_Customers.csv")

# Manual: Age, Annual Income and Spending Score
features_el = df.iloc[:, [2, 3, 4]].values

wcss = []

for i in range(1, 10):
    model = KMeans(n_clusters=i, random_state=42, n_init=10)
    model.fit(features_el)
    wcss.append(model.inertia_)
    print(f"Clusters: {i}, WCSS: {model.inertia_:.2f}")

plt.figure(figsize=(9, 5))
plt.plot(range(1, 10), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method for Optimal Clusters")
plt.xticks(range(1, 10))
plt.savefig("outputs/20d_elbow_method.png", bbox_inches="tight")
plt.close()

print("\nElbow method graph saved successfully!")
