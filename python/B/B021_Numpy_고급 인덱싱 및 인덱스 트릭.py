import numpy as np


# 부울 배열로 인덱싱

a = np.arange(12).reshape(3, 4)
b1 = np.array([False, True, True])         
b2 = np.array([True, False, True, False])  

print(a[b1, :])                                   # 행 선택
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[b1])                                      # 위와 같음
# [[ 4  5  6  7]
#  [ 8  9 10 11]]

print(a[:, b2])                                   # 열 선택
# [[ 0  2]
#  [ 4  6]
#  [ 8 10]]

print(a[b1, b2])                                  
# [ 4 10]