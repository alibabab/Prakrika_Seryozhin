import pandas as pd
df = pd.read_csv("results.csv")
print("Структура:")
print("shape:", df.shape)
print(df.dtypes)
df.info()
df["Процент посещаемости"] = (df["Посещено"] / 20 * 100).round(1)
result = df[df["Баллы"] >= 70]
result = result.sort_values("Баллы", ascending=False)
print("Отфильтровано:")
print(result)
result.to_csv("results_filtered.csv", index=False, encoding="utf-8")
print("Сохранено в results_filtered.csv")