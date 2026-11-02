import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("data/Salary_data.csv")
df = df.dropna()

# Features and target
features = df[["YearsExperience"]].values
label = df[["Salary"]].values

# Split dataset into training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    features, label, test_size=0.2, random_state=42
)

# Create and train model
model = LinearRegression()
model.fit(x_train, y_train)

# Evaluate model
train_score = model.score(x_train, y_train)
test_score = model.score(x_test, y_test)

print("LINEAR REGRESSION MODEL")
print("\nTraining score:", train_score)
print("Testing score:", test_score)
print("\nCoefficient:", model.coef_)
print("Intercept:", model.intercept_)

print("\nRegression Equation:")
print(f"Salary = {model.coef_[0][0]:.2f} * YearsExperience + {model.intercept_[0]:.2f}")

# Save trained model
with open("outputs/SalaryPred.model", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved as outputs/SalaryPred.model")

# Plot regression line
plt.figure(figsize=(8, 5))
plt.scatter(features, label, label="Actual Salary")
plt.plot(features, model.predict(features), color="red", label="Regression Line")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression - Experience vs Salary")
plt.legend()
plt.savefig("outputs/17b_linear_regression.png", bbox_inches="tight")
plt.close()

# Save predictions
predictions = pd.DataFrame({
    "YearsExperience": features.flatten(),
    "ActualSalary": label.flatten(),
    "PredictedSalary": model.predict(features).flatten()
})
predictions.to_csv("outputs/17b_predictions.csv", index=False)

print("\nRegression graph and predictions saved.")

