import numpy as np
temps = np.array([
[18, 20, 22, 19, 21],
[15, 17, 25, 23, 16],
[19, 21, 18, 24, 20]
])
print("Среднее по дням:", np.mean(temps, axis=1))
print("Среднее по столбцам:", np.mean(temps, axis=0))
avg = np.mean(temps)
print("Выше среднего:", temps[temps > avg])