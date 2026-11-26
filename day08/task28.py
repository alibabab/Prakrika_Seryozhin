import pandas as pd
data = {
    "Имя": ["Анна", "Иван", "Олег"],
    "Баллы": [85, 72, 91]
}
df = pd.DataFrame(data)
result = df[(df["Баллы"] >= 70) & (df["Баллы"] <= 90)]
print(result)