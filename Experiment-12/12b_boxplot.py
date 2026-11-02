import matplotlib.pyplot as plt
import seaborn as sns

data = [
    27, 50, 44, 6, 58, 61, 23, 86,
    67, 20, 75, 7, 79, 61, 90, 54, 250
]

print("EXPERIMENT 12b - BOXPLOT VISUALIZATION")
print("Dataset:", data)

plt.figure(figsize=(9, 5))
sns.boxplot(x=data)

plt.title("Outlier Detection using Boxplot")
plt.xlabel("Values")
plt.tight_layout()

plt.savefig("outputs/12b_boxplot.png")
plt.show()
