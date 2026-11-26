import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
print(df.head())

result = df.groupby("Группа")["Баллы"].mean().reset_index()
result = result.sort_values("Баллы", ascending=False)
print(result)

result.to_csv("group_result.csv", index=False, encoding="utf-8")

plt.bar(result["Группа"], result["Баллы"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("chart.png")
plt.close()
print("Готово")
