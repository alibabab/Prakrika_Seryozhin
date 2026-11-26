import pandas as pd
data = {
    "Имя": ["Анна", "Иван"],
    "Баллы": [80, 90]
}
df = pd.DataFrame(data)
result = df[df["Баллы"] == 80]
print(result)