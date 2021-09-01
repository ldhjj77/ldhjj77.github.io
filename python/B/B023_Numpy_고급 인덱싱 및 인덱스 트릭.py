import numpy as np

# "자동" 재형성


a = np.arange(30)
b = a.reshape((2, -1, 3))  # -1 means "whatever is needed"
print(b.shape)
# (2, 5, 3)

print(b)
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]
#   [ 9 10 11]
#   [12 13 14]]

#  [[15 16 17]
#   [18 19 20]
#   [21 22 23]
#   [24 25 26]
#   [27 28 29]]]




## 벡터 스태킹


x = np.arange(0, 10, 2)
y = np.arange(5)
m = np.vstack([x, y])
print(m)
# [[0 2 4 6 8]
#  [0 1 2 3 4]]

xy = np.hstack([x, y])
print(xy)
# [0 2 4 6 8 0 1 2 3 4]
