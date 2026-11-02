import numpy as np
from scipy.stats import norm

sample = np.array([
    54, 56, 53, 55, 57,
    52, 56, 55, 54, 58,
    53, 57, 56, 55, 54
])

population_mean = 50
population_std = 6

n = len(sample)
sample_mean = np.mean(sample)

z_score = (
    sample_mean - population_mean
) / (population_std / np.sqrt(n))

p_value = 1 - norm.cdf(z_score)

print("EXPERIMENT 8b - RIGHT TAILED Z TEST")
print("H0: Population mean = 50")
print("H1: Population mean > 50")

print("\nSample Mean:", round(sample_mean, 3))
print("Z Score:", round(z_score, 4))
print("P Value:", round(p_value, 4))

if p_value < 0.05:
    print("\nReject Null Hypothesis")
else:
    print("\nFail to Reject Null Hypothesis")
