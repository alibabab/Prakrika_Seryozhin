import pandas as pd
df = pd.read_csv("students.csv")
print("Первые 3:")
print(df.head(3))
print("Последние 2:")
print(df.tail(2))