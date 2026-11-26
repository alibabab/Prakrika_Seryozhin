import numpy as np
scores = np.array([
[70, 80, 90, 60, 75],
[55, 75, 85, 95, 65],
[88, 62, 71, 80, 50]
])
means = np.mean(scores, axis=1)
print("Средние групп:", means)
print("Лучшее среднее:", np.max(means))