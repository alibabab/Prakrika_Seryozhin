import pandas as pd
data = {
    "Имя": ["Анна", "Иван", "Олег", "Мария"],
    "Баллы": [85, 72, 91, 64]
}
df = pd.DataFrame(data)
average = df["Баллы"].mean()
result = df[df["Баллы"] > average]
print("Среднее:", average)
print(result)