from numpy.lib.function_base import append
import requests
from bs4 import BeautifulSoup
import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine


def 코로나():
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B5%AD%EB%82%B4+%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90+%ED%98%84%ED%99%A9'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    전체 = soup.find('div', attrs={'class':'api_subject_bx'})
    확진환자 = soup.find('li', attrs={'class':'info_01'}).get_text()
    사망자 = soup.find('li', attrs={'class':'info_04'}).get_text()
    지역명추출 = soup.find_all('td', attrs={'class':'align_center'})
    지역 = []
    for i in 지역명추출:
        a = i.get_text().strip()
        지역.append(a)
        if a == '세종' :
            break
    지역 = pd.DataFrame(지역)
    
    누적확진자추출 = soup.find_all('td', attrs={'class':'align_right'})
    확진자 = []
    for i in 누적확진자추출:
        b = i.get_text().strip()
        c = b.replace(',','')   # , 로 인해 숫자로 변환이 안되기때문에 제거
        확진자.append(c)
        
    누적확진자 = pd.DataFrame(확진자[0:35:2])
    전일확진자 = pd.DataFrame(확진자[1:37:2])
    코로나현황 = pd.concat([지역, 누적확진자 , 전일확진자], axis=1)
    코로나현황.columns = ['지역', '누적확진자', '전일확진자']
    코로나현황.drop(코로나현황.index[7], inplace=True)  # 불필요한 '검역'행 삭제
    코로나현황2 = pd.DataFrame(코로나현황)
    코로나현황2 = 코로나현황2.reset_index(drop=True)    # 인덱스 재설정
    
    return 코로나현황2
    


def 위도_경도():
    
    좌표리스트 = {'위도' : ['37.5666']+ ['37.4376'] + ['35.8722'] +
             ['37.4563'] + ['35.1794'] + ['35.4677'] + 
             ['36.3346'] + ['36.6990'] + ['37.8710'] +
             ['36.3511'] + ['37.0243'] + ['35.1597'] + 
             ['35.5388'] + ['35.7459'] + ['34.8824'] + 
             ['33.5000'] + [' 36.4875'], 
             '경도' : ['127.0780'] + ['127.5172'] + ['128.6025'] + 
             ['126.7052'] + ['129.0755'] + ['128.2147'] + 
             ['128.8789'] + ['126.8004'] + ['128.1657'] + 
             ['127.6850'] + ['127.7010'] + ['126.8530'] + 
             ['129.3166'] + ['127.1530'] + ['126.9929'] + 
             ['126.5166'] + ['127.2816']}
    # 합계용 좌표 36.3750 / 128.0230
    좌표 = pd.DataFrame(좌표리스트)
    return(좌표)


코로나현황 = 코로나()
코로나현황 = 코로나현황.apply(pd.to_numeric, errors = 'ignore')

# 합계 추가
# 코로나현황합계 = [{'지역' : '합계' , '누적확진자' : 코로나현황['누적확진자'].sum() ,
#             '전일확진자' : 코로나현황['전일확진자'].sum()}]
# 코로나현황합계 = pd.DataFrame(코로나현황합계)
# 코로나현황1 = 코로나현황.append(코로나현황합계)
# 코로나현황2 = 코로나현황1.reset_index(drop=True, inplace=False) # 인덱스 재설정
좌표 = 위도_경도()
전국코로나현황 = pd.concat([코로나현황, 좌표 ], axis=1)
전국코로나현황.to_excel('./source/xlsx/P007_전국코로나현황.xlsx')  


    
if __name__ == '__main__':
    코로나()
    위도_경도() 


# 데이터 프레임을 오라클 데이터베이스에 넣기
# PROTOCOL=TCP / HOST = 서버주소 / PORT = 서버포트 / SERVICE_NAME = 데이터베이스이름
dsn_tns = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))\
       (CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))"
pwd = 'tiger'       # 사용자 비밀번호  / 아래 c##scott은 사용자명
engine = create_engine('oracle+cx_oracle://c##scott:' + pwd + '@%s' % dsn_tns)
전국코로나현황.to_sql('P007_전국코로나현황', engine.connect(), if_exists='replace', index=False)





