import pandas as pd
df = pd.read_csv("students.csv")
print(df[(df["Баллы"] >= 75) & (df["Посещено"] >= 16)])