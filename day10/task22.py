import pandas as pd
df = pd.read_csv("students.csv")
result = df.groupby("Группа")["Баллы"].agg(["mean", "min", "max"])
print(result)