# 참조(at) - https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html
# 참조(iat) - https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html

import pandas as pd
import numpy as np

# Series.at / Series.iat

# Series.at
# 행 / 열 레이블 쌍의 단일 값에 액세스

# Series.iat
# 정수 위치로 행 / 열 쌍의 단일 값에 액세스






# Series.at
# 데이터프레임 생성
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  index=[4, 5, 6], columns=['A', 'B', 'C'])
print(df)
#     A   B   C
# 4   0   2   3
# 5   0   4   1
# 6  10  20  30

# 지정된 행 / 열 쌍에서 값 가져 오기
print(df.at[4, 'B'])
# 2

# 지정된 행 / 열 쌍에서 값 설정
df.at[4, 'B'] = 10
print(df.at[4, 'B'])
# 10

# 시리즈 내에서 가치 얻기
print(df.loc[5].at['B'])
# 4




# Series.iat
# 데이터프레임 생성
df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
                  columns=['A', 'B', 'C'])
print(df)
#     A   B   C
# 0   0   2   3
# 1   0   4   1
# 2  10  20  30

# 지정된 행/열 쌍에서 값 가져오기
print(df.iat[1, 2])
# 1

# 지정된 행/열 쌍에 값 설정
df.iat[1, 2] = 10
print(df.iat[1, 2])
# 10

# 시리즈 내에서 가치 얻기
print(df.loc[0].iat[1])
# 2


