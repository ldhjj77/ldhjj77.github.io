# 참조(to_list) - https://pydole.tistory.com/entry/%EC%9E%91%EC%84%B1%EC%A4%91
# 참조(get) - https://www.geeksforgeeks.org/python-pandas-series-get/

import pandas as pd
import numpy as np

# to_list
# 값 목록을 반환

# Series.get
# 주어진 키(DataFrame 열, 패널 슬라이스 등)에 대한 개체에서 항목을 가져옵



df = pd.DataFrame(['a', 'b', 'c', 1, 2, 3])
print(df)
#    0
# 0  a
# 1  b
# 2  c
# 3  1
# 4  2
# 5  3

print(np.array(df[0].to_list()))
# ['a' 'b' 'c' '1' '2' '3']





# Series.get
# 시리즈생성
sr = pd.Series(['New York', 'Chicago', 'Toronto', None, 'Rio'])
index_ = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5'] 
sr.index = index_
print(sr)
# City 1    New York
# City 2     Chicago
# City 3     Toronto
# City 4        None
# City 5         Rio
# dtype: object


# 주어진 시리즈 객체에서 전달된 인덱스 레이블의 값을 반환
result = sr.get(key = 'City 3')
print(result)
# Toronto


# 시리즈생성
sr = pd.Series([11, 21, 8, 18, 65, 84, 32, 10, 5, 24, 32])
index_ = pd.date_range('2010-10-09', periods = 11, freq ='M')
sr.index = index_
print(sr)
# 2010-10-31    11
# 2010-11-30    21
# 2010-12-31     8
# 2011-01-31    18
# 2011-02-28    65
# 2011-03-31    84
# 2011-04-30    32
# 2011-05-31    10
# 2011-06-30     5
# 2011-07-31    24
# 2011-08-31    32
# Freq: M, dtype: int64



# 주어진 시리즈 객체에서 전달된 인덱스 레이블의 값을 반환
result = sr.get(key = '2011-03-31')
print(result)
84


