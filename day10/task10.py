import pandas as pd
df = pd.read_csv("students.csv")
result = df.groupby("Группа")["Посещено"].mean().reset_index()
result.to_csv("attendance_by_group.csv", index=False, encoding="utf-8")
print(result)