import numpy as np
groups = np.array([
[70, 80, 90, 60, 75],
[55, 75, 85, 95, 65]
])
print("Среднее по группам:", np.mean(groups, axis=1))
print("Среднее по заданиям:", np.mean(groups, axis=0))
print("Мин:", np.min(groups))
print("Макс:", np.max(groups))