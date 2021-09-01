import pandas as pd
import numpy as np

# 기본



# pandas.Series란?
# 축 레이블이 있는 1차원 ndarray(시계열 포함).

# ndarray는 Numpy의 핵심인 다차원 행렬 자료구조 클래스
# 파이썬이 제공하는 List 자료형과 동일한 출력 형태


# 지정된 인덱스를 사용하여 사전에서 시리즈 생성
d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['a', 'b', 'c'])
print(ser)
# a    1
# b    2
# c    3
# dtype: int64

# 사전의 키는 Index 값과 일치하므로 Index 값은 효과가 없습니다
d = {'a': 1, 'b': 2, 'c': 3}
ser = pd.Series(data=d, index=['x', 'y', 'z'])
print(ser)
# x   NaN
# y   NaN
# z   NaN
# dtype: float64


# copy = False 를 사용하여 목록에서 시리즈 생성 .
r = [1, 2]
ser = pd.Series(r, copy=False)
ser.iloc[0] = 999
print(r)
# [1, 2]

print(ser)
# 0    999
# 1      2
# dtype: int64


# copy = False 를 사용하여 1d ndarray에서 시리즈 생성 .
r = np.array([1, 2])
ser = pd.Series(r, copy=False)
ser.iloc[0] = 999
print(r)
# [999   2]

print(ser)
# 0    999
# 1      2
# dtype: int32