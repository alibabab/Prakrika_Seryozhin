import pandas as pd
data = {
    "Имя": ["Анна", "Иван", "Олег"],
    "Баллы": [85, 72, 91]
}
df = pd.DataFrame(data)
print("Сумма:", df["Баллы"].sum())
print("Среднее:", df["Баллы"].mean())
print("Мин:", df["Баллы"].min())
print("Макс:", df["Баллы"].max())