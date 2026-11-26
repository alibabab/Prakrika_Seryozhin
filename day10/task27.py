import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Группа": ["1ИИ-1","1ИИ-1","1ИИ-1","1ИИ-1","1ИИ-1","1ИИ-2","1ИИ-2","1ИИ-2","1ИИ-2","1ИИ-2"],
    "Имя": ["Анна","Иван","Сергей","Пётр","Наталья","Олег","Мария","Ирина","Елена","Артём"],
    "Тест1": [80, 65, 70, 55, 78, 90, 60, 85, 95, 68],
    "Тест2": [75, 70, 72, 50, 82, 88, 58, 80, 92, 71]
}
df = pd.DataFrame(data)
print(df)
avg = df.groupby("Группа")[["Тест1", "Тест2"]].mean()
print("Средние:")
print(avg)
print("Мин:")
print(df.groupby("Группа")[["Тест1", "Тест2"]].min())
print("Макс:")
print(df.groupby("Группа")[["Тест1", "Тест2"]].max())
avg.reset_index().to_csv("task27_tests.csv", index=False, encoding="utf-8")
avg_plot = avg.reset_index()
plt.bar(avg_plot["Группа"], avg_plot["Тест1"])
plt.title("Средний Тест1 по группам")
plt.xlabel("Группа")
plt.ylabel("Балл")
plt.savefig("task27_chart.png")
plt.close()