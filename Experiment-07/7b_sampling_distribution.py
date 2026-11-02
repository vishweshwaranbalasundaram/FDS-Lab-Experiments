import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.normal(50, 10, 10000)

sample_size = 30
number_of_samples = 1000

sample_means = []

for i in range(number_of_samples):
    sample = np.random.choice(
        population,
        size=sample_size,
        replace=False
    )
    sample_means.append(np.mean(sample))

print("EXPERIMENT 7b - SAMPLING DISTRIBUTION")

print("Number of samples:", number_of_samples)
print("Sample size:", sample_size)
print("Mean of sample means:", np.mean(sample_means))
print("Standard deviation:", np.std(sample_means))

plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, edgecolor="black")

plt.axvline(
    np.mean(sample_means),
    linestyle="dashed",
    label="Mean of Sample Means"
)

plt.title("Sampling Distribution of Sample Means")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()

plt.savefig("outputs/7b_sampling_distribution.png")
plt.show()
