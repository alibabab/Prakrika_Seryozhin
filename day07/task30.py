import numpy as np
sales = np.array([
[100, 150, 200, 80],
[120, 130, 180, 90],
[90, 160, 210, 70]
])
print("Общая сумма:", np.sum(sales))
print("Суммы по дням:", np.sum(sales, axis=1))
print("Суммы по товарам:", np.sum(sales, axis=0))
print("Среднее:", np.mean(sales))