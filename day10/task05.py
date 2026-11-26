import pandas as pd
df = pd.read_csv("students.csv")
print(df.groupby("Группа")["Баллы"].agg(["mean", "min", "max", "count"]))
