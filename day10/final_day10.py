import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
print("1. Первые строки:")
print(df.head())
print("2. shape:", df.shape)
print("3. columns:", df.columns.tolist())
df.info()

print("4. mean min max count по баллам:")
stats = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"]).reset_index()
print(stats)

print("5. Средняя посещаемость:")
att = df.groupby("Группа")["Посещено"].mean().reset_index()
print(att)

result = stats.copy()
result = result.sort_values("mean", ascending=False)
print(result)

result.to_csv("group_summary.csv", index=False, encoding="utf-8")

plt.bar(result["Группа"], result["mean"])
plt.title("Средний балл по группам")
plt.xlabel("Группа")
plt.ylabel("Средний балл")
plt.grid()
plt.tight_layout()
plt.savefig("group_summary.png")
plt.close()