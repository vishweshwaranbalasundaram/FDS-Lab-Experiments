import numpy as np
import pandas as pd

np.random.seed(42)

population = np.random.normal(50, 10, 1000)

sample = np.random.choice(population, size=30, replace=False)

print("EXPERIMENT 7a - POPULATION AND RANDOM SAMPLING")

print("\nPopulation size:", len(population))
print("Sample size:", len(sample))

print("\nPopulation Mean:", np.mean(population))
print("Sample Mean:", np.mean(sample))

print("\nSelected Random Sample:")
print(sample)

pd.DataFrame({"Sample": sample}).to_csv(
    "data/random_sample.csv", index=False
)
