import pandas as pd
df = pd.read_csv("students_missing.csv")
avg_ball = df["Баллы"].mean()
df["Баллы"] = df["Баллы"].fillna(avg_ball)
df["Посещено"] = df["Посещено"].fillna(0)
df.to_csv("clean_full.csv", index=False, encoding="utf-8")
filtered = df[df["Баллы"] >= 70]
filtered.to_csv("filtered_only.csv", index=False, encoding="utf-8")
print("Сохранены clean_full.csv и filtered_only.csv")