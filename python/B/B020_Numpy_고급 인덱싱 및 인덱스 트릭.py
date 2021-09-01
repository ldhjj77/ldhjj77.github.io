import numpy as np

# 부울 배열로 인덱싱


a = np.arange(12).reshape(3, 4)
b = a > 4
print(b)  # `b` is a boolean with `a`'s shape
# [[False False False False]
#  [False  True  True  True]
#  [ True  True  True  True]]

print(a[b])  # 1d array with the selected elements
# [ 5  6  7  8  9 10 11]

a[b] = 0  # All elements of `a` higher than 4 become 0
print(a)
# [[0 1 2 3]
#  [4 0 0 0]
#  [0 0 0 0]]