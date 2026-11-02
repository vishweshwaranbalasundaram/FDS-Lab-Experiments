import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv("data/website_traffic.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")

print("EXPERIMENT 6c - SEASONAL DECOMPOSITION")

result = seasonal_decompose(
    df["Page_Views"],
    model="additive",
    period=7
)

print("\nTrend component:")
print(result.trend.dropna().head())

print("\nSeasonal component:")
print(result.seasonal.head())

print("\nResidual component:")
print(result.resid.dropna().head())

result.plot()
plt.suptitle("Website Traffic Seasonal Decomposition")
plt.tight_layout()
plt.savefig("outputs/6c_seasonal_decomposition.png")
plt.show()
