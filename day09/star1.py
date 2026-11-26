import pandas as pd
df = pd.read_csv("students.csv")
avg = df["Баллы"].mean()
result = df[df["Баллы"] > avg]
print("Среднее:", avg)
print(result)