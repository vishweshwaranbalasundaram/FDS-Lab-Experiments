import joblib
import numpy as np

model = joblib.load("outputs/knn_iris_model.pkl")

sample = np.array([[5.1, 3.5, 1.4, 0.2]])

prediction = model.predict(sample)

print("FLOWER MEASUREMENTS:", sample.tolist()[0])
print("PREDICTED IRIS VARIETY:", prediction[0])
