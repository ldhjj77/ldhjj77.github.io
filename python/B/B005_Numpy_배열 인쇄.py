import numpy as np

# 배열 인쇄

a = np.arange(6)                    # 1d array
print(a)
# [0 1 2 3 4 5]

b = np.arange(12).reshape(4, 3)     # 2d array
print(b)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]


c = np.arange(24).reshape(2, 3, 4)  # 3d array
print(c)
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]

#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]


print(np.arange(10000))
# [   0    1    2 ... 9997 9998 9999]



print(np.arange(10000).reshape(100, 100))
# [[   0    1    2 ...   97   98   99]
#  [ 100  101  102 ...  197  198  199]
#  [ 200  201  202 ...  297  298  299]
#  ...
#  [9700 9701 9702 ... 9797 9798 9799]
#  [9800 9801 9802 ... 9897 9898 9899]
#  [9900 9901 9902 ... 9997 9998 9999]]

import sys
np.set_printoptions(threshold=sys.maxsize)  
# 출력량이 많아서 중간을 생략한 부분을 강제로 모두 출력하도록 하는 명령어



