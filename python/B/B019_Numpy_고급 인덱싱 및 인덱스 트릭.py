import numpy as np

# 인덱스 배열로 인덱싱


a = np.arange(5)
print(a)
# [0 1 2 3 4]

a[[1, 3, 4]] = 0
print(a)
# [0 0 2 0 0]


a = np.arange(5)
a[[0, 0, 2]] = [1, 2, 3]
print(a)
# [2 1 3 3 4]


a = np.arange(5)
a[[0, 0, 2]] += 1
print(a)
# [1 1 3 3 4]