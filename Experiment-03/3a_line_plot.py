import matplotlib.pyplot as plt

overs = list(range(5, 51, 5))
india = [30, 55, 90, 129, 165, 200, 239, 270, 310, 350]
srilanka = [25, 70, 90, 120, 140, 170, 195, 220, 255, 279]

print("INDIA VS SRILANKA")
print("Overs:", overs)
print("India:", india)
print("Sri Lanka:", srilanka)

plt.figure(figsize=(10, 6))
plt.plot(overs, india, marker="o", label="INDIA")
plt.plot(overs, srilanka, marker="o", label="SRILANKA")
plt.title("INDIA Vs SRILANKA")
plt.xlabel("Overs")
plt.ylabel("Score")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/3a_line_plot.png")
plt.show()
