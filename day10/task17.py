import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
plt.plot(df["Имя"], df["Баллы"])
plt.title("Баллы студентов")
plt.xlabel("Студент")
plt.ylabel("Баллы")
plt.savefig("task17_line.png")
plt.close()