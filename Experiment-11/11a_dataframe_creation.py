import pandas as pd

data = {
    "EmpID": [101, 102, 103, 104, 105],
    "Name": ["Arun", "Bala", "Charan", "Divya", "Ezhil"],
    "Department": ["CSE", "IT", "ECE", "CSE", "IT"],
    "Salary": [30000, 40000, 35000, 45000, 50000]
}

df = pd.DataFrame(data)

print("EXPERIMENT 11a - DATAFRAME CREATION")
print("\nEmployee DataFrame:")
print(df)

print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
