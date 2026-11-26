import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Имя": ["Анна","Иван","Олег","Мария","Сергей"],
    "Тест1": [80, 65, 90, 60, 70],
    "Тест2": [75, 70, 88, 58, 72]
}
df = pd.DataFrame(data)
plt.plot(df["Имя"], df["Тест1"], marker="o", label="Тест1")
plt.plot(df["Имя"], df["Тест2"], marker="s", label="Тест2")
plt.title("Сравнение тестов")
plt.xlabel("Студент")
plt.ylabel("Балл")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("star3_tests.png")
plt.close()
print("График с легендой сохранён")
