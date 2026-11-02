import numpy as np
from scipy.stats import zscore

data = np.array([
    27, 50, 44, 6, 58, 61, 23, 86,
    67, 20, 75, 7, 79, 61, 90, 54, 250
])

z_scores = zscore(data)

outliers = data[np.abs(z_scores) > 2]

print("EXPERIMENT 12c - Z SCORE METHOD")
print("\nOriginal Data:", data)
print("\nZ Scores:", np.round(z_scores, 3))
print("\nDetected Outliers:", outliers)
