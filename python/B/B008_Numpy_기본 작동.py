import numpy as np

# 기본 작동

rg = np.random.default_rng(1)  # create instance of default random number generator
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
print(a)
# [[3 3 3]
#  [3 3 3]]

b += a
print(b)
# [[3.51182162 3.9504637  3.14415961]
#  [3.94864945 3.31183145 3.42332645]]

# a += b  
# print(a)     해당 코드는 b는 정수형으로 자동 변환되지 않기때문에 에러가남

