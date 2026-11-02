import numpy as np

data = np.array([
    27, 50, 44, 6, 58, 61, 23, 86,
    67, 20, 75, 7, 79, 61, 90, 54, 250
])

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = data[
    (data < lower_limit) | (data > upper_limit)
]

print("EXPERIMENT 12a - IQR OUTLIER DETECTION")
print("\nOriginal Data:", data)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Detected Outliers:", outliers)
