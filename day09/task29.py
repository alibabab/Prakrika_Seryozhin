import pandas as pd
df = pd.read_csv("students.csv")
df.to_csv("result.csv", index=False)
print("Сохранено")