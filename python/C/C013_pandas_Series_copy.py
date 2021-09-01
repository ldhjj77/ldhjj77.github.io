# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.copy.html

import pandas as pd
import numpy as np

# copy
# 이 개체의 인덱스와 데이터를 복사


s = pd.Series([1, 2], index=["a", "b"])
print(s)
# a    1
# b    2
# dtype: int64

s_copy = s.copy()
print(s_copy)
# a    1
# b    2
# dtype: int64


# 얕은 복사 대 기본(깊은) 복사
s = pd.Series([1, 2], index=["a", "b"])
deep = s.copy()
shallow = s.copy(deep=False)

# 얕은 사본은 원본과 데이터 및 색인을 공유
print(s is shallow)
# False

print(s.values is shallow.values and s.index is shallow.index)
# True

print(s is deep)
# False

print(s.values is deep.values or s.index is deep.index)
# False


# 얕은 사본과 원본이 공유하는 데이터에 대한 업데이트는 둘 다에 반영. 
# 깊은 복사는 변경되지 않은 상태로 유지.
s[0] = 3
shallow[1] = 4
print(s)
# a    3
# b    4
# dtype: int64

print(shallow)
# a    3
# b    4
# dtype: int64

print(deep)
# a    1
# b    2
# dtype: int64


# Python 객체가 포함된 객체를 복사할 때 전체 복사는 데이터를 복사하지만 재귀적으로 복사하지는 않음. 
# 중첩된 데이터 개체를 업데이트하면 전체 복사본에 반영
s = pd.Series([[1, 2], [3, 4]])
deep = s.copy()
s[0][0] = 10
print(s)
# 0    [10, 2]
# 1     [3, 4]
# dtype: object

print(deep)
# 0    [10, 2]
# 1     [3, 4]
# dtype: object

