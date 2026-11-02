import pandas as pd

try:
    import seaborn as sns
    df = sns.load_dataset("tips")
    df.to_csv("data/tips.csv", index=False)
    print("Official Seaborn Tips dataset downloaded.")
except Exception as e:
    print("Could not download Seaborn dataset:", e)
    print("Creating a small illustrative fallback dataset.")

    data = {
        "total_bill": [16.99,10.34,21.01,23.68,24.59,25.29,8.77,26.88,15.04,14.78,
                       10.27,35.26,15.42,18.43,14.83,21.58,10.33,16.29,17.46,13.94],
        "tip": [1.01,1.66,3.50,3.31,3.61,4.71,2.00,3.12,1.96,3.23,
                1.71,5.00,1.57,3.00,3.02,3.92,1.67,3.71,2.54,3.06],
        "sex": ["Female","Male","Male","Male","Female","Male","Male","Male","Male","Male",
                "Male","Female","Male","Male","Male","Female","Female","Male","Female","Male"],
        "smoker": ["No","No","No","No","No","No","No","No","No","No",
                   "No","No","No","No","No","No","No","No","No","No"],
        "day": ["Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun",
                "Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun","Sun"],
        "time": ["Dinner"] * 20,
        "size": [2,3,3,2,4,4,2,4,2,2,2,4,2,4,2,2,2,3,2,2]
    }

    df = pd.DataFrame(data)
    df.to_csv("data/tips.csv", index=False)

print("\nDATASET CREATED")
print(df.head())
print("\nDataset shape:", df.shape)
