import numpy as np
scores = np.array([[45, 67, 82], [91, 53, 74]])
avg = np.mean(scores)
print("Среднее:", avg)
print(scores[scores < avg])