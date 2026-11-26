import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
result = df.groupby("Группа")["Посещено"].mean().reset_index()
plt.bar(result["Группа"], result["Посещено"])
plt.title("Средняя посещаемость по группам")
plt.xlabel("Группа")
plt.ylabel("Посещено")
plt.savefig("task16_attendance.png")
plt.close()
print(result)