# 참조(loc) - https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html

import pandas as pd
import numpy as np

# loc

# Series.loc
# 레이블 또는 부울 배열로 행 및 열 그룹에 액세스





# Series.loc
# 데이터프레임 생성
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=['cobra', 'viper', 'sidewinder'],
     columns=['max_speed', 'shield'])
print(df)
#             max_speed  shield
# cobra               1       2
# viper               4       5
# sidewinder          7       8


# 단일 레이블. 이것은 행을 시리즈로 반환
print(df.loc['viper'])
# max_speed    4
# shield       5
# Name: viper, dtype: int64


# 레이블 목록. [[]] 사용 하면 DataFrame이 반환
print(df.loc[['viper', 'sidewinder']])
#             max_speed  shield
# viper               4       5
# sidewinder          7       8


# 행 및 열에 대한 단일 레이블
print(df.loc['cobra', 'shield'])
# 2


# 행에 대한 레이블과 열에 대한 단일 레이블이 있는 슬라이스. 슬라이스의 시작과 끝이 모두 포함
print(df.loc['cobra':'viper', 'max_speed'])
# cobra    1
# viper    4
# Name: max_speed, dtype: int64


# 행 축과 길이가 같은 부울 목록
print(df.loc[[False, False, True]])
#             max_speed  shield
# sidewinder          7       8


# 정렬 가능한 부울 시리즈
print(df.loc[pd.Series([False, True, False],
       index=['viper', 'sidewinder', 'cobra'])])
#             max_speed  shield
# sidewinder          7       8


# 인덱스(df.reindex와 동일한 동작)
print(df.loc[pd.Index(["cobra", "viper"], name="foo")])
#        max_speed  shield
# foo
# cobra          1       2
# viper          4       5


# 부울 시리즈를 반환하는 조건부
print(df.loc[df['shield'] > 6])
#             max_speed  shield
# sidewinder          7       8


# 열 레이블이 지정된 부울 시리즈를 반환하는 조건부
print(df.loc[df['shield'] > 6, ['max_speed']])
#             max_speed
# sidewinder          7


# 부울 시리즈를 반환하는 호출 가능
print(df.loc[lambda df: df['shield'] == 8])
#             max_speed  shield
# sidewinder          7       8


# 레이블 목록과 일치하는 모든 항목에 대한 값 설정
df.loc[['viper', 'sidewinder'], ['shield']] = 50
print(df)
#             max_speed  shield
# cobra               1       2
# viper               4      50
# sidewinder          7      50


# 전체 행에 대한 값 설정
df.loc['cobra'] = 10
print(df)
#             max_speed  shield
# cobra              10      10
# viper               4      50
# sidewinder          7      50


# 전체 열에 대한 값 설정
df.loc[:, 'max_speed'] = 30
print(df)
#             max_speed  shield
# cobra              30      10
# viper              30      50
# sidewinder         30      50


# 호출 가능한 조건과 일치하는 행에 대한 값 설정
df.loc[df['shield'] > 35] = 0
print(df)
#             max_speed  shield
# cobra              30      10
# viper               0       0
# sidewinder          0       0


# 정수 레이블이 있는 인덱스를 사용하여 DataFrame에서 값 가져오기
# 인덱스에 정수를 사용하는 또 다른 예
df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],
     index=[7, 8, 9], columns=['max_speed', 'shield'])
print(df)
#    max_speed  shield
# 7          1       2
# 8          4       5
# 9          7       8


# 행에 대한 정수 레이블이 있는 슬라이스. 위에서 언급했듯이 슬라이스의 시작과 끝이 모두 포함
print(df.loc[7:9])
#    max_speed  shield
# 7          1       2
# 8          4       5
# 9          7       8


# MultiIndex로 값 가져오기
# MultiIndex와 함께 DataFrame을 사용하는 여러 예
tuples = [
   ('cobra', 'mark i'), ('cobra', 'mark ii'),
   ('sidewinder', 'mark i'), ('sidewinder', 'mark ii'),
   ('viper', 'mark ii'), ('viper', 'mark iii')
]
index = pd.MultiIndex.from_tuples(tuples)
values = [[12, 2], [0, 4], [10, 20],
        [1, 4], [7, 1], [16, 36]]
df = pd.DataFrame(values, columns=['max_speed', 'shield'], index=index)
print(df)
#                      max_speed  shield
# cobra      mark i           12       2
#            mark ii           0       4
# sidewinder mark i           10      20
#            mark ii           1       4
# viper      mark ii           7       1
#            mark iii         16      36


# 단일 레이블. 이것은 단일 인덱스가 있는 DataFrame을 반환
print(df.loc['cobra'])
#          max_speed  shield
# mark i          12       2
# mark ii          0       4


# 단일 인덱스 튜플. 이것은 Series를 반환
print(df.loc[('cobra', 'mark ii')])
# max_speed    0
# shield       4
# Name: (cobra, mark ii), dtype: int64


# 행 및 열에 대한 단일 레이블. 튜플을 전달하는 것과 유사하게 Series를 반환
print(df.loc['cobra', 'mark i'])
# max_speed    12
# shield        2
# Name: (cobra, mark i), dtype: int64


# 단일 튜플. [[]] 사용하면 DataFrame이 반환
print(df.loc[[('cobra', 'mark ii')]])
#                max_speed  shield
# cobra mark ii          0       4


# 열에 대한 단일 레이블이 있는 인덱스에 대한 단일 튜플
print(df.loc[('cobra', 'mark i'), 'shield'])
# 2


# 인덱스 튜플에서 단일 레이블로 슬라이스
print(df.loc[('cobra', 'mark i'):'viper'])
#                      max_speed  shield
# cobra      mark i           12       2
#            mark ii           0       4
# sidewinder mark i           10      20
#            mark ii           1       4
# viper      mark ii           7       1
#            mark iii         16      36


# 인덱스 튜플에서 인덱스 튜플로 슬라이스
print(df.loc[('cobra', 'mark i'):('viper', 'mark ii')])
#                     max_speed  shield
# cobra      mark i          12       2
#            mark ii          0       4
# sidewinder mark i          10      20
#            mark ii          1       4
# viper      mark ii          7       1








