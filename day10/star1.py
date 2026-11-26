import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
avg_ball = df.groupby("Группа")["Баллы"].mean().reset_index()
avg_att = df.groupby("Группа")["Посещено"].mean().reset_index()
plt.bar(avg_ball["Группа"], avg_ball["Баллы"])
plt.title("Средний балл")
plt.savefig("star1_scores.png")
plt.close()
plt.bar(avg_att["Группа"], avg_att["Посещено"])
plt.title("Средняя посещаемость")
plt.savefig("star1_attendance.png")
plt.close()
print("Два графика сохранены")
