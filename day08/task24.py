import pandas as pd
data = {
    "Имя": ["Анна", "Иван", "Олег"],
    "Баллы": [85, 72, 91]
}
df = pd.DataFrame(data)
df["Посещено занятий"] = [18, 15, 20]
print(df)