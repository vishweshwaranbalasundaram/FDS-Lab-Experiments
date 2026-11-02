import numpy as np
from scipy.stats import norm

sample = np.array([
    152, 148, 151, 149, 147,
    153, 150, 148, 152, 149,
    151, 150, 149, 152, 151,
    148, 150, 152, 149, 150,
    148, 153, 151, 150, 149,
    152, 148, 151, 150, 153
])

population_mean = 150
population_std = 5
sample_size = len(sample)

sample_mean = np.mean(sample)

z_score = (
    sample_mean - population_mean
) / (population_std / np.sqrt(sample_size))

p_value = 2 * (1 - norm.cdf(abs(z_score)))

print("EXPERIMENT 8a - ONE SAMPLE Z TEST")
print("Null Hypothesis: Population mean = 150")
print("Alternative Hypothesis: Population mean != 150")

print("\nSample Size:", sample_size)
print("Sample Mean:", round(sample_mean, 3))
print("Population Mean:", population_mean)
print("Z Score:", round(z_score, 4))
print("P Value:", round(p_value, 4))

alpha = 0.05

if p_value < alpha:
    print("\nReject Null Hypothesis")
else:
    print("\nFail to Reject Null Hypothesis")
