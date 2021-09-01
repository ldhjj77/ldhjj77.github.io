import pandas as pd

data = pd.read_csv('2016walking.csv')   # csv 파일 불러오기
print(data)

selectdata = data[['1', '2', '3']]      # 1, 2, 3열의 데이터만 추출하기
print(selectdata)

selectdata.to_csv('./A/A024_123.csv')   # 추출한 데이터를 다름이름으로 저장하기











