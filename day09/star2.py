import pandas as pd
df = pd.read_csv("students.csv")
result = df.sort_values(["Группа", "Баллы"], ascending=[True, False])
print(result)