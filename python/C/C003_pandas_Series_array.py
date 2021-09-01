# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html

import pandas as pd
import numpy as np

# array / T / dtype / shape / nbytes / ndim / size 

# 이 시리즈 또는 인덱스를 지원하는 데이터의 확장Array

# int 및 float와 같은 일반 NumPy 유형의 경우 PandasArray가 반환됩니다.
print(pd.Series([1, 2, 3]).array)
# <PandasArray>
# [1, 2, 3]
# Length: 3, dtype: int64

# Categorical과 같은 확장 유형의 경우 실제 ExtensionArray가 반환됩니다.
ser = pd.Series(pd.Categorical(['a', 'b', 'a']))
print(ser.array)
# ['a', 'b', 'a']
# Categories (2, object): ['a', 'b']


# T -> 정의상 self인 조옮김을 반환합니다.
print(ser.T)
# 0    a
# 1    b
# 2    a
# dtype: category
# Categories (2, object): ['a', 'b']



# dtype -> 기본 데이터의 dtype 객체를 반환
print(ser.dtype)
# category



# shape) -> 기본 데이터 모양의 튜플을 반환
print(ser.shape)
# (3,)



# nbytes -> 기본 데이터의 바이트 수를 반환
print(ser.nbytes)
# 19



# ndim -> 정의 1에 따른 기본 데이터의 차원 수
print(ser.ndim)
# 1



# size -> 기본 데이터의 요소 수를 반환
print(ser.size)
# 3


