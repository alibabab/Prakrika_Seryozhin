import pandas as pd
df = pd.read_csv("students.csv")
print(df.sort_values(["Группа", "Баллы"], ascending=[True, False]))