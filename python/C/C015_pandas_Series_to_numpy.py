# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html

import pandas as pd
import numpy as np

# to_numpy
# 이 시리즈 또는 인덱스의 값을 나타내는 NumPy ndarray



ser = pd.Series(pd.Categorical(['a', 'b', 'a']))
print(ser.to_numpy())
# ['a' 'b' 'a']
print(ser.to_numpy().dtype)
# object



# 날짜/시간 인식 데이터가 표시되는 방식을 제어 하려면 dtype 을 지정해야함 . 
ser = pd.Series(pd.date_range('2000', periods=2, tz="CET"))
print(ser.to_numpy(dtype=object))
# [Timestamp('2000-01-01 00:00:00+0100', tz='CET', freq='D')
#  Timestamp('2000-01-02 00:00:00+0100', tz='CET', freq='D')]
print(ser.to_numpy(dtype=object).dtype)
# object


print(ser.to_numpy(dtype="datetime64[ns]"))
# ['1999-12-31T23:00:00.000000000' '2000-01-01T23:00:00.000000000']
print(ser.to_numpy(dtype="datetime64[ns]").dtype)
# datetime64[ns]
