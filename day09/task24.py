import pandas as pd
df = pd.read_csv("students.csv")
df.to_csv("all_students_result.csv", index=False, encoding="utf-8")
print("Сохранено в all_students_result.csv")