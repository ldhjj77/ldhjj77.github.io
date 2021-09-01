# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html

import pandas as pd
import numpy as np

# astype
# pandas 객체를 지정된 dtype으로 캐스팅


# 데이터 프레임 생성
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
print(df.dtypes)
# col1    int64
# col2    int64
# dtype: object


# 모든 열을 int32로 캐스트
print(df.astype('int32').dtypes)
# col1    int32
# col2    int32
# dtype: object


# 사전을 사용하여 col1을 int32로 캐스트
print(df.astype({'col1': 'int32'}).dtypes)
# col1    int32
# col2    int64
# dtype: object


# 시리즈 만들기
ser = pd.Series([1, 2], dtype='int32')
print(ser)
# 0    1
# 1    2
# dtype: int32

print(ser.astype('int64'))
# 0    1
# 1    2
# dtype: int64


# 범주형으로 변환
print(ser.astype('category'))
# 0    1
# 1    2
# dtype: category
# Categories (2, int64): [1, 2]


# 사용자 지정 순서를 사용하여 정렬된 범주 유형으로 변환
from pandas.api.types import CategoricalDtype
cat_dtype = CategoricalDtype(
    categories=[2, 1], ordered=True)
print(ser.astype(cat_dtype))
# 0    1
# 1    2
# dtype: category
# Categories (2, int64): [2 < 1]


# copy=False 새 pandas 객체에서 데이터를 사용하고 변경하면 변경 사항이 전파 될 수 있음
s1 = pd.Series([1, 2])
s2 = s1.astype('int64', copy=False)
s2[0] = 10
print(s1)  # s1[0]도 변경되었습니다.
# 0    10
# 1     2
# dtype: int64


# 일련의 날짜 만들기
ser_date = pd.Series(pd.date_range('20200101', periods=3))
print(ser_date)
# 0   2020-01-01
# 1   2020-01-02
# 2   2020-01-03
# dtype: datetime64[ns]