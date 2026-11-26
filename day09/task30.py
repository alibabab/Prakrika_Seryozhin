import pandas as pd
df = pd.read_csv("products.csv")
print("Таблица:")
print(df)
df["Стоимость"] = df["Цена"] * df["Количество"]
df = df.sort_values("Стоимость", ascending=False)
print("По стоимости:")
print(df)
print("Цена выше 30:")
print(df[df["Цена"] > 30])
df.to_csv("products_result.csv", index=False, encoding="utf-8")
print("Сохранено в products_result.csv")