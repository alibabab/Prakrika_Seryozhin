import numpy as np
data = np.array([[45, 67, 82], [91, 53, 74]])
new_data = data.copy()
new_data[new_data < 60] = new_data[new_data < 60] + 10
print(data)
print(new_data)