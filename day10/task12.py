import matplotlib.pyplot as plt
cats = ["A", "B", "C"]
vals = [15, 25, 20]
plt.bar(cats, vals)
plt.savefig("task12_bar.png")
plt.close()