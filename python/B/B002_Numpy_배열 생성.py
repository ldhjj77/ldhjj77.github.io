import numpy as np

# 배열 생성


a = np.array([2, 3, 4])
a
print(a)
# [2, 3, 4]
print(a.dtype)
# int64

b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b.dtype)
# float64
print(b)
# [[1.5 2.  3. ]
#  [4.  5.  6. ]]

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
# [[1.+0.j 2.+0.j]
#  [3.+0.j 4.+0.j]]


