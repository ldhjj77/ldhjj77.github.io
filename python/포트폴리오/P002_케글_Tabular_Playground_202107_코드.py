


## 1


import pandas as pd
import numpy as np
import seaborn as sns   # 통계 데이터 시각화 패키지
import matplotlib.pyplot as plt     # 대화 형 플롯과 간단한 프로그래밍 플롯 생성
import time     # 시간데이터 처리용 모듈
import warnings     # 경고 메시지를 출력하고 걸러내는 모듈
# simplefilter -> 간단한 항목으로 이뤄진 제어문
# 'ignore -> 일치하는 경고를 인쇄하지 않음
# FutureWarning -> 폐지된 기능에 대한 경고의 베이스 범주
warnings.simplefilter(action='ignore', category=FutureWarning)














## 2


train = pd.read_csv('../input/tabular-playground-series-jul-2021/train.csv')
train   # 7111열의 데이터가 있음











## 3



test = pd.read_csv('../input/tabular-playground-series-jul-2021/test.csv')
test    # 2247열의 데이터가 있음










## 4


# concat -> 인자로 주어진 배열이나 값들을 기존 배열에 합쳐서 새 배열을 반환
# 기존배열을 변경하지 않고 추가된 새로운 배열을 반환
all_data = pd.concat([train, test])
all_data    # 9358열의 데이터가 있음











## 5


all_data.info()     # 합친 데이터 정보보기











## 6


# to_datetime -> 데이터프레임을 datetime 으로 변환
# 'date_time' 컬럼의 내용을 datetime으로 변환후 추가
all_data['date_time'] = pd.to_datetime(all_data['date_time'])

# 'year' 컬럼을 생성하고 'date_time' 데이터의 년도 데이터를 추가
all_data['year'] = all_data['date_time'].dt.year

# 'month' 컬럼을 생성하고 'date_time' 데이터의 월 데이터를 추가
all_data['month'] = all_data['date_time'].dt.month

# 'week' 컬럼을 생성하고 'date_time' 데이터의 주 데이터를 추가
all_data['week'] = all_data['date_time'].dt.week

# 'day' 컬럼을 생성하고 'date_time' 데이터의 일 데이터를 추가
all_data['day'] = all_data['date_time'].dt.day

# 'dayofweek' 컬럼을 생성하고 'date_time' 데이터에서 요일 구분을 위한 데이터 추가
all_data['dayofweek'] = all_data['date_time'].dt.dayofweek

# 'time' 컬럼을 생성하고 'date_time' 데이터에서 몇일차인지의 데이터를 추가
# 현재날짜 - 데이터첫번째 날짜
all_data['time'] = all_data['date_time'].dt.date - all_data['date_time'].dt.date.min()

# 'hour' 컬럼을 생성하고 'date_time' 데이터의 시간 데이터를 추가
all_data['hour'] = all_data['date_time'].dt.hour

# 'time' 컬럼의 내용중 일 데이터만 추가(몇일차데이터 삽입)
all_data['time'] = all_data['time'].apply(lambda x : x.days)

# 'date_time' 컬럼 삭제
all_data.drop(columns = 'date_time', inplace = True)
all_data












## 7



# 'dayofweek'의 데이터타입을 object로 변환
all_data['dayofweek'] = all_data['dayofweek'].astype(object)

# get_dummies -> 가변수화 
# 문자형을 수치형으로 바꾸기만 했을경우 관계성으로 인한 학습에러를 방지하기위해 가변수화의 과정이 필요함
all_data = pd.get_dummies(all_data)










## 8



# all_data['SMC'] = (all_data['absolute_humidity'] * 100) / all_data['relative_humidity']
# all_data['Dew_Point'] = 243.12*(np.log(all_data['relative_humidity'] * 0.01) + (17.62 * all_data['deg_C'])/(243.12+all_data['deg_C']))/(17.62-(np.log(all_data['relative_humidity'] * 0.01)+17.62*all_data['deg_C']/(243.12+all_data['deg_C'])))
# all_data['relative_humidity'] = all_data['relative_humidity']/100
# all_data['deg_F'] = all_data['deg_C'] * 1.8 + 32











## 9




# 데이터 분리
# train2 변수에 train의 열의 수만큼 all_data의 데이터를 추가
train2 = all_data[:len(train)]

# test2 변수에 train의 열의 수만큼 건너뛰고 all_data의 데이터를 추가
test2 = all_data[len(train):]
# train['SMC'] = train2['SMC']











## 10


# 편차값을 줄이기위한 로그 스케일링 함수 생성
def log_scaling(col):
    # log1p -> 0의 로그값을 구하려고 하면 에러가 나기때문에 원본에1을 더한다음 로그스케일링을 진행하도록 하는함수
  col = np.log1p(col)
  return col











## 11


# cols 차트 리스트 생성
cols = ['target_carbon_monoxide', 'target_benzene', 'target_nitrogen_oxides']
for col in cols:
    # train2에 col 칼럼에 col의 내용을 로그스케일링 한 데이터를 추가 
  train2[col] = log_scaling(train2[col])











## 12




# Figure 객체를 생성하고 len(cols)=3 *2 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(len(cols), 2, figsize=(12,12))
n = 0
for i in cols:
    # histplot -> 변수에 대한 히스토그램
    # 하나 혹은 두 개의 변수 분포를 나타내는 전형적인 시각화 도구로 범위에 포함화는 관측수를 세어 표시
    # train[cols] 값에대한 단순그래프
    # ax -> 그래프 생성위치 설정
  sns.histplot(train[i], ax=ax[n, 0]);

    # train2[cols] 값에대한 단순그래프
  sns.histplot(train2[i], ax = ax[n, 1]);
  n += 1

# tight_layout -> 여백설정과 레이아웃 설정을 해줌
fig.tight_layout()
plt.show()












## 13



# train_3에다가 train2의 데이타중 다음 3개의 칼럼'target_carbon_monoxide', 'target_benzene', 'target_nitrogen_oxides' 을 삭제후 추가
train_3 = train2.drop(columns = ['target_carbon_monoxide', 'target_benzene', 'target_nitrogen_oxides'])

# test_3에다가 test2의 데이타중 다음 3개의 칼럼'target_carbon_monoxide', 'target_benzene', 'target_nitrogen_oxides' 을 삭제후 추가
test_3 = test2.drop(columns = ['target_carbon_monoxide', 'target_benzene', 'target_nitrogen_oxides'])

# train_co에다가 train2의 데이타중 다음 2개의 칼럼 'target_benzene', 'target_nitrogen_oxides' 을 삭제후 추가
train_co = train2.drop(columns = ['target_benzene', 'target_nitrogen_oxides'])

# train_be에다가 train2의 데이타중 다음 2개의 칼럼 'target_carbon_monoxide', 'target_nitrogen_oxides' 을 삭제후 추가
train_be = train2.drop(columns = ['target_carbon_monoxide', 'target_nitrogen_oxides'])

# train_no에다가 train2의 데이타중 다음 2개의 칼럼 'target_carbon_monoxide', 'target_benzene' 을 삭제후 추가
train_no = train2.drop(columns = ['target_carbon_monoxide', 'target_benzene'])

# test_co에다가 test2의 데이타중 다음 2개의 칼럼'target_benzene', 'target_nitrogen_oxides' 을 삭제후 추가
test_co = test2.drop(columns = ['target_benzene', 'target_nitrogen_oxides'])

# test_be에다가 test2의 데이타중 다음 2개의 칼럼'target_carbon_monoxide', 'target_nitrogen_oxides' 을 삭제후 추가
test_be = test2.drop(columns = ['target_carbon_monoxide', 'target_nitrogen_oxides'])

# test_no에다가 test2의 데이타중 다음 2개의 칼럼'target_carbon_monoxide', 'target_benzene' 을 삭제후 추가
test_no = test2.drop(columns = ['target_carbon_monoxide', 'target_benzene'])










## 14


# Figure 객체를 생성하고 4*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(4, 3, figsize = (12,10))

# ax -> 그래프 생성위치 설정
# x축은 'year'(년도단위) y축은 'target_carbon_monoxide' 의 평균값을 'r' (red) 빨간색으로 표시
ax[0,0].plot(train2.groupby(train2['year'])['target_carbon_monoxide'].mean(), 'r');

# 'target_benzene' 의 평균값
ax[0,1].plot(train2.groupby(train2['year'])['target_benzene'].mean(), 'r');

# 'target_nitrogen_oxides' 의 평균값
ax[0,2].plot(train2.groupby(train2['year'])['target_nitrogen_oxides'].mean(), 'r');


# x축은 'month'(월단위) y축은 'target_carbon_monoxide' 의 평균값을 'b' (blue) 파란색으로 표시
ax[1,0].plot(train2.groupby(train2['month'])['target_carbon_monoxide'].mean(), 'b');

# 'target_benzene' 의 평균값
ax[1,1].plot(train2.groupby(train2['month'])['target_benzene'].mean(), 'b');

# 'target_nitrogen_oxides' 의 평균값
ax[1,2].plot(train2.groupby(train2['month'])['target_nitrogen_oxides'].mean(), 'b');


# x축은 'time'(몇일차) y축은 'target_carbon_monoxide' 의 평균값을 'y' (yellow) 노란색으로 표시
ax[2,0].plot(train2.groupby(train2['time'])['target_carbon_monoxide'].mean(), 'y');

# 'target_benzene' 의 평균값
ax[2,1].plot(train2.groupby(train2['time'])['target_benzene'].mean(), 'y');

# 'target_nitrogen_oxides' 의 평균값
ax[2,2].plot(train2.groupby(train2['time'])['target_nitrogen_oxides'].mean(), 'y');

# x축은 'hour'(시간) y축은 'target_carbon_monoxide' 의 평균값을 'black' 검은색으로 표시
ax[3,0].plot(train2.groupby(train2['hour'])['target_carbon_monoxide'].mean(), 'black');

# 'target_benzene' 의 평균값
ax[3,1].plot(train2.groupby(train2['hour'])['target_benzene'].mean(), 'black');

# 'target_nitrogen_oxides' 의 평균값
ax[3,2].plot(train2.groupby(train2['hour'])['target_nitrogen_oxides'].mean(), 'black');


# 그래프 제목설정
ax[0,0].set_title('Year-CO')
ax[0,1].set_title('Year-Benzene')
ax[0,2].set_title('Year-NOx')

ax[1,0].set_title('month-CO')
ax[1,1].set_title('month-Benzene')
ax[1,2].set_title('month-NOx')

ax[2,0].set_title('time-CO')
ax[2,1].set_title('time-Benzene')
ax[2,2].set_title('time-NOx')

ax[3,0].set_title('hour-CO')
ax[3,1].set_title('hour-Benzene')
ax[3,2].set_title('hour-NOx')

# tight_layout -> 여백설정과 레이아웃 설정을 해줌
fig.tight_layout()
plt.show()









## 15


# Figure 객체를 생성하고 3*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(3, 3, figsize = (10,10))

# ax -> 그래프 생성위치 설정
# x축은 'deg_C' y축은 'target_carbon_monoxide' 의 평균값을 'r' (red) 빨간색으로 표시
ax[0,0].plot(train2.groupby(train2['deg_C'])['target_carbon_monoxide'].mean(), 'r');

# 'target_benzene' 의 평균값
ax[0,1].plot(train2.groupby(train2['deg_C'])['target_benzene'].mean(), 'r');

# 'target_nitrogen_oxides' 의 평균값
ax[0,2].plot(train2.groupby(train2['deg_C'])['target_nitrogen_oxides'].mean(), 'r');


# x축은 'relative_humidity' y축은 'target_carbon_monoxide' 의 평균값을 'b' (blue) 파란색으로 표시
ax[1,0].plot(train2.groupby(train2['relative_humidity'])['target_carbon_monoxide'].mean(), 'b');

# 'target_benzene' 의 평균값
ax[1,1].plot(train2.groupby(train2['relative_humidity'])['target_benzene'].mean(), 'b');

# 'target_nitrogen_oxides' 의 평균값
ax[1,2].plot(train2.groupby(train2['relative_humidity'])['target_nitrogen_oxides'].mean(), 'b');


# x축은 'absolute_humidity' y축은 'target_carbon_monoxide' 의 평균값을 'y' (yellow) 노란색으로 표시
ax[2,0].plot(train2.groupby(train2['absolute_humidity'])['target_carbon_monoxide'].mean(), 'y');

# 'target_benzene' 의 평균값
ax[2,1].plot(train2.groupby(train2['absolute_humidity'])['target_benzene'].mean(), 'y');

# 'target_nitrogen_oxides' 의 평균값
ax[2,2].plot(train2.groupby(train2['absolute_humidity'])['target_nitrogen_oxides'].mean(), 'y');


# 그래프 제목설정
ax[0,0].set_title('deg-CO')
ax[0,1].set_title('deg-Benzene')
ax[0,2].set_title('deg-NOx')

ax[1,0].set_title('rel_humid-CO')
ax[1,1].set_title('rel_humid-Benzene')
ax[1,2].set_title('rel_humid-NOx')

ax[2,0].set_title('ab_humid-CO')
ax[2,1].set_title('ab_humid-Benzene')
ax[2,2].set_title('ab_humid-NOx')

# tight_layout -> 여백설정과 레이아웃 설정을 해줌
fig.tight_layout()
plt.show()










## 16

# Figure 객체를 생성하고 3*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(5, 3, figsize = (10,13))

# ax -> 그래프 생성위치 설정
# x축은 'sensor_1' y축은 'target_carbon_monoxide' 의 평균값을 'r' (red) 빨간색으로 표시
ax[0,0].plot(train2.groupby(train2['sensor_1'])['target_carbon_monoxide'].mean(), 'r');

# 'target_benzene' 의 평균값
ax[0,1].plot(train2.groupby(train2['sensor_1'])['target_benzene'].mean(), 'r');

# 'target_nitrogen_oxides' 의 평균값
ax[0,2].plot(train2.groupby(train2['sensor_1'])['target_nitrogen_oxides'].mean(), 'r');


# x축은 'sensor_2' y축은 'target_carbon_monoxide' 의 평균값을 'b' (blue) 파란색으로 표시
ax[1,0].plot(train2.groupby(train2['sensor_2'])['target_carbon_monoxide'].mean(), 'b');

# 'target_benzene' 의 평균값
ax[1,1].plot(train2.groupby(train2['sensor_2'])['target_benzene'].mean(), 'b');

# 'target_nitrogen_oxides' 의 평균값
ax[1,2].plot(train2.groupby(train2['sensor_2'])['target_nitrogen_oxides'].mean(), 'b');


# x축은 'sensor_3' y축은 'target_carbon_monoxide' 의 평균값을 'y' (yellow) 노란색으로 표시
ax[2,0].plot(train2.groupby(train2['sensor_3'])['target_carbon_monoxide'].mean(), 'y');

# 'target_benzene' 의 평균값
ax[2,1].plot(train2.groupby(train2['sensor_3'])['target_benzene'].mean(), 'y');

# 'target_nitrogen_oxides' 의 평균값
ax[2,2].plot(train2.groupby(train2['sensor_3'])['target_nitrogen_oxides'].mean(), 'y');


# x축은 'sensor_4' y축은 'target_carbon_monoxide' 의 평균값을 'black'  검은색으로 표시
ax[3,0].plot(train2.groupby(train2['sensor_4'])['target_carbon_monoxide'].mean(), 'black');

# 'target_benzene' 의 평균값
ax[3,1].plot(train2.groupby(train2['sensor_4'])['target_benzene'].mean(), 'black');

# 'target_nitrogen_oxides' 의 평균값
ax[3,2].plot(train2.groupby(train2['sensor_4'])['target_nitrogen_oxides'].mean(), 'black');


# x축은 'sensor_5' y축은 'target_carbon_monoxide' 의 평균값을 'violet'  보라색으로 표시
ax[4,0].plot(train2.groupby(train2['sensor_5'])['target_carbon_monoxide'].mean(), 'violet');

# 'target_benzene' 의 평균값
ax[4,1].plot(train2.groupby(train2['sensor_5'])['target_benzene'].mean(), 'violet');

# 'target_nitrogen_oxides' 의 평균값
ax[4,2].plot(train2.groupby(train2['sensor_5'])['target_nitrogen_oxides'].mean(), 'violet');


# 그래프 제목설정
ax[0,0].set_title('sensor_1-CO')
ax[0,1].set_title('sensor_1-Benzene')
ax[0,2].set_title('sensor_1-NOx')

ax[1,0].set_title('sensor_2-CO')
ax[1,1].set_title('sensor_2-Benzene')
ax[1,2].set_title('sensor_2-NOx')

ax[2,0].set_title('sensor_3-CO')
ax[2,1].set_title('sensor_3-Benzene')
ax[2,2].set_title('sensor_3-NOx')

ax[3,0].set_title('sensor_4-CO')
ax[3,1].set_title('sensor_4-Benzene')
ax[3,2].set_title('sensor_4-NOx')

ax[4,0].set_title('sensor_5-CO')
ax[4,1].set_title('sensor_5-Benzene')
ax[4,2].set_title('sensor_5-NOx')


# tight_layout -> 여백설정과 레이아웃 설정을 해줌
fig.tight_layout()
plt.show()








## 17

plt.figure(figsize=(12,12))
# heatmap -> X축과 Y축에 2개의 범주형 자료의 계급(class)별로 연속형 자료를 집계한 자료를 사용하여, 집계한 값에 비례하여 색깔을 다르게 해서 2차원으로 자료를 시각화
# corr -> correlation(상관관계)
sns.heatmap(train2.corr());







## 18


# Figure 객체를 생성하고 3*3 subplot에 대응하는 Figure 객체와 Axes 객체의 리스트를 리턴
fig, ax = plt.subplots(3, 3, figsize = (20,15))


# boxplot -> 상자 그림 그래프
# 자료로부터 얻어낸 통계량인 5가지 요약 수치로 그림
# ax -> 그래프 생성위치 설정
# x축은 'year'(년단위) y축은 'target_carbon_monoxide' 을 사용
sns.boxplot(train2['year'], train2['target_carbon_monoxide'], ax = ax[0, 0]);

# y축을 'target_benzene' 을 사용
sns.boxplot(train2['year'], train2['target_benzene'], ax= ax[0, 1]);

# y축을 'target_nitrogen_oxides' 을 사용
sns.boxplot(train2['year'], train2['target_nitrogen_oxides'], ax = ax[0, 2]);


# x축은 'month'(월단위) y축은 'target_carbon_monoxide' 을 사용
sns.boxplot(train2['month'], train2['target_carbon_monoxide'], ax = ax[1, 0]);

# y축을 'target_benzene' 을 사용
sns.boxplot(train2['month'], train2['target_benzene'], ax= ax[1, 1]);

# y축을 'target_nitrogen_oxides' 을 사용
sns.boxplot(train2['month'], train2['target_nitrogen_oxides'], ax = ax[1, 2]);


# x축은 'hour'(시간대별단위) y축은 'target_carbon_monoxide' 을 사용
sns.boxplot(train2['hour'], train2['target_carbon_monoxide'], ax = ax[2,0]);

# y축을 'target_benzene' 을 사용
sns.boxplot(train2['hour'], train2['target_benzene'], ax= ax[2,1]);

# y축을 'target_nitrogen_oxides' 을 사용
sns.boxplot(train2['hour'], train2['target_nitrogen_oxides'], ax = ax[2,2]);

plt.show();









## 19

# 모델링


# 파이케럿설치 / 코드를 처음 실행하는 경우라면 주석을지우고 한번 설치해야함
# !pip install pycaret







## 20


# pycaret.regression -> 파이케럿 초기화
# setup -> 환경설정
# compare_models -> 모델성능비교
# blend_models -> 블렌드 모델(혼합모델)
# finalize_model -> 모델 완성
# predict_model -> 예측 모델
# plot_model -> 모델의 성능을 분석
from pycaret.regression import setup, compare_models, blend_models, finalize_model, predict_model, plot_model







## 21



# 모델함수 생성

# train ->데이터셋, target -> 컬럼, test -> 테스트용 데이터셋
# n_select -> 성능평가후 상위 몇개의 모델을 반환 할것인가(5개 5개 4개를 사용)
# opt -> 정렬옵션 설정 ( 'RMSLE' 사용 )
def pycaret_model(train, target, test, n_select, fold, opt):
  print('Setup Your Data....')
  # 환경 설정값
  setup(data=train,     # 데이터로 쓸 데이터 설정 
              target=target,    # 데이터내의 어떤값을 쓸것인가
              numeric_imputation = 'mean',  # 결측값(nan등)에 평균값 입력
              silent= True) # 에러메시지 침묵시킴
  
  print('Comparing Models....')
  # compare_models -> 모델을 비교해서 최고성능의 모델을 찾음
  # sort=opt -> 정렬 옵션(매개변수로 정의해놓은 상태 / 'RMSLE' 사용됨)
  # n_select -> 최상위 모델 한개만 반환
  # fold -> 데이터셋의 숫자(매개변수로 정의해놓은 상태 / 3개 사용됨)
  # exclude -> 블렉리스트 / include -> 해당모델만 비교
  best = compare_models(sort=opt, n_select=n_select, fold = fold, exclude = ['xgboost'])


  print('Here is Best Model Feature Importances!')

  # plot_model -> 모델의 성능분석
  # estimator -> 측정자 / 'feature' -> Feature Importance(기능 중요도)
  # time.sleep(5) -> 5초간 대기
  plot_model(estimator = best[0], plot = 'feature')
  time.sleep(5)
  

  print('Blending Models....')

  # blend_models -> 블렌드 모델(혼합모델-추정자 간의 합의를 사용하여 최종 예측을 생성)
  # estimator_list -> 추정자 리스트
  # fold -> 데이터셋의 숫자(매개변수로 정의해놓은 상태 / 3개 사용됨)
  # optimize -> 정렬옵션('RMSLE'가 사용됨)
  blended = blend_models(estimator_list= best, fold=fold, optimize=opt)

  # predict_model -> 정확도 예측(blend_models 사용)
  pred_holdout = predict_model(blended)
    

  print('Finallizing Models....')

  # finalize_model -> 모델 완성(blend_models 사용)
  final_model = finalize_model(blended)
  print('Done...!!!')

  # 최종 예측
  pred_esb = predict_model(final_model, test)
  re = pred_esb['Label']

  return re







## 22


# 셈플데이터 불러오기
sub = pd.read_csv('../input/tabular-playground-series-jul-2021/sample_submission.csv')

# sub의 'target_carbon_monoxide' 칼럼에 train_co의 'target_carbon_monoxide' 칼럼을 test_co 를 사용해서 최종예측값을 내고 그값의 지수값을 추가
sub['target_carbon_monoxide'] = np.exp(pycaret_model(train_co, 'target_carbon_monoxide', test_co, 5, 3, 'RMSLE'))-1







## 23


# sub의 'target_benzene' 칼럼에 train_be의 'target_benzene' 칼럼을 test_co 를 사용해서 최종예측값을 내고 그값의 지수값을 추가
sub['target_benzene'] = np.exp(pycaret_model(train_be, 'target_benzene', test_be, 5, 3, 'RMSLE'))-1







## 23


# sub의 'target_nitrogen_oxides' 칼럼에 train_no의 'target_nitrogen_oxides' 칼럼을 test_co 를 사용해서 최종예측값을 내고 그값의 지수값을 추가
sub['target_nitrogen_oxides'] = np.exp(pycaret_model(train_no, 'target_nitrogen_oxides', test_no, 4, 3, 'RMSLE')) - 1








## 25

sub








## 26

sub.to_csv('sub.csv', index=False)

