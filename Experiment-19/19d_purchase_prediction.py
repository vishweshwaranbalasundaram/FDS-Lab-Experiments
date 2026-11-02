import joblib
import numpy as np

model = joblib.load("outputs/logistic_regression_model.pkl")

age = 35
salary = 80000

sample = np.array([[age, salary]])
prediction = model.predict(sample)

print("CUSTOMER AGE:", age)
print("ESTIMATED SALARY:", salary)
print("PURCHASE PREDICTION:", "Yes" if prediction[0] == 1 else "No")
