import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range("2025-01-01", periods=120, freq="D")
trend = np.arange(120) * 2
seasonality = 80 * np.sin(2 * np.pi * np.arange(120) / 7)
noise = np.random.normal(0, 20, 120)

page_views = 500 + trend + seasonality + noise

df = pd.DataFrame({
    "Date": dates,
    "Page_Views": page_views.astype(int),
    "Unique_Visitors": (page_views * 0.65).astype(int),
    "Bounce_Rate": np.random.uniform(30, 60, 120)
})

# Add a few artificial traffic spikes for anomaly detection
df.loc[20, "Page_Views"] += 400
df.loc[75, "Page_Views"] += 500

df.to_csv("data/website_traffic.csv", index=False)

print("Website traffic dataset created successfully!")
print(df.head())
