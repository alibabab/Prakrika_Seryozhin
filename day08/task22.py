import pandas as pd
data = {
    "Имя": ["Анна", "Иван", "Олег"],
    "Баллы": [85, 72, 91]
}
df = pd.DataFrame(data)
df["Баллы"] = df["Баллы"] + 3
print(df)