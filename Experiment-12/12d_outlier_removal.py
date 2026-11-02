import numpy as np

data = np.array([
    27, 50, 44, 6, 58, 61, 23, 86,
    67, 20, 75, 7, 79, 61, 90, 54, 250
])

Q1 = np.percentile(data, 25)
Q3 = np.percentile(data, 75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

cleaned_data = data[
    (data >= lower) & (data <= upper)
]

print("EXPERIMENT 12d - OUTLIER REMOVAL")
print("\nOriginal Data:", data)
print("Original Size:", len(data))
print("\nCleaned Data:", cleaned_data)
print("Cleaned Size:", len(cleaned_data))
