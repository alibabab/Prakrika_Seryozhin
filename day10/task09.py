import pandas as pd
df = pd.read_csv("students.csv")
result = df.groupby("Группа")["Баллы"].mean().reset_index()
result.to_csv("average_by_group.csv", index=False, encoding="utf-8")
print(result)