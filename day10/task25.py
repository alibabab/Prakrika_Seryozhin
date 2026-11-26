import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
stats = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"]).reset_index()
print(stats)
stats.to_csv("task25_stats.csv", index=False, encoding="utf-8")
plt.bar(stats["Группа"], stats["mean"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("task25_chart.png")
plt.close()