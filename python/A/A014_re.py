# regix expression( 정규식 표현 ) 주민번호로 남여 구분을 해야하는 등의 경우에 사용
# 주민등록번호 123456-1234567
# 이메일 주소 1234@1234.123
# 차량 번호 12가 3456
# IP주소

import re
# abcd, book, desk
# care, cafe, case, cave, cade, coffe, caae

p = re.compile("ca.e")      # ca.e 에서 . 은 정규표현식
# . : 하나의 문자를 의미    care, cafe, case, cave, cade, caae
p = re.compile("^de")   
# ^ : 시작하는 문자열 (de로 시작하는 문자 추출) desk
p = re.compile("se$")
# $ : 끝나는 문자열(se로 끝나는 문자 추출)  case

def print_match(m):
    if m:
        print(m.group())        # group은 묶어주는 함수
        print(m.string())       # 입력받은 문자열
        print(m.start())        # 일치하는 문자열의 시작 인덱스값을 가져옴
        print(m.end())          # 일치하는 문자열의 끝 인덱스값을 가져옴
        print(m.span())         # 일치하는 문자열의 시작과 끝의 인덱스값을 가져옴
    else:
        print("매칭되지 않음")


lst = p.findall('good care cafe')   # findall = 일치하는 모든것들을 리스트로 저장
# lst = [care, cafe] 가 나옴
lst = p.search('careless')  # 문자열중에 일치하는것이 있는지 확인 care
m = p.search('careless')

# re.compile = 정규식(원하는 형태로)
# .match - 문자열의 처음부터 일치하는가
# .search - 문자열 중에 일치하는게 있는가
# .findall - 일치하는 모든 문자열을 리스트로 반환


# http Method
# - request - GET / POST
import requests         # 터미널창에 pip install requests 입력해서 설치 필요
from requests import status_codes
url = 'http://coupang.com'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
res = requests.get(url, headers=headers)
res.raise_for_status()

# res = requests.get('http://naver.com')
# res.raise_for_status()
# print('응답 코드 : ', res.status_code)

if res.status_code -- requests.codes.ok:
    print('정상입니다.')
else:
    print('문제가 생겼습니다.[에러코드 ', res.status_code, ']')

print(len(res.text))
print(res.text)

with open('mycoupang.html', 'w', encoding='utf8') as op:  # 결과값을 파일로 생성
    op.write(res.text)





