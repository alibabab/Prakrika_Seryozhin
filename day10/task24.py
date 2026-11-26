import matplotlib.pyplot as plt
groups = ["A", "B", "C"]
scores = [10, 20, 15]
plt.bar(groups, scores)
plt.savefig("task24_fixed.png")
plt.close()