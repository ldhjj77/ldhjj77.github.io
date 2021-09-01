# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html

import pandas as pd
import numpy as np

# convert_dtypes
# Series (또는 DataFrame의 각 series)를 pd.NA를 지원하는 dtype으로 변환해줌
# pandas 1.0.0 이상에서 사용가능

# 기본 dtypes가 있는 DataFrame으로 시작.
df = pd.DataFrame(
    {
        "a": pd.Series([1, 2, 3], dtype=np.dtype("int32")),
        "b": pd.Series(["x", "y", "z"], dtype=np.dtype("O")),
        "c": pd.Series([True, False, np.nan], dtype=np.dtype("O")),
        "d": pd.Series(["h", "i", np.nan], dtype=np.dtype("O")),
        "e": pd.Series([10, np.nan, 20], dtype=np.dtype("float")),
        "f": pd.Series([np.nan, 100.5, 200], dtype=np.dtype("float")),
    }
)

print(df)
#    a  b      c    d     e      f
# 0  1  x   True    h  10.0    NaN
# 1  2  y  False    i   NaN  100.5
# 2  3  z    NaN  NaN  20.0  200.0

print(df.dtypes)
# a      int32
# b     object
# c     object
# d     object
# e    float64
# f    float64
# dtype: object


# 가능한 최상의 dtypes를 사용하도록 DataFrame을 변환
dfn = df.convert_dtypes()
print(dfn)
#    a  b      c     d     e      f
# 0  1  x   True     h    10   <NA>
# 1  2  y  False     i  <NA>  100.5
# 2  3  z   <NA>  <NA>    20  200.0

print(dfn.dtypes)
# a      Int32
# b     string
# c    boolean
# d     string
# e      Int64
# f    Float64
# dtype: object

#  np.nan으로 표시되는 일련의 문자열 및 누락된 데이터로 시작
s = pd.Series(["a", "b", np.nan])
print(s)
# 0      a
# 1      b
# 2    NaN
# dtype: object

# dtype 으로 시리즈를 얻음 StringDtype.
print(s.convert_dtypes())
# 0       a
# 1       b
# 2    <NA>
# dtype: string
