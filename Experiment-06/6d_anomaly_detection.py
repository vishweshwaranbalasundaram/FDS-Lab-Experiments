import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/website_traffic.csv")
df["Date"] = pd.to_datetime(df["Date"])

mean = df["Page_Views"].mean()
std = df["Page_Views"].std()

df["Z_Score"] = (df["Page_Views"] - mean) / std

anomalies = df[df["Z_Score"].abs() > 2]

print("EXPERIMENT 6d - ANOMALY DETECTION")

print("\nMean:", mean)
print("Standard Deviation:", std)

print("\nDetected anomalies:")
print(anomalies[["Date", "Page_Views", "Z_Score"]])

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Page_Views"], label="Website Traffic")

plt.scatter(
    anomalies["Date"],
    anomalies["Page_Views"],
    color="red",
    label="Detected Anomalies"
)

plt.title("Website Traffic Anomaly Detection")
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("outputs/6d_anomaly_detection.png")
plt.show()
