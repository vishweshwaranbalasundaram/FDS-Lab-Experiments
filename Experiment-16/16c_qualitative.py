import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/tips.csv")

print("QUALITATIVE ANALYSIS")

print("\nDay counts:")
print(df["day"].value_counts())

print("\nGender counts:")
print(df["sex"].value_counts())

print("\nTime counts:")
print(df["time"].value_counts())

# Countplot for day
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="day")
plt.title("Count of Customers by Day")
plt.savefig("outputs/16c_day_countplot.png", bbox_inches="tight")
plt.close()

# Countplot for sex
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="sex")
plt.title("Count of Customers by Gender")
plt.savefig("outputs/16c_gender_countplot.png", bbox_inches="tight")
plt.close()

# Pie chart for gender
plt.figure(figsize=(6, 6))
df["sex"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.ylabel("")
plt.savefig("outputs/16c_gender_pie.png", bbox_inches="tight")
plt.close()

# Bar chart for gender
plt.figure(figsize=(8, 5))
df["sex"].value_counts().plot(kind="bar")
plt.title("Gender Distribution - Bar Chart")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("outputs/16c_gender_bar.png", bbox_inches="tight")
plt.close()

print("\nQualitative charts saved successfully.")
