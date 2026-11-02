import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("EXPERIMENT 10c - ARRAY SLICING")

print("\nOriginal Array:")
print(arr)

print("\nElement at [1,1]:")
print(arr[1, 1])

print("\nFirst Row:")
print(arr[0, :])

print("\nFirst Two Rows:")
print(arr[0:2, :])

print("\nLast Column:")
print(arr[:, 2])

print("\nSelected Elements:")
print(arr[1:3, 1:3])
