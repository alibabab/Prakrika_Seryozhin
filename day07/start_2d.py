import numpy as np
numbers = np.array([10, 20, 30, 40])
print(numbers)
print(numbers.shape)
print(numbers.ndim)
data = np.array([
[10, 20, 30],
[40, 50, 60]
])
print(data)
print(data.ndim)
print(data.shape)
print(data.size)
print(data[0, 0])
print(data[1, 2])
print(data[0])
print(data[:, 1])