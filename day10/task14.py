import matplotlib.pyplot as plt
cats = ["A", "B", "C"]
vals = [15, 25, 20]
plt.bar(cats, vals)
plt.title("Пример диаграммы")
plt.xlabel("Категория")
plt.ylabel("Значение")
plt.grid()
plt.savefig("task14_bar.png")
plt.close()