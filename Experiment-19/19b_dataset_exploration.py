import pandas as pd

df = pd.read_csv("data/Social_Network_Ads.csv")
print("DATASET INFORMATION")
print(df.info())
print("\nFIRST FIVE ROWS")
print(df.head())
print("\nPURCHASE COUNTS")
print(df["Purchased"].value_counts())
print("\nSTATISTICAL SUMMARY")
print(df.describe())
print("\nMISSING VALUES")
print(df.isnull().sum())
