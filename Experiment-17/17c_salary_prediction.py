import pickle
import numpy as np

# Load saved model
with open("outputs/SalaryPred.model", "rb") as file:
    model = pickle.load(file)

print("SALARY PREDICTION USING SAVED MODEL")

# Example prediction
years = 5.0
input_data = np.array([[years]])

predicted_salary = model.predict(input_data)

print(f"\nYears of Experience: {years}")
print(f"Estimated Salary: Rs. {predicted_salary[0][0]:,.2f}")

# More sample predictions
print("\nSAMPLE SALARY PREDICTIONS")
for experience in [1, 3, 5, 7, 10]:
    result = model.predict(np.array([[experience]]))
    print(f"{experience} years -> Rs. {result[0][0]:,.2f}")
