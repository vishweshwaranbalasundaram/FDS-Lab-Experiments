import matplotlib.pyplot as plt

names = ["SHREE", "DEV", "KEERTHI", "PRIYA", "SHAN", "KUMARAN"]
percentage = [96, 91, 94, 75, 45, 81]

print("COMPARISON OF HSC PERCENTAGE")
for name, mark in zip(names, percentage):
    print(name, ":", mark, "%")

plt.figure(figsize=(10, 6))
plt.bar(names, percentage)
plt.xlabel("Names of Pupil")
plt.ylabel("Percentage")
plt.title("Comparison of HSC Percentage", fontsize=20, color="green")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/3b_bar_chart.png")
plt.show()
