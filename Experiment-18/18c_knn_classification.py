import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

df = pd.read_csv("data/Iris.csv")
features = df.iloc[:, :-1].values
label = df.iloc[:, 4].values

xtrain, xtest, ytrain, ytest = train_test_split(
    features, label, test_size=0.2, random_state=42, stratify=label
)

model_KNN = KNeighborsClassifier(n_neighbors=5)
model_KNN.fit(xtrain, ytrain)

print("K-NEAREST NEIGHBORS CLASSIFICATION")
print("\nTraining Accuracy:", model_KNN.score(xtrain, ytrain))
print("Testing Accuracy:", model_KNN.score(xtest, ytest))
print("\nTest Set Accuracy:", accuracy_score(ytest, model_KNN.predict(xtest)))
print("\nCONFUSION MATRIX")
print(confusion_matrix(ytest, model_KNN.predict(xtest), labels=["Setosa","Versicolor","Virginica"]))
print("\nCLASSIFICATION REPORT")
print(classification_report(ytest, model_KNN.predict(xtest), zero_division=0))

import joblib
joblib.dump(model_KNN, "outputs/knn_iris_model.pkl")
print("Model saved to outputs/knn_iris_model.pkl")
