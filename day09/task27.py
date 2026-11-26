import pandas as pd
df = pd.read_csv("students.csv")
result = df[(df["Баллы"] >= 80) & (df["Посещено"] >= 16)]
print(result)