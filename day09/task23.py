import pandas as pd
df = pd.read_csv("students.csv")
df = df.rename(columns={"Баллы": "Тестовый балл"})
print(df)