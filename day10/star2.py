import pandas as pd
df = pd.read_csv("students.csv")
df["Статус"] = ["зачёт" if b >= 60 else "незачёт" for b in df["Баллы"]]
result = df.groupby(["Группа", "Статус"])["Баллы"].mean()
print(result)
