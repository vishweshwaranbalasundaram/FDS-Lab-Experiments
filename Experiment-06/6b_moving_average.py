import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/website_traffic.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Moving_Average"] = df["Page_Views"].rolling(window=7).mean()

print("EXPERIMENT 6b - TREND AND MOVING AVERAGE")
print(df[["Date", "Page_Views", "Moving_Average"]].tail(15))

plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Page_Views"], label="Daily Page Views")
plt.plot(df["Date"], df["Moving_Average"],
         label="7-Day Moving Average", linewidth=2)

plt.title("Website Traffic Trend and Moving Average")
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("outputs/6b_moving_average.png")
plt.show()
