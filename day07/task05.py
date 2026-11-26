import numpy as np
a = np.array([
[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120]
])
a[1, 2] = 999
print(a)