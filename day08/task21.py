import pandas as pd
data = {
    "Имя": ["Анна", "Иван", "Олег", "Мария"],
    "Баллы": [85, 72, 91, 64]
}
df = pd.DataFrame(data)
print("head:")
print(df.head())
print("tail:")
print(df.tail(2))
print("info:")
df.info()
print("describe:")
print(df.describe())