import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv("data/Social_Network_Ads.csv")

features = df.iloc[:, [2, 3]].values
label = df.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(
    features, label, test_size=0.2, random_state=37
)

model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

print("LOGISTIC REGRESSION MODEL")
print("\nTraining Accuracy:", model.score(x_train, y_train))
print("Testing Accuracy:", model.score(x_test, y_test))
print("\nCONFUSION MATRIX")
print(confusion_matrix(y_test, model.predict(x_test)))
print("\nCLASSIFICATION REPORT")
print(classification_report(y_test, model.predict(x_test), zero_division=0))

joblib.dump(model, "outputs/logistic_regression_model.pkl")
print("Model saved successfully!")
