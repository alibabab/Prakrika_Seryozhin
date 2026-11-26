import numpy as np
data = np.array([[1, 2], [3, 4]])
print(data[1, 0])  # 3

data = np.array([[1, 2, 3], [4, 5, 6]])
print(data[:, 1])  # [2 5]

data = np.array([[10, 20], [30, 40]])
print(np.sum(data, axis=0))  # [40 60]

data = np.array([[10, 20], [30, 40]])
print(np.mean(data, axis=1))  # [15. 35.]

data = np.arange(1, 7).reshape(2, 3)
print(data)  # [[1 2 3] [4 5 6]]