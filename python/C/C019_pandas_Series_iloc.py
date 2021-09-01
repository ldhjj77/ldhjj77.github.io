# 참조 - https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html

import pandas as pd
import numpy as np

# iloc


# Series.iloc
# 위치별 선택을 위한 순수한 정수 위치 기반 인덱싱.


# 데이터프레임 생성
mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
          {'a': 100, 'b': 200, 'c': 300, 'd': 400},
          {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
df = pd.DataFrame(mydict)
print(df)
#       a     b     c     d
# 0     1     2     3     4
# 1   100   200   300   400
# 2  1000  2000  3000  4000


# 행만 인덱싱. 스칼라 정수로
print(type(df.iloc[0]))
# <class 'pandas.core.series.Series'>
print(df.iloc[0])
# a    1
# b    2
# c    3
# d    4
# Name: 0, dtype: int64


# 정수 목록 포함
print(df.iloc[[0]])
#    a  b  c  d
# 0  1  2  3  4
print(type(df.iloc[[0]]))
# <class 'pandas.core.frame.DataFrame'>


print(df.iloc[[0, 1]])
#      a    b    c    d
# 0    1    2    3    4
# 1  100  200  300  400


# A를 슬라이스 객체입니다.
print(df.iloc[:3])
#       a     b     c     d
# 0     1     2     3     4
# 1   100   200   300   400
# 2  1000  2000  3000  4000


# 인덱스와 길이가 같은 부울 마스크를 사용
print(df.iloc[[True, False, True]])
#       a     b     c     d
# 0     1     2     3     4
# 2  1000  2000  3000  4000


# 콜러블을 사용하여 메서드 체인에 유용함. 전달 된 xlambda 는 슬라이스되는 DataFrame. 인덱스 레이블이 짝수인 행을 선택
print(df.iloc[lambda x: x.index % 2 == 0])
#       a     b     c     d
# 0     1     2     3     4
# 2  1000  2000  3000  4000




# 두 축 모두 인덱싱
# 인덱스와 열에 대한 인덱서 유형을 혼합. 전체 축을 선택하는 데 사용 함.
 
# 스칼라 정수
print(df.iloc[0, 1])
# 2

# 정수 목록 포함
print(df.iloc[[0, 2], [1, 3]])
#       b     d
# 0     2     4
# 2  2000  4000


# 슬라이스 개체 와 함께
print(df.iloc[1:3, 0:3])
#       a     b     c
# 1   100   200   300
# 2  1000  2000  3000


# 길이가 열과 일치하는 부울 배열을 사용
print(df.iloc[:, [True, False, True, False]])
#       a     c
# 0     1     3
# 1   100   300
# 2  1000  3000


# Series 또는 DataFrame을 예상하는 호출 가능한 함수를 사용
print(df.iloc[:, lambda df: [0, 2]])
#       a     c
# 0     1     3
# 1   100   300
# 2  1000  3000


