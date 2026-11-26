import numpy as np
scores = np.array([
[70, 80, 90, 60, 75],
[55, 75, 85, 95, 65],
[88, 62, 71, 80, 50]
])
print("1. Исходная таблица:")
print(scores)
print("2. shape:", scores.shape)
print("ndim:", scores.ndim)
print("size:", scores.size)
print("3. Общее среднее:", np.mean(scores))
print("4. Среднее каждой группы:", np.mean(scores, axis=1))
print("5. Среднее каждого задания:", np.mean(scores, axis=0))
print("6. Мин:", np.min(scores), "Макс:", np.max(scores))
print("7. Значения 60 и выше:", scores[scores >= 60])
print("8. Ниже среднего:", scores[scores < np.mean(scores)])
print("9. Первая строка:", scores[0])
print("10. Последний столбец:", scores[:, -1])
print("11. Фрагмент 2 на 2:")
print(scores[0:2, 0:2])
scores[1, 3] = 77
print("12. После изменения:")
print(scores)
new_scores = scores + 5
print("13. Плюс 5:")
print(new_scores)
print("14. Новое среднее:", np.mean(new_scores))