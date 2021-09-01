from math import *		# C 표준에서 정의된 수학 함수
import pandas as pd     # 오픈소스 데이터 분석 및 조작 도구
import numpy as np      # 행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리
import tensorflow as tf		# ML 모델을 개발하고 학습시키는 데 도움이 되는 핵심 오픈소스 라이브러리
import warnings			# 경고 제어
from sklearn.metrics import accuracy_score		# 하위 집합의 정확도를 계산
from sklearn.model_selection import train_test_split, StratifiedKFold
# train_test_split - 배열 또는 행렬을 임의 학습 및 테스트 하위 집합으로 분할
# StratifiedKFold - 계층화 된 K- 폴드 교차 검증 자
from sklearn.preprocessing import Imputer, StandardScaler
# Imputer - 결 측값 완성을위한 대치 변환기
# StandardScaler - 평균을 제거하고 단위 분산에 맞게 조정하여 기능 표준화
import matplotlib.pyplot as plt	# 대화 형 플롯과 간단한 프로그래밍 플롯 생성 
from matplotlib import gridspec	# 영역을 내마음대로 나누고 싶을 때 사용

import keras    # 딥러닝 프레임워크
from keras.models import Sequential
# 각 레이어에 정확히 하나의 입력 텐서와 하나의 출력 텐서가 있는 일반 레이어 스택에 적합한 모델

from keras.layers import Dense, Dropout, BatchNormalization, Activation
# Dense - 입력과 출력을 모두 연결해주며, 입력과 출력을 각각 연결해주는 가중치를 포함하고 있음
# Dropout - Dropout은 딥러닝 학습에 있어서의 문제중 하나인 Overfitting을 해소하기 위해 사용
# 네트워크의 유닛의 일부만 동작하고 일부는 동작하지 않도록 하는 방법
# BatchNormalization - vanishing/exploding gradient 문제를 해결하기위해 사용
# Activation -  활성화 함수 tf.nn.relu또는 "relu"와 같은 내장 활성화 함수의 문자열 이름

from keras.optimizers import Adam 	# 1 차 및 2 차 모멘트의 적응 적 추정을 기반으로하는 확률 적 경사 하강 법
from keras import backend as K	# 텐서 곱셈, 합성 곱 등의 저수준의 연산을 제공
from tensorflow.python.client import device_lib		# Tensorflow가 내 GPU를 활용하고 있는지 확인



import lightgbm as lgb	# 트리 기반 학습 알고리즘을 사용하는 그라디언트 부스팅 프레임 워크
import catboost as cb	# 데이터에 범주형 변수 많을 때 유용한 모델
import xgboost as xgb	# 분산 그라디언트 부스팅 라이브러리


import seaborn as sns	# 통계 데이터 시각화
sns.set_style("whitegrid")	# whitegrid 사용
pd.set_option('display.max_columns', None)  # 최대 열수 설정
pd.set_option('display.max_rows', 200)  # 출력 행수 설정
warnings.filterwarnings('ignore')   # 일치하는 경고를 인쇄하지 않습니다

print(device_lib.list_local_devices())

config = tf.ConfigProto(device_count={"CPU": 1, "GPU" : 1}) # tensorflow에 사용할 장비 설정
session = tf.Session(config=config) # tensorflow의 연산결과를 확인하기위한 변수
K.set_session(session)  # keras가 tensorflow의 세션을 사용할수 있도록

















### 2

# 데이터 합치기
#test = pd.read_csv(r"c:\work\dataset\titanic\test.csv", ",")
#train = pd.read_csv(r"c:\work\dataset\titanic\train.csv", ",")
test = pd.read_csv("../input/test.csv", ",")    # test파일 불러오기 ("경로", "문자열")
train = pd.read_csv("../input/train.csv", ",")  # train파일 불러오기 ("경로", "문자열")
test["is_test"] = True      # test함수에 "is_test" 컬럼을 생성하고 내용은 전부 True 입력
train["is_test"] = False    # train함수에 "is_test" 컬럼을 생성하고 내용은 전부 Fales 입력 
# 13개의 컬럼을 가진 common 함수 생성
common = pd.concat([test, train],axis=0).loc[:,["PassengerId", "Survived", "is_test", 
                                                "Age", "Cabin", "Embarked", 
                                                "Fare", "Name", "Parch", "Pclass", 
                                                "Sex", "SibSp", "Ticket"]]


# PassengerId : 순번						
# survived : 생존=1, 죽음=0
# pclass : 승객 등급. 1등급=1, 2등급=2, 3등급=3
# Name : 이름
# Sex : 성별
# Age : 나이
# sibsp : 함께 탑승한 형제 또는 배우자 수
# parch : 함께 탑승한 부모 또는 자녀 수
# ticket : 티켓 번호
# Fare : 티켓가격
# cabin : 선실 번호
# embarked : 탑승장소 S=Southhampton, C=Cherbourg, Q=Queenstown

















### 3

# 중복 티켓 수 확인
common["Ticket"].count() - len(common["Ticket"].unique())



















### 4

#  train 데이터를 이용해 그룹화 / by="Ticket" -> "Ticket"의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"PassengerId" : 'count', -> Cabin의 값이 같은 "PassengerId" 의 수를 'count'해서(합) "PassengerId" 에 추가 
# "Sex" : lambda x : x[x=="female"].count()}) -> "female" 일 경우 count()(합)의 값을 "Sex" 칼럼에 추가
t = train.groupby(by="Ticket", as_index=False).agg({"PassengerId" : 'count', "Sex" : lambda x : x[x=="female"].count()})

# t 의컬럼을 "Ticket", "SameTicket", "FemalesOnTicket" 으로 변경
t.columns = ["Ticket", "SameTicket", "FemalesOnTicket"]

# common 에다가 t 를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="Ticket" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, t, how="left", on="Ticket")

# common데이터에 "TicketDigits" 컬럼을 생성하고 Ticket의 내용을 숫자로 변환해서 입력
# str.split(" ") -> 공백으로 문자열을 나눔 / errors="coerce" -> 잘못된 구문은 NaN으로 설정
# .astype(np.str) -> 문자형으로 변환 / .str.len() -> 길이구하기
# 결과는 문자의 길이가 나옴
common["TicketDigits"] = pd.to_numeric(common["Ticket"].str.split(" ").str[-1], errors="coerce").astype(np.str).str.len()

# common 데이터에 "TicketIsNumber" 칼럼 추가후 "Ticket" 의 내용을 추가
# .str.contains("[A-Za-z]", regex = True) -> [A-Za-z] 포함여부 확인후 포함되어있다면 True값 반환
common["TicketIsNumber"] = ~common["Ticket"].str.contains("[A-Za-z]", regex = True)

# common 데이터에 "FemalesPerTicketPart" 컬럼 추가후 common["FemalesOnTicket"]/common["SameTicket"] 값을 삽입
common["FemalesPerTicketPart"] = common["FemalesOnTicket"]/common["SameTicket"]



















### 5

# Figure 객체를 생성하고 1*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(1, 3, figsize=(20, 5))
# 막대그래프 생성
sns.barplot(x="TicketDigits", y="Survived", data=common, ax=ax[0])  # "TicketDigits" 의 생존률
sns.barplot(x="TicketIsNumber", y="Survived", data=common, ax = ax[1])  #  "TicketIsNumber" 의 생존률
# 산점도 그래프 생성
sns.regplot(x="FemalesPerTicketPart", y="Survived", data=common, ax = ax[2])  # "FemalesPerTicketPart" 의 생존률
plt.show();






















### 6

# str.contains - 지정한 문자열이 포함되어있는지 확인(있으면 True값을 반환)
# 중북이름 여부 컬럼 생성
common["DoubleName"] = common["Name"].str.contains("\(")
# 이름길이 측정 컬럼 생성
common["NameLen"] = common["Name"].str.len()
















### 7

# Figure 객체를 생성하고 1*2 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(1, 2, figsize=(20, 5))
# "DoubleName" 의 생존률 막대그래프 생성
sns.barplot(x="DoubleName", y="Survived", data=common, ax=ax[0])
# "NameLen" 의 산점도 그래프 생성
sns.regplot(x="NameLen", y="Survived", data=common, ax = ax[1])
plt.show();

















### 8

# title 컬럼 생성( Miss, Mr등 )
common["Title"] = common["Name"].str.split(", ").str[1].str.split(" ").str[0]
common.loc[common["Title"].str[-1]!=".", "Title"]="Bad"

# 특이한 타이틀(Col, Major 등) 추출하기 
rare_title = common["Title"].value_counts()[common["Title"].value_counts() < 5].index

# 특이한 타이틀들을 Rare 로 변환하기
common["Title"] = common["Title"].apply(lambda x: 'Rare' if x in rare_title else x)

# 타이틀별 생존률
titletarget = common.groupby(by="Title", as_index=False).agg({"Survived" : 'mean'})

# titletarget의 컬럼을 "Title", "TargetByTitle" 로 변환
titletarget.columns = ["Title", "TargetByTitle"]

# common 에다가 titletarget 를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="Title" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, titletarget, how="left", on="Title")


















### 9

# title 별 생존률 막대그래프
sns.barplot(x="Title", y="TargetByTitle", data=common)
plt.show()
















### 10

# Family 컬럼을 생성하고 Parch + SibSp + 1 의값을 넣음
common["Family"] = common["Parch"] + common["SibSp"] + 1
# Alone 컬럼을 생성하고 Family 가 1인 경우에 True 값을 넣고 그외엔 False를 넣음
common["Alone"] = common["Family"] == 1

















### 11

# train 데이터를 이용해 그룹화 / by="Cabin" -> Cabin의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"PassengerId" : 'count'}) -> Cabin의 값이 같은 "PassengerId" 의 수를 'count'해서(합) "PassengerId" 에 추가 
# 선실별로 인원수 구하기
cap = train.groupby(by="Cabin", as_index=False).agg({"PassengerId" : 'count'})

# cap의 컬럼을 "Cabin", "SameCabin" 로 변경
cap.columns = ["Cabin", "SameCabin"]

# common 데이터에 cap 데이터를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="Title" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, cap, how="left", on="Cabin")

# common데이터에 "CabinNumber" 컬럼을 생성하고 Cabin의 내용을 숫자로 변환해서 입력
# errors="coerce" -> 잘못된 구문은 NaN으로 설정
common["CabinNumber"] = pd.to_numeric(common["Cabin"].str[1:], errors = "coerce")

# common 데이터에 "CabinEven" 컬럼을 생성후 "CabinNumber"값을 2로 나눈후 나머지값 입력(선실이 좌측인지 우측인지 구분)
common["CabinEven"] = common["CabinNumber"] %2

# "CabinsPerMan" 컬럼을 생성후 "Cabin" 의내용을 가져와서 공백으로 문자열을 분리하고 문자열의 갯수를 입력
common["CabinsPerMan"] = common["Cabin"].str.split(" ").str.len()

# "Deck" 컬럼을 생성후 "Cabin" 의내용을 가져와서 첫글자에따라 순위를 매기고 nan값에는 -1을 입력
common["Deck"] = common["Cabin"].str[0].rank().fillna(-1)


# common 데이터를 이용해 그룹화 / by="Deck" -> "Deck"의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"Survived" : 'mean'}) -> "Deck"의 값이 같은 "Survived" 의 수를 'mean'해서(평균) "Survived" 에 추가 
# 선실 앞자리 글자별 평균생존률 구하기
decktarget = common.groupby(by="Deck", as_index=False).agg({"Survived" : 'mean'})

# decktarget의 컬럼을 "Deck", "TargetByDeck" 로 변환
decktarget.columns = ["Deck", "TargetByDeck"]

# common 데이터에 decktarget 데이터를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="Deck" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, decktarget, how="left", on="Deck")















### 12

# Figure 객체를 생성하고 1*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(1, 3, figsize=(20, 5))

# "Deck"의 생존률 막대그래프
sns.barplot(x="Deck", y="TargetByDeck", data=common.sort_values("Deck"), ax=ax[0])

# "CabinEven"의 생존률 막대그래프
sns.barplot(x="CabinEven", y="Survived", data=common, ax=ax[1])
# "CabinNumber"의 생존률 산점도그래프
sns.regplot(x="CabinNumber", y="Survived", data=common, ax=ax[2])

plt.show()















### 13
# 연령별 성별별 생존률의 점이 겹치지 않는 범주 형 산점도 그래프
sns.swarmplot(x="Survived", y="Age", hue="Sex", palette=sns.color_palette(["#20AFCF","#cf4040"]), data=common)
plt.show()















### 14

# pd.qcut(common['Age'] -> 동일한 갯수로 나눔 / fillna(common['Age'] -> nan에 'Age'의 평균값을 정수형으로 삽입
# 'AgeGroup' 컬럼을 생성하고 'Age'의 내용을 6개의 연령대를 만들어서 연령대로 구분(-0.001 ~ 19 / 19 ~ 25 / 25 ~ 29 / 29 ~ 30 / 30 ~ 41 / 41 ~ 80 )해서 삽입하고 
# nan에는 평균값인 25 ~ 29가 들어감
common['AgeGroup'] = pd.qcut(common['Age'].fillna(common['Age'].mean()).astype(int), 6)

# common 데이터를 이용해 그룹화 / by="AgeGroup" -> "AgeGroup"의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"Survived" :  'mean'}) -> "AgeGroup"의 값이 같은 "Survived" 의 수를 'mean'해서(평균) "Survived" 에 추가 
# 연령 그룹별 평균생존률
agetarget = common.groupby(by="AgeGroup", as_index=False).agg({"Survived" : 'mean'})

# agetarget의 컬럼을 "AgeGroup", "TargetByAgeGroup"로 변환
agetarget.columns = ["AgeGroup", "TargetByAgeGroup"]

# common 데이터에 agetarget 데이터를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="AgeGroup" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, agetarget, how="left", on="AgeGroup")

# "IsTinyChild" 컬럼을 생성후 "Age" <1 값을 삽입
common["IsTinyChild"] = common["Age"]<1

# "IsChild" 컬럼을 생성후  "Age" <10 값을 삽입
common["IsChild"] = common["Age"]<10

# "AverageAge" 컬럼을 생성후 "Age" / "Family" 값을 삽입
common["AverageAge"] = common["Age"] / common["Family"]













### 15

# Figure 객체를 생성하고 1*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(1, 3, figsize=(20, 5))

# "AgeGroup"의 생존률 막대그래프
sns.barplot(x="AgeGroup", y="TargetByAgeGroup", data=common, ax = ax[0])

# "IsChild"의 생존률 막대그래프
sns.barplot(x="IsChild", y="Survived", data=common, ax = ax[1])

# "AverageAge"의 생존률 산점도그래프
sns.regplot(x="AverageAge", y="Survived", data=common, ax = ax[2])
plt.show();















### 16

# 'FareGroup' 컬럼을 생성하고 'Fare'의 값을 6개의 그룹으로 나눠서 삽입(-0.001 ~ 7.0 / 7.0 ~ 8.0 / 8.0 ~ 14.0 / 14.0 ~ 26.0 / 26.0 ~ 53.0 / 53.0 ~ 512.0)
# nan에는 'Fare' 값의 평균값을 정수로 삽입
common['FareGroup'] = pd.qcut(common['Fare'].fillna(common['Fare'].mean()).astype(int), 6)

# common 데이터를 이용해 그룹화 / by="FareGroup" -> "FareGroup"의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"Survived" :  'mean'}) -> "FareGroup"의 값이 같은 "Survived" 의 수를 'mean'해서(평균) "Survived" 에 추가 
# 페어그룹별 평균 생존률
faretarget = common.groupby(by="FareGroup", as_index=False).agg({"Survived" : 'mean'})

# faretarget의 컬럼을 "FareGroup", "TargetByFareGroup"로 변경
faretarget.columns = ["FareGroup", "TargetByFareGroup"]

# common 데이터에 faretarget 데이터를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="FareGroup" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, faretarget, how="left", on="FareGroup")

# "AverageFareByFamily" 컬럼을 생성후 "Fare" / "Family" 값을 삽입
common["AverageFareByFamily"] = common["Fare"] / common["Family"]

# "AverageFareByTicket" 컬럼을 생성후 "Fare" / "SameTicket" 값을 삽입
common["AverageFareByTicket"] = common["Fare"] / common["SameTicket"]

# "FareLog" 컬럼을 생성후 "Fare" 의 로그값을 삽입
common["FareLog"] = np.log(common["Fare"])














### 17

# "FareGroup"의 생존률 막대그래프
sns.barplot(x="FareGroup", y="TargetByFareGroup", data=common)
plt.show()














### 18

# common 데이터를 이용해 그룹화 / by="Pclass" ->"Pclass"의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"Survived" :  'mean'}) -> "Pclass"의 값이 같은 "Survived" 의 수를 'mean'해서(평균) "Survived" 에 추가 
# 승객등급별 생존률 구하기
pclasstarget = common.groupby(by="Pclass", as_index=False).agg({"Survived" : 'mean'})

# pclasstarget의 컬럼을 "Pclass", "TargetByPclass"로 변환
pclasstarget.columns = ["Pclass", "TargetByPclass"]

# common 데이터에 pclasstarget 데이터를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="Pclass" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, pclasstarget, how="left", on="Pclass")

# common 데이터를 이용해 그룹화 / by="Embarked" -> "Embarked"의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"Survived" :  'mean'}) -> "Embarked"의 값이 같은 "Survived" 의 수를 'mean'해서(평균) "Survived" 에 추가 
# 탑승장소별로 생존률 구하기
Embarkedtarget = common.groupby(by="Embarked", as_index=False).agg({"Survived" : 'mean'})

# Embarkedtarget의 컬럼을 "Embarked", "TargetByEmbarked"로 변환
Embarkedtarget.columns = ["Embarked", "TargetByEmbarked"]

# common 데이터에 Embarkedtarget 데이터를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="Embarked" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, Embarkedtarget, how="left", on="Embarked")

# common 데이터를 이용해 그룹화 / by="Sex" -> "Sex"의 값이 추가되고 / as_index=False -> 인덱스 사용안함
# .agg({"Survived" :  'mean'}) -> "Sex"의 값이 같은 "Survived" 의 수를 'mean'해서(평균) "Survived" 에 추가 
# 성별별 생존률 구하기
Sextarget = common.groupby(by="Sex", as_index=False).agg({"Survived" : 'mean'})

# Sextarget의 컬럼을 "Sex", "TargetBySex"로 변환
Sextarget.columns = ["Sex", "TargetBySex"]

# common 데이터에 Sextarget 데이터를 병합함(how="left" -> 왼쪽 프레임의 키만 사용 / on="Sex" -> 조인 할 열 또는 인덱스 수준 이름)
common = pd.merge(common, Sextarget, how="left", on="Sex")














### 19

# Figure 객체를 생성하고 1*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(1, 3, figsize=(20, 5))

# "Pclass"의 생존률 막대그래프
sns.barplot(x="Pclass", y="TargetByPclass", data=common, ax=ax[0])

# "Embarked"의 생존률 막대그래프
sns.barplot(x="Embarked", y="TargetByEmbarked", data=common, ax = ax[1])

# "Sex"의 생존률 산점도그래프
sns.barplot(x="Sex", y="TargetBySex", data=common, ax = ax[2])
plt.show();













### 20

# 사용할 모든 컬럼을 가진 allfeatures 변수 생성
allfeatures = [
    "PassengerId", 
    "is_test", 
    "Survived", 
    "Age", 
    "Fare", 
    "Parch", 
    "Pclass",
    "SibSp", 
    "Sex", 
    "Embarked", 
    "SameTicket", 
    "FemalesOnTicket", 
    "SameCabin", 
    "Deck", 
    "TargetByDeck", 
    "TargetByTitle", 
    "TargetByAgeGroup", 
    "TargetByFareGroup",
    "TargetByPclass",
    "TargetByEmbarked",
    "TargetBySex",
    "Title", 
    "CabinNumber", 
    "CabinEven", 
    "CabinsPerMan", 
    "DoubleName", 
    "NameLen", 
    "TicketDigits",
    "TicketIsNumber",
    "IsTinyChild", 
    "IsChild", 
    "Alone", 
    "Family", 
    "AverageAge",
    "AverageFareByFamily",
    "AverageFareByTicket",
    "FemalesPerTicketPart"
]

# c변수를 생성하고 common데이터의 모든행과 allfeatures에 들어있는 열의 정보를 가져오도록 함
c = common.loc[:, allfeatures]

# 문자형 데이터인 "Title", "Embarked", "Pclass", "Sex"를 수치형 데이터로 변환후 가변수화함
# 문자형 컬럼을 데이터 종류별로 컬럼을 만듬(title 을 Title_Dr.  Title_Master. 등으로) 
# 문자형을 수치형으로 바꾸기만 했을경우 관계성으로 인한 학습에러를 방지하기위해 가변수화의 과정이 필요함
c = pd.get_dummies(c, columns=[
    "Title", 
    "Embarked", 
    "Pclass", 
    "Sex"
])













### 21

# .describe() -> 데이터 요약 / .sort_values("count") -> "count" 컬럼을 기준으로 정렬
c.describe().T.sort_values("count")












### 22

# .iloc -> 정수기반 인덱싱 / Imputer(strategy="most_frequent") -> 결측치를 "most_frequent"(최빈값)으로 대체
# .fit_transform(c.iloc[:,3:]) -> c.iloc[:,3:] 데이터의 계수추정과 자료변환 실행
c.iloc[:,3:] = Imputer(strategy="most_frequent").fit_transform(c.iloc[:,3:])

# dep변수에 "is_test"가 False인 "Survived"값 추가
dep = c[c["is_test"] == False].loc[:, ["Survived"]]

# indep변수에 "is_test"가 False인 자료들의 3열이후의(4열부터) 값들 추가
indep = c[c["is_test"] == False].iloc[:, 3:]

# res변수에 "is_test"가 True인 자료들의 3열이후의(4열부터) 값들 추가
res = c[c["is_test"] == True].iloc[:, 3:]

# res_index변수에 "is_test"가 True인 자료들의 "PassengerId" 값을 추가
res_index = c[c["is_test"] == True].loc[:, "PassengerId"]

# .iloc -> 정수기반 인덱싱 
# StandardScaler() -> 평균을 제거하고 단위 분산으로 스케일링하여 기능 표준화
# .fit_transform(indep.iloc[:,3:]) -> indep.iloc[:,3:] 데이터의 계수추정과 자료변환 실행
indep.iloc[:,3:] = StandardScaler().fit_transform(indep.iloc[:,3:])

# StandardScaler() -> 평균을 제거하고 단위 분산으로 스케일링하여 기능 표준화
# .fit_transform(res.iloc[:,3:]) -> res.iloc[:,3:] 데이터의 계수추정과 자료변환 실행
res.iloc[:,3:] = StandardScaler().fit_transform(res.iloc[:,3:])

# train_test_split -> 배열 또는 행렬을 임의 학습 및 테스트 하위 집합으로 분할
# test_size=0.40 -> float 인 경우 0.0에서 1.0 사이 여야하며 테스트 분할에 포함 할 데이터 세트의 비율, int 인 경우 테스트 샘플의 절대 수를 나타냄
# random_state -> 렌덤함수의 스피드(수치를 바꾸면 렌덤데이터를 추출하는 레코드값이 달라짐)
indep_train, indep_test, dep_train, dep_test = train_test_split(indep, dep, test_size=0.40, random_state=47)








### Model 1. Keras MLP
### 23

# 수동으로 디바이스 배치하기 CPU 0번
with tf.device('/device:CPU:0'):

    # 선형 레이어 구성 모델
    gs1 = Sequential()

    # Dense(45 -> (*, 45) 형태의 배열을 출력
    # activation='linear' -> 활성화 함수지정('linear'= 계산된 값을 그대로 출력으로 보냄) 
    # input_dim=45 -> (*, 45) 형태의 배열을 인풋으로 받음
    gs1.add(Dense(45 ,activation='linear', input_dim=45))

    # 학습성능을 높이기 위함 정규화
    gs1.add(BatchNormalization())

    # Dense(9 -> (*, 9) 형태의 배열을 출력
    # activation='linear' -> 활성화 함수지정('linear'= 계산된 값을 그대로 출력으로 보냄)  
    gs1.add(Dense(9,activation='linear'))

    # 학습성능을 높이기 위함 정규화
    gs1.add(BatchNormalization())

    # Overfitting을 해소하기 위해사용 0.4 유닛을 드롭함
    gs1.add(Dropout(0.4))

    # Dense(5 -> (*, 5) 형태의 배열을 출력
    # activation='linear' -> 활성화 함수지정('linear'= 계산된 값을 그대로 출력으로 보냄) 
    gs1.add(Dense(5,activation='linear'))

    # 학습성능을 높이기 위함 정규화
    gs1.add(BatchNormalization())

    # Overfitting을 해소하기 위해사용 0.2 유닛을 드롭함
    gs1.add(Dropout(0.2))

    # Dense(5 -> (*, 5) 형태의 배열을 출력
    # activation='relu' -> 활성화 함수 지정('relu'=정류 된 선형 단위 활성화 함수)  
    gs1.add(Dense(1,activation='relu', ))

    # 학습을 위한 모델 생성
    # optimizer=Adam -> 컴파일을 위한 매개변수(Adam : 값을 예측할 경우 사용)
    # lr=0.001 -> 0보다 크거나 같은 float 값. 학습률.
    # beta_1=0.9  -> 0보다 크고 1보다 작은 float 값. 일반적으로 1에 가깝게 설정
    # beta_2=0.999  -> 0보다 크고 1보다 작은 float 값. 일반적으로 1에 가깝게 설정
    # epsilon -> 수치 식에 사용되는 fuzz factor의 값을 반환
    # decay -> 0보다 크거나 같은 float 값. 업데이트마다 적용되는 학습률의 감소율
    # loss='binary_crossentropy' -> 이진 교차 엔트로피 손실을 계산
    # metrics=['accuracy'] -> 딥 러닝 모델의 성능을 평가하는 데 사용되는 함수('accuracy'=예측이 레이블과 동일한 빈도를 계산)
    gs1.compile(optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0), loss='binary_crossentropy', metrics=['accuracy'])


    # fit -> 데이터학습용 파라미터 입력
    # epochs -> 정수. 모델을 학습시킬 세대의 수. 한 세대는 제공된 모든 x와 y 데이터에 대한 반복
    # batch_size -> 정수 혹은 None. 몇 개의 샘플로 가중치를 갱신할 것인지 지정. 따로 지정하지 않으면 디폴트인 32가 적용
    # validation_data -> 성능 평가용 데이터
    # verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
    gs1.fit(indep_train, dep_train, epochs=500, batch_size=30, validation_data=(indep_test,dep_test), verbose=False)

    # # res를 기반으로 gs1 데이터셋 예측 수행()
    g=gs1.predict_classes(res)[:,0]


    print(accuracy_score(dep_test, gs1.predict_classes(indep_test)), accuracy_score(dep_train, gs1.predict_classes(indep_train)))















### 24

cvscores = []   # cvscore 리스트변수 생성
data = pd.DataFrame()   # data 데이터프레임 변수 생성
i=1

# tensorflow에 사용할 디바이스 설정 CPU 0번 사용
with tf.device('/device:CPU:0'):
    # 교차검증을 위한 설정 StratifiedKFold -> target에 속성값의 개수를 동일하게 가져감으로써 kfold 같이 데이터가 한곳으로 몰리는것을 방지
    # n_splits -> 데이터 분할 수 / shuffle -> 데이터를 분할할때마다 데이터를 섞을지 여부
    # random_state -> 렌덤함수의 스피드(수치를 바꾸면 렌덤데이터를 추출하는 레코드값이 달라짐)
    # split(indep, dep.iloc[:,0]) -> indep과 dep.iloc[:,0]로 분할 
    # dep.iloc[:,0] -> dep의 [:,0]행 선택
    for train, test in StratifiedKFold(n_splits=5, shuffle=True, random_state=1).split(indep, dep.iloc[:,0]):

        # indep의 재 인덱싱작업(train열의 형태로 모든행 입력)
        X = indep.reindex().iloc[train,:]
        # dep의 재 인덱싱작업(train열의 형태로 첫번째행 입력)
        Y = dep.reindex().iloc[train,0]

        # dep의 재 인덱싱작업(test열의 형태로 모든행 입력)
        Xv = indep.reindex().iloc[test,:]
        # dep의 재 인덱싱작업(test열의 형태로 첫번째행 입력)
        Yv = dep.reindex().iloc[test,0]
        
        # 선형 레이어 구성 모델
        gs1 = Sequential()

        # Dense(45 -> (*, 45) 형태의 배열을 출력
        # activation='linear' -> 활성화 함수지정('linear'= 계산된 값을 그대로 출력으로 보냄) 
        # input_dim=45 -> (*, 45) 형태의 배열을 인풋으로 받음
        gs1.add(Dense(45 ,activation='linear', input_dim=45))

        # 학습성능을 높이기 위함 정규화
        gs1.add(BatchNormalization())

        # Dense(9 -> (*, 9) 형태의 배열을 출력
        # activation='linear' -> 활성화 함수지정('linear'= 계산된 값을 그대로 출력으로 보냄) 
        gs1.add(Dense(9,activation='linear'))

        # 학습성능을 높이기 위함 정규화     
        gs1.add(BatchNormalization())

        # Overfitting을 해소하기 위해사용 0.4 유닛을 드롭함
        gs1.add(Dropout(0.4))

        # Dense(5 -> (*, 5) 형태의 배열을 출력
        # activation='linear' -> 활성화 함수지정('linear'= 계산된 값을 그대로 출력으로 보냄) 
        gs1.add(Dense(5,activation='linear'))

        # 학습성능을 높이기 위함 정규화    
        gs1.add(BatchNormalization())

        # Overfitting을 해소하기 위해사용 0.2 유닛을 드롭함
        gs1.add(Dropout(0.2))

        # Dense(5 -> (*, 5) 형태의 배열을 출력
        # activation='relu' -> 활성화 함수 지정('relu'=정류 된 선형 단위 활성화 함수)  
        gs1.add(Dense(1,activation='relu', ))

        # 학습을 위한 모델 생성
        # optimizer=Adam -> 컴파일을 위한 매개변수(Adam : 값을 예측할 경우 사용)
        # lr=0.001 -> 0보다 크거나 같은 float 값. 학습률.
        # beta_1=0.9  -> 0보다 크고 1보다 작은 float 값. 일반적으로 1에 가깝게 설정
        # beta_2=0.999  -> 0보다 크고 1보다 작은 float 값. 일반적으로 1에 가깝게 설정
        # epsilon -> 수치 식에 사용되는 fuzz factor의 값을 반환
        # decay -> 0보다 크거나 같은 float 값. 업데이트마다 적용되는 학습률의 감소율
        # loss='binary_crossentropy' -> 이진 교차 엔트로피- 손실을 계산
        # metrics=['accuracy'] -> 딥 러닝 모델의 성능을 평가하는 데 사용되는 함수('accuracy'=예측이 레이블과 동일한 빈도를 계산)    
        gs1.compile(optimizer=Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0), loss='binary_crossentropy', metrics=['accuracy'])


        # fit -> 데이터학습용 파라미터 입력
        # epochs -> 정수. 모델을 학습시킬 세대의 수. 한 세대는 제공된 모든 x와 y 데이터에 대한 반복
        # batch_size -> 정수 혹은 None. 몇 개의 샘플로 가중치를 갱신할 것인지 지정. 따로 지정하지 않으면 디폴트인 32가 적용
        # validation_data -> 성능 평가용 데이터
        # verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
        gs1.fit(X, Y, epochs=500, batch_size=30, validation_data=(Xv, Yv), verbose=False)
        
        # res를 기반으로 gs1 데이터셋 예측 수행()
        data[i] = gs1.predict_classes(res)[:,0]

        # evaluate -> 테스트 모드에서의 모델의 손실 값과 측정항목 값을 반환
        # verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
        scores = gs1.evaluate(Xv, Yv, verbose=0)
        print(gs1.metrics_names[1], scores[1])

        # cvscores에 scores[1] 데이터 추가
        cvscores.append(scores[1])
        i+=1

# mlp_mean에 cvscores의 평균값 추가
mlp_mean = np.mean(cvscores)

# mlp_stdev에 cvscores의 표준편차값 추가
mlp_stdev = np.std(cvscores)
print(mlp_mean, mlp_stdev)

# g에 data값의 행값들의 평균을 반올림한 값을 추가
g = np.round(data.mean(axis=1))
















### 25

# Figure 객체를 생성하고 1*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴 
# sharex='col' -> 각 서브 플롯 열은 x 축 또는 y 축을 공유
fig, ax = plt.subplots(2, 1, sharex='col', figsize=(20, 10))

# 차트제목 설정
ax[0].set_title('Model accuracy history')

# 훈련 정확도 확인
ax[0].plot(gs1.history.history['acc'])

# 검증 정확도 확인
ax[0].plot(gs1.history.history['val_acc'])

# y축 레이블 설정
ax[0].set_ylabel('Accuracy')

# 차트의 범례 설정
ax[0].legend(['train', 'test'], loc='right')

# 차트에 그리드 설정여부 기본은 False
ax[0].grid()




# 차트제목 설정
ax[1].set_title('Model loss history')

# 훈련 손실값 확인
ax[1].plot(gs1.history.history['loss'])

# 검증 손실값 확인
ax[1].plot(gs1.history.history['val_loss'])

# y축 라벨 설정
ax[1].set_ylabel('Loss')

# 차트의 범례 설정
ax[1].legend(['train', 'test'], loc='right')

# 차트에 그리드 설정여부 기본은 False
ax[1].grid()

# x축 라벨 설정
plt.xlabel('Epoch')
plt.show()













### 26

#result = pd.DataFrame(res_index.astype(np.int), columns=["PassengerId"])
#result["Survived"] = g.astype(np.int)
#result.to_csv(r"c:\work\dataset\titanic\mlp.csv", ",", index=None)
#result.to_csv("mlp.csv", ",", index=None)























### Model 2. LightGBM
### 27

# Example of manual parameter tuning
"""
for i in range(1,10):
    params = {}
    params["max_depth"] = i
    params["learning_rate"] = 0.45
    params["lambda_l1"] = 0.1
    params["lambda_l2"] = 0.01
    params["n_estimators"] = 5000
    params["n_jobs"]=5 
    params["objective"] = "binary"
    
    params["boosting"] = "dart"
    params["colsample_bytree"] = 0.9
    params["subsample"] =0.9

    train_data = lgb.Dataset(data=indep_train, label=dep_train, free_raw_data=False, feature_name = list(indep_train))
    cv_result = lgb.cv(params, train_data, nfold=5, stratified=False, metrics=['binary_error'], early_stopping_rounds=50)
    print(i, 1-np.mean(cv_result["binary_error-mean"]))
    """;













### 28

# train_test_split -> 배열 또는 행렬을 임의 학습 및 테스트 하위 집합으로 분할
# test_size=0.40 -> float 인 경우 0.0에서 1.0 사이 여야하며 테스트 분할에 포함 할 데이터 세트의 비율, int 인 경우 테스트 샘플의 절대 수를 나타냄
# random_state -> 렌덤함수의 스피드(수치를 바꾸면 렌덤데이터를 추출하는 레코드값이 달라짐)
indep_train, indep_test, dep_train, dep_test = train_test_split(indep, dep, test_size=0.40, random_state=47)

# lgb.LGBMClassifier -> 모델생성 
# max_depth = 7 -> 기본 학습자의 최대 트리 깊이 7
# lambda_l1 / lambda_l2 -> 정규화. 과적합을 방지할수 있지만, 정확도를 저하시킬수 있기때문에 일반적으로 디폴트값이 0을 사용
# learning_rate = 0.01 -> 학습 스텝의 크기 /  n_estimators -> 생성할 트리의 개수
# reg_alpha -> 가중치에 대한 L1 정규화 항. 이 값을 늘리면 모델이 더 보수적이 됨
# colsample_bytree -> 개별 의사결정나무 모형에 사용될 변수갯수를 지정. 보통 0.5 ~ 1 사용됨. 기본값 1
# subsample -> 개별 의사결정나무 모형에 사용되는 임의 표본수를 지정. 보통 0.5 ~ 1 사용됨
# n_jobs -> xgboost를 실행하는 데 사용되는 병렬 스레드 수. 그리드 검색과 같은 다른 Scikit-Learn 알고리즘과 함께 사용하는 경우 스레드를 병렬화하고 균형을 조정할 알고리즘을 선택할 수 있습니다. 스레드 경합을 만들면 두 알고리즘이 크게 느려집니다.
gs1 = lgb.LGBMClassifier(max_depth = 7,
                         lambda_l1 = 0.1,
                         lambda_l2 = 0.01,
                         learning_rate = 0.01, 
                         n_estimators = 500, reg_alpha = 1.1, colsample_bytree = 0.9, subsample = 0.9,
                         n_jobs = 5)

# eval_set -> 검증용 세트 지정 / verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
# eval_metric='accuracy' -> 딥 러닝 모델의 성능을 평가하는 데 사용되는 함수
# ('accuracy'=예측이 레이블과 동일한 빈도를 계산)  
# early_stopping_rounds -> 조기 중단을 위한 라운드를 설정
gs1.fit(indep_train, dep_train, eval_set=[(indep_test, dep_test)], eval_metric='accuracy', verbose=False, early_stopping_rounds=50);


# res를 기반으로 gs1 데이터셋 예측 수행
g = gs1.predict(res)

# accuracy_score -> 부분 집합 정확도를 계산
a = accuracy_score(dep_test, gs1.predict(indep_test))
b = accuracy_score(dep_train, gs1.predict(indep_train))
print(a, b)












### 29

# zip -> indep.columns과 gs1의 feature_importances_(변수중요도)를 묶어줌 
attr2 = {k: v for k, v in zip(indep.columns, gs1.feature_importances_) if v>0}

# 중요도가 낮은순으로 정렬
attr2 = sorted(attr2.items(), key=lambda x: x[1], reverse = False)

# x1과 y1에 attr2의 컬럼을 각각 분리해서 넣음
x1,y1 = zip(*attr2)


i1=range(len(x1))   # range(0, 33) 컬럼의 갯수

# 새로운 피규어 생성
plt.figure(num=None, figsize=(9, 7), dpi=300, facecolor='w', edgecolor='k')

# 가로 막대그래프 생성
plt.barh(i1, y1)

# 그래프 제목설정
plt.title("LGBM")

# y축 눈금값 설정
plt.yticks(i1, x1)
plt.show();











### 30

model = []  # model 리스트 변수 생성
cvscores = []   # cvscores 리스트 변수 생성

for i in range(0,90):   # 90회 반복하며 학습함

    # train_test_split -> 배열 또는 행렬을 임의 학습 및 테스트 하위 집합으로 분할
    # test_size=0.40 -> float 인 경우 0.0에서 1.0 사이 여야하며 테스트 분할에 포함 할 데이터 세트의 비율, int 인 경우 테스트 샘플의 절대 수를 나타냄
    # random_state -> 렌덤함수의 스피드(수치를 바꾸면 렌덤데이터를 추출하는 레코드값이 달라짐)
    indep_train, indep_test, dep_train, dep_test = train_test_split(indep, dep, test_size=0.40, random_state=i)

    # lgb.LGBMClassifier -> 모델생성 
    # max_depth = 7 -> 기본 학습자의 최대 트리 깊이 7
    # lambda_l1 / lambda_l2 -> 정규화. 과적합을 방지할수 있지만, 정확도를 저하시킬수 있기때문에 일반적으로 디폴트값이 0을 사용
    # learning_rate = 0.01 -> 학습 스텝의 크기 
    # num_iterations -> 나무를 반복하며 부스팅 하는데 몇번을 반복할것인가
    # n_estimators -> 생성할 트리의 개수
    # reg_alpha -> 가중치에 대한 L1 정규화 항. 이 값을 늘리면 모델이 더 보수적이 됨
    # colsample_bytree -> 개별 의사결정나무 모형에 사용될 변수갯수를 지정. 보통 0.5 ~ 1 사용됨. 기본값 1
    # subsample -> 개별 의사결정나무 모형에 사용되는 임의 표본수를 지정. 보통 0.5 ~ 1 사용됨
    # n_jobs -> LightGBM을 실행하는 데 사용되는 병렬 스레드 수. 
    # boosting='dart' -> 부스팅방법 'dart'는 딥러닝 드랍아웃을 사용하여 정확도를 중요시하는 방식
    gs1 = lgb.LGBMClassifier(max_depth = 7,
                             lambda_l1 = 0.1,
                             lambda_l2 = 0.01,
                             learning_rate =  0.01, num_iterations=20000,
                             n_estimators = 5000, reg_alpha = 1.1, colsample_bytree = 0.9, subsample = 0.9,
                             n_jobs = 5, boosting='dart' )

    # eval_set -> 검증용 세트 지정 
    # eval_metric='accuracy' -> 딥 러닝 모델의 성능을 평가하는 데 사용되는 함수
    # ('accuracy'=예측이 레이블과 동일한 빈도를 계산)  
    # verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
    # early_stopping_rounds -> 조기 중단을 위한 라운드를 설정                         
    gs1.fit(indep_train, dep_train, eval_set=[(indep_test, dep_test)], eval_metric='accuracy', verbose=False, early_stopping_rounds=50);

    # model에 gs1데이터를 추가
    model.append(gs1)

    # cvscores에 accuracy_score -> 부분 집합 정확도를 계산해서 추가
    cvscores.append(accuracy_score(dep_test, gs1.predict(indep_test)))


data = pd.DataFrame()   # data 데이터프레임 생성
te = pd.DataFrame()     # te 데이터 프레임 생성

for i in range(0,90):
    # res 데이터를 기반으로한 예측
    data[i] = model[i].predict(res)

    # indep_test 데이터를 기반으로한 예측    
    te[i] = model[i].predict(indep_test)

# data의 데이터중 행의 평균값을 구하고 반올림
g = np.round(data.mean(axis=1))

# te의 데이터중 행의 평균값을 구하고 반올림
t = np.round(te.mean(axis=1))

# cvscores 데이터의 평균값
lgb_mean = np.mean(cvscores)

# cvscores 데이터의 표준편차
lgb_stdev = np.std(cvscores)
print(lgb_mean, lgb_stdev)












### 31

result = pd.DataFrame(res_index.astype(np.int), columns=["PassengerId"])
result["Survived"] = g.astype(np.int)
result.to_csv("lgbm.csv", ",", index=None)























### Model 3. CatBoost
### 32

# cb.CatBoostClassifier -> 모델생성 
# depth -> 기본 학습자의 최대 트리 깊이 
# reg_lambda -> L2 정규화. 과적합을 방지할수 있지만, 정확도를 저하시킬수 있기때문에 일반적으로 디폴트값이 0을 사용
# learning_rate -> 학습 스텝의 크기 
# iterations -> 나무를 반복하며 부스팅 하는데 몇번을 반복할것인가
gs1 = cb.CatBoostClassifier(depth = 9, reg_lambda=0.1,
                         learning_rate = 0.09, 
                         iterations = 500)

# eval_set -> 검증용 세트 지정 
# verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
# early_stopping_rounds -> 조기 중단을 위한 라운드를 설정                             
gs1.fit(indep_train, dep_train, eval_set=[(indep_test, dep_test)],  verbose=False, early_stopping_rounds=50);

# res를 기반으로 gs1 데이터셋 예측 수행
g = gs1.predict(res)

# cvscores에 accuracy_score -> 부분 집합 정확도를 계산해서 추가
a = accuracy_score(dep_test, gs1.predict(indep_test))
b = accuracy_score(dep_train, gs1.predict(indep_train))
#cv = cross_val_score(gs1, indep_train, dep_train, cv=5)
print(a, b)












### 33

# zip -> indep.columns과 gs1의 feature_importances_(변수중요도)를 묶어줌 
attr2 = {k: v for k, v in zip(indep.columns, gs1.feature_importances_) if v>0}

# 중요도가 낮은순으로 정렬
attr2 = sorted(attr2.items(), key=lambda x: x[1], reverse = False)

# x1과 y1에 attr2의 컬럼을 각각 분리해서 넣음
x1,y1 = zip(*attr2)


i1=range(len(x1))   # range(0, 42) 컬럼의 갯수

# 새로운 피규어 생성
plt.figure(num=None, figsize=(9, 8), dpi=300, facecolor='w', edgecolor='k')

# 가로 막대그래프 생성
plt.barh(i1, y1)

# 그래프 제목설정
plt.title("CatBoost")

# y축 눈금값 설정
plt.yticks(i1, x1)
plt.show();










### 34 

model = []     # model 리스트 변수 생성
cvscores = []   # cvscores 리스트 변수 생성
for i in range(0, 90):  # 90회 반복하며 학습함

    # train_test_split -> 배열 또는 행렬을 임의 학습 및 테스트 하위 집합으로 분할
    # test_size=0.40 -> float 인 경우 0.0에서 1.0 사이 여야하며 테스트 분할에 포함 할 데이터 세트의 비율, int 인 경우 테스트 샘플의 절대 수를 나타냄
    # random_state -> 렌덤함수의 스피드(수치를 바꾸면 렌덤데이터를 추출하는 레코드값이 달라짐)
    indep_train, indep_test, dep_train, dep_test = train_test_split(indep, dep, test_size=0.40, random_state=i)

    # cb.CatBoostClassifier -> 모델생성 
    # depth -> 기본 학습자의 최대 트리 깊이 
    # reg_lambda -> L2 정규화. 과적합을 방지할수 있지만, 정확도를 저하시킬수 있기때문에 일반적으로 디폴트값이 0을 사용
    # learning_rate -> 학습 스텝의 크기 
    # iterations -> 나무를 반복하며 부스팅 하는데 몇번을 반복할것인가
    gs1 = cb.CatBoostClassifier(depth = 9, reg_lambda=0.1,
                     learning_rate = 0.09, 
                     iterations = 500)

    # 데이터학습용 파라미터 입력
    # eval_set -> 검증용 세트 지정 / verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
    # early_stopping_rounds -> 조기 중단을 위한 라운드를 설정                     
    gs1.fit(indep_train, dep_train, eval_set=[(indep_test, dep_test)],  verbose=False, early_stopping_rounds=50);


    model.append(gs1)   # gs1 데이터를 model에 삽입

    # accuracy_score -> 부분 집합 정확도를 계산
    # 정확도 계산값을 cvscores에 삽입
    cvscores.append(accuracy_score(dep_test, gs1.predict(indep_test)))
    
data = pd.DataFrame()   # data 데이타 프레임생성
te = pd.DataFrame()     # te 데이타 프레임생성

for i in range(0, 90):

    # res 데이터를 기반으로한 예측
    data[i] = model[i].predict(res)

    # indep_test 데이터를 기반으로한 예측
    te[i] = model[i].predict(indep_test)

# data의 데이터중 행의 평균값을 구하고 반올림
g = np.round(data.mean(axis=1))

# data의 데이터중 행의 평균값을 구하고 반올림
t = np.round(te.mean(axis=1))

# cvscores 데이터의 평균값
cb_mean = np.mean(cvscores)

# cvscores 데이터의 표준편차
cb_stdev = np.std(cvscores)
print(cb_mean, cb_stdev)










### 35

#result = pd.DataFrame(res_index.astype(np.int), columns=["PassengerId"])
#result["Survived"] = g.astype(np.int)
#result.to_csv(r"c:\work\dataset\titanic\catboost.csv", ",", index=None)
#result.to_csv("catboost.csv", ",", index=None)



























### Model 4. XGBoost
### 36

# xgb.XGBClassifier -> 모델생성 
# max_depth = 9 -> 기본 학습자의 최대 트리 깊이 9
# learning_rate = 0.01 -> 학습 스텝의 크기 /  n_estimators -> 생성할 트리의 개수
# reg_alpha -> 가중치에 대한 L1 정규화 항. 이 값을 늘리면 모델이 더 보수적이 됨
# colsample_bytree -> 개별 의사결정나무 모형에 사용될 변수갯수를 지정. 보통 0.5 ~ 1 사용됨. 기본값 1
# subsample -> 개별 의사결정나무 모형에 사용되는 임의 표본수를 지정. 보통 0.5 ~ 1 사용됨
# n_jobs -> xgboost를 실행하는 데 사용되는 병렬 스레드 수. 그리드 검색과 같은 다른 Scikit-Learn 알고리즘과 함께 사용하는 경우 스레드를 병렬화하고 균형을 조정할 알고리즘을 선택할 수 있습니다. 스레드 경합을 만들면 두 알고리즘이 크게 느려집니다.
gs1 = xgb.XGBClassifier(max_depth = 9,
                         learning_rate = 0.01, 
                         n_estimators = 500, reg_alpha = 1.1, colsample_bytree = 0.9, subsample = 0.9,
                         n_jobs = 5)

# 데이터학습용 파라미터 입력
# eval_set -> 검증용 세트 지정 / verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
# early_stopping_rounds -> 조기 중단을 위한 라운드를 설정
gs1.fit(indep_train, dep_train, eval_set=[(indep_test, dep_test)],  verbose=False, early_stopping_rounds=50);

# res를 기반으로 gs1 데이터셋 예측 수행
g = gs1.predict(res)

# accuracy_score -> 부분 집합 정확도를 계산
a = accuracy_score(dep_test, gs1.predict(indep_test))
b = accuracy_score(dep_train, gs1.predict(indep_train))
print(a, b)









### 37


# zip -> indep.columns과 gs1의 feature_importances_(변수중요도)를 묶어줌 
attr2 = {k: v for k, v in zip(indep.columns, gs1.feature_importances_) if v>0}

# 중요도가 낮은순으로 정렬
attr2 = sorted(attr2.items(), key=lambda x: x[1], reverse = False)

# x1과 y1에 attr2의 컬럼을 각각 분리해서 넣음
x1,y1 = zip(*attr2)

i1=range(len(x1))   # range(0, 35) 컬럼의 갯수

# 새로운 피규어 생성
plt.figure(num=None, figsize=(9, 7), dpi=300, facecolor='w', edgecolor='k')

# 가로 막대그래프 생성
plt.barh(i1, y1)

# 그래프 제목설정
plt.title("XGBoost")

# y축 눈금값 설정
plt.yticks(i1, x1)
plt.show();









### 38

model = []  # model 리스트 변수 생성
cvscores = [] # cvscores 리스트 변수 생성

for i in range(0, 90):  # 90회 반복하며 학습함
    # train_test_split -> 배열 또는 행렬을 임의 학습 및 테스트 하위 집합으로 분할
    # test_size=0.40 -> float 인 경우 0.0에서 1.0 사이 여야하며 테스트 분할에 포함 할 데이터 세트의 비율, int 인 경우 테스트 샘플의 절대 수를 나타냄
    # random_state -> 렌덤함수의 스피드(수치를 바꾸면 렌덤데이터를 추출하는 레코드값이 달라짐)
    indep_train, indep_test, dep_train, dep_test = train_test_split(indep, dep, test_size=0.40, random_state=i)
    
    # xgb.XGBClassifier -> 모델생성 
    # max_depth -> 기본 학습자의 최대 트리 깊이 / reg_lambda -> 가중치에 대한 L2 정규화 항. 이 값을 늘리면 모델이 더 보수적이 됨
    # learning_rate -> 학습 스텝의 크기 /  n_estimators -> 생성할 트리의 개수
    # reg_alpha -> 가중치에 대한 L1 정규화 항. 이 값을 늘리면 모델이 더 보수적이 됨
    # colsample_bytree -> 개별 의사결정나무 모형에 사용될 변수갯수를 지정. 보통 0.5 ~ 1 사용됨. 기본값 1
    # subsample -> 개별 의사결정나무 모형에 사용되는 임의 표본수를 지정. 보통 0.5 ~ 1 사용됨
    # n_jobs -> xgboost를 실행하는 데 사용되는 병렬 스레드 수. 그리드 검색과 같은 다른 Scikit-Learn 알고리즘과 함께 사용하는 경우 스레드를 병렬화하고 균형을 조정할 알고리즘을 선택할 수 있습니다. 스레드 경합을 만들면 두 알고리즘이 크게 느려집니다.
    gs1 = xgb.XGBClassifier(max_depth = 7, reg_lambda = 0.02,
                         learning_rate = 0.01, 
                         n_estimators = 5000, reg_alpha = 1.1, colsample_bytree = 0.9, subsample = 0.9,
                         n_jobs = 5)
    
    # 데이터학습용 파라미터 입력
    # eval_set -> 검증용 세트 지정 / verbose -> 평가단계에서 인쇄여부 1=true 매번인쇄, 100=100회 반복마다 인쇄
    # early_stopping_rounds -> 조기 중단을 위한 라운드를 설정
    gs1.fit(indep_train, dep_train, eval_set=[(indep_test, dep_test)], verbose=False, early_stopping_rounds=50);
    
    model.append(gs1)   # gs1 데이터를 model에 삽입
    
    # accuracy_score -> 부분 집합 정확도를 계산
    # 정확도 계산값을 cvscores에 삽입
    cvscores.append(accuracy_score(dep_test, gs1.predict(indep_test)))


data = pd.DataFrame()   # data 데이타 프레임생성
te = pd.DataFrame()   # te 데이타 프레임생성


for i in range(0, 90):
    
    # res 데이터를 기반으로한 예측
    data[i] = model[i].predict(res)
    # indep_test 데이터를 기반으로한 예측
    te[i] = model[i].predict(indep_test)


# data의 데이터중 행의 평균값을 구하고 반올림
g = np.round(data.mean(axis=1))

# te의 데이터중 행의 평균값을 구하고 반올림
t = np.round(te.mean(axis=1))

# cvscores 데이터의 평균값
xgb_mean = np.mean(cvscores)

# cvscores 데이터의 표준편차
xgb_stdev = np.std(cvscores)
print(xgb_mean, xgb_stdev)






### 39

#result = pd.DataFrame(res_index.astype(np.int), columns=["PassengerId"])
#result["Survived"] = g.astype(np.int)
#result.to_csv(r"c:\work\dataset\titanic\xgb.csv", ",", index=None)
#result.to_csv("lgbm.csv", ",", index=None)







### 40

d = {'Model':["Keras MLP", "LightGBM", "CatBoost", "XGBoost"], 
     'Mean accuracy': [mlp_mean, lgb_mean, cb_mean, xgb_mean], 
     'Std. Dev.': [mlp_stdev, lgb_stdev, cb_stdev, xgb_stdev],
    'Leaderboard': [0.77033, 0.82296, 0.78947, 0.77511]}
pd.DataFrame(data=d, columns=["Model", "Mean accuracy", "Std. Dev.", "Leaderboard"]).sort_values("Mean accuracy", ascending=False).head(10)
