# 모듈
import A007_movie          # 만들어 놓은(다른 파일에 있는) movie 모듈 호출

A007_movie.price(3)
A007_movie.price_morning(4)
A007_movie.price_soldier(5)

import A007_movie as mv      # movie 모듈이름을 mv로 변경해서 호출

mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)


from A007_movie import *     # 모듈이름을 안쓰고 함수만 바로 사용 가능
price(3)
price_morning(4)
price_soldier(5)


from A007_movie import price, price_morning      # price와 price_morning만 호출
price(3)
price_morning(4)
price_soldier(5)            # 에러남


from A007_movie import price_soldier as price    # 이름 바꿔서 호출
price(5)    # 솔져 가격이 나옴





# 패키지
import travel.thailand      # 경로가 다를경우 경로를 적어줘야함
# travel폴더에 있는 thailand라는 파일
trip_to = travel.thailand.ThailandPackage()     # 변수에 클레스를 넣음
trip_to.detail()


from travel import vietnam      # 베트남 호출
trip_to = vietnam.VietnamPackage()
trip_to.detail()

from travel import *    # 베트남과 타일렌드 모두 호출


# 모듈 위치 확인
import inspect      # 위치 확인하는 모듈
import random
print(inspect.getfile(random))
#print(inspect.getabsfile(vietnam))


# input - 사용자 입력을 받는 함수
language = input("어떤 언어를 좋아하나요 : ")
print('{0}은 아주 좋은 언어입니다.'.format(language))





# dir - 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수의 함수를 가지고 있는지
print(dir())
import random
print(dir())

import random
import pickle
print(dir())
print(dir(pickle))
print(dir(random))


lst = [1, 2, 3, 4, 5]
print(dir(lst))

name = "edushare"
print(dir(name))





from datetime import *

# 내장함수
glob # 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir)
os # 운영체제에서 제공하는 기본 기능
time # 시간 관련 함수
timedelta # 두 날짜 사이의 간격
import glob
print(glob.glob('AH_class-quiz.py'))
import os
print(os.getcwd())  # 현재 디렉토리를 알려줌( 리눅스의 pwd )

folder = "sample_dir"
if os.path.exists(folder):
    print("이미 존재하는 폴더입니다")
    os.rmdir(folder)
    print(folder, "폴더를 삭제했습니다.")
else:
    os.mkdir(folder)  # 폴더 생성
    print(folder, "폴더를 생성했습니다")

print(os.listdir()) # 목록보기



import time
print(time.localtime())     # 현재시간
print(time.strftime("%y-%m-%d %H:%M:%S"))   # 형식을 지정하는 함수


import datetime
print("오늘 날짜는 ", datetime.date.today())

today = datetime.date.today()   # 오늘 날짜 저장
td = datetime.timedelta(days=100)   # 100일 저장
print("우리가 만난지 100일", today + td) # 오늘부터 100일 후
































