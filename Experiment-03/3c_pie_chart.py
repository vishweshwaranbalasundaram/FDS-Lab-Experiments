import matplotlib.pyplot as plt

labels = ["CANDIDATE 1", "CANDIDATE 2", "CANDIDATE 3", "CANDIDATE 4"]
votes = [315, 130, 245, 210]

print("ELECTION RESULTS")
for candidate, vote in zip(labels, votes):
    print(candidate, ":", vote, "votes")

plt.figure(figsize=(8, 6))
plt.pie(votes, labels=labels, autopct="%0.2f%%",
        explode=(0.2, 0, 0, 0))
plt.title("Election Results")
plt.tight_layout()
plt.savefig("outputs/3c_pie_chart.png")
plt.show()
