import numpy as np

arr = np.arange(1, 10)

print("EXPERIMENT 10b - RESHAPE AND RAVEL")
print("\nOriginal Array:")
print(arr)

reshaped = arr.reshape(3, 3)

print("\nReshaped Array:")
print(reshaped)

print("\nRavelled Array:")
print(reshaped.ravel())
