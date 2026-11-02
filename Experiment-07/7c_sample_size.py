import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

population = np.random.normal(50, 10, 10000)

sample_sizes = [10, 30, 50, 100]
number_of_samples = 500

print("EXPERIMENT 7c - EFFECT OF SAMPLE SIZE")

plt.figure(figsize=(10, 6))

for size in sample_sizes:

    sample_means = []

    for i in range(number_of_samples):
        sample = np.random.choice(
            population,
            size=size,
            replace=False
        )
        sample_means.append(np.mean(sample))

    print(
        "Sample size:", size,
        "| Mean:", round(np.mean(sample_means), 3),
        "| Standard deviation:", round(np.std(sample_means), 3)
    )

    plt.hist(
        sample_means,
        bins=30,
        alpha=0.45,
        label=f"Sample Size {size}"
    )

plt.title("Effect of Sample Size on Sampling Distribution")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()

plt.savefig("outputs/7c_sample_size_comparison.png")
plt.show()
