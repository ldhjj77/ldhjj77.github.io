# 참조 - https://yganalyst.github.io/data_handling/Pd_8/

import pandas as pd
import numpy as np

# to_datetime / to_Period

# 시간 내에서 특정 순간의 타임스탬프(Timestamp)자료형
# 2007년 1월 전체 기간이나, 2010년 전체 같은 기간(Period)자료형


# 데이터프레임 생성
df = pd.DataFrame([["2021-07-01", 10000], ["2021-07-02", 10500]], columns=["date", "volume"])
print(df)
# 0  2021-07-01   10000
# 1  2021-07-02   10500

print(df.dtypes)
# date      object
# volume     int64
# dtype: object

# Date컬럼을 시계열 객체(Timestamp)로 변환
df['new_date'] = pd.to_datetime(df['date'])
print(df)
#          date  volume   new_date
# 0  2021-07-01   10000 2021-07-01
# 1  2021-07-02   10500 2021-07-02

print(df.dtypes)
# date                object
# volume               int64
# new_date    datetime64[ns]
# dtype: object


# date 컬럼 삭제하고 new_date 컬럼을 인덱스로 지정
df.drop('date', axis = 1, inplace=True)
df.set_index('new_date', inplace=True)

print(df)
#             volume
# new_date
# 2021-07-01   10000
# 2021-07-02   10500

print(df.dtypes)
# volume    int64
# dtype: object

# Timestamp를 Period로 변환
dates = ['2019-01-01', '2019-01-25', '2019-02-01', '2020-03-01', '2021-06-01']
ts_dates = pd.to_datetime(dates)
print(ts_dates)
# DatetimeIndex(['2019-01-01', '2019-01-25', '2019-02-01', '2020-03-01',
#                '2021-06-01'],
#               dtype='datetime64[ns]', freq=None)

pr_day = ts_dates.to_period(freq='D')   # 일 단위로 구분
print(pr_day)
# PeriodIndex(['2019-01-01', '2019-01-25', '2019-02-01', '2020-03-01',
#              '2021-06-01'],
#             dtype='period[D]', freq='D')

pr_month = ts_dates.to_period(freq='M') # 월 단위로 구분
print(pr_month)
# PeriodIndex(['2019-01', '2019-01', '2019-02', '2020-03', '2021-06'], dtype='period[M]', freq='M')

pr_year = ts_dates.to_period(freq='A')  # 년 단위로 구분
print(pr_year)
# PeriodIndex(['2019', '2019', '2019', '2020', '2021'], dtype='period[A-DEC]', freq='A-DEC')



# 시계열 데이터 만들기 : date_range() , period_range()

# Timestamp 배열
ts_ms = pd.date_range(start = '2019-01-01',     # 날짜 범위 시작
                     end = None,                # 날짜 범위 끝
                     periods = 6,               # 생성할 Timestamp 개수
                     freq = 'MS',               # 시간 간격(MS : 월의 시작일)
                     # M만 하면 월의 마지막 일 / 3M 3달 간격
                     tz = 'Asia/Seoul')         # 시간대(timezone)
print(ts_ms)
# DatetimeIndex(['2019-01-01 00:00:00+09:00', '2019-02-01 00:00:00+09:00',
#                '2019-03-01 00:00:00+09:00', '2019-04-01 00:00:00+09:00',
#                '2019-05-01 00:00:00+09:00', '2019-06-01 00:00:00+09:00'],
#               dtype='datetime64[ns, Asia/Seoul]', freq='MS')


# Period 배열
pr_m = pd.period_range(start = '2019-01-01',
                   	   end = None,
                       periods = 3,     
                       freq = 'M')           
print(pr_m)
# PeriodIndex(['2019-01', '2019-02', '2019-03'], dtype='period[M]', freq='M')
