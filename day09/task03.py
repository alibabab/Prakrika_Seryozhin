import pandas as pd
df = pd.read_csv("students.csv")
print("shape:", df.shape)
print("columns:", df.columns.tolist())
print("dtypes:")
print(df.dtypes)
print("info:")
df.info()