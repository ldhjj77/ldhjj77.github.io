from numpy.lib.function_base import append
from bs4 import BeautifulSoup
import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine
from selenium import webdriver
import time
import re
import glob


def 코로나전세계_네이버():
    국가 = []
    누적확진자 = []
    신규확진자 = []
    사망자 = []
    사망율 = []
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98%ED%98%84%ED%99%A9')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="_cs_production_type"]/div/div[2]/div/div/ul/li[3]/a/span').click()
    for i in range(0, 27):   # 27까지
        driver.find_element_by_xpath('//*[@id="_cs_production_type"]/div/div[5]/div/div[3]/div[4]/div/div/a[2]').click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 신규확진자
        for i in range(1, 9):
            국가1 = soup.select('#_cs_production_type > div > div:nth-child(5) > div > div:nth-child(3) > div.csp_table_area.overseas_table > div > table > tbody > tr:nth-child(%d) > td.align_left > span' %(i))
            누적확진자1 = soup.select('#_cs_production_type > div > div:nth-child(5) > div > div:nth-child(3) > div.csp_table_area.overseas_table > div > table > tbody > tr:nth-child(%d) > td:nth-child(2) > span' %(i))
            신규확진자1 = soup.select('#_cs_production_type > div > div:nth-child(5) > div > div:nth-child(3) > div.csp_table_area.overseas_table > div > table > tbody > tr:nth-child(%d) > td:nth-child(3) > span' %(i))
            사망자1 = soup.select('#_cs_production_type > div > div:nth-child(5) > div > div:nth-child(3) > div.csp_table_area.overseas_table > div > table > tbody > tr:nth-child(%d) > td.align_center > span' %(i))
        
            for ii in 국가1:
                aa = str(ii)
                aa1 = re.search('">(.*)</', aa).group(1)    # 문자열 추출
                국가.append(aa1)


            for ii in 누적확진자1:
                aa = str(ii)
                aa1 = re.search('">(.*)</', aa).group(1)
                제거할문자 = ','        # 제거할문자목록
                aa1 = ''.join( x for x in aa1 if x not in 제거할문자)   # 불필요한 문자제거
                aa2 = int(aa1)      # 데이터 타입 변환
                누적확진자.append(aa2)


            for ii in 신규확진자1:
                aa = str(ii)
                aa1 = re.search('">(.*)</', aa).group(1)
                if aa1 == '-':
                    aa1 = 0     # 정수
                    aa1 = str(aa1)  # 정수가 나오면 밑에 join에서 에러가 나기때문에 문자로 변환
                제거할문자 = ','
                aa1 = ''.join( x for x in aa1 if x not in 제거할문자)
                aa2 = int(aa1)
                신규확진자.append(aa2)

            for ii in 사망자1:
                aa = str(ii)
                aa1 = re.search('">(.*)</', aa).group(1)    
                aa2 = re.search('(.*)<sp', aa1).group(1)
                aa3 = re.search('>(.*)<', aa1).group(1)
                제거할문자 = '(),%'
                aa2 = ''.join( x for x in aa2 if x not in 제거할문자)
                aa3 = ''.join( x for x in aa3 if x not in 제거할문자)
                aa4 = float(aa2)        # 사망율
                aa5 = int(aa3)          # 사망자
                사망율.append(aa4)
                사망자.append(aa5)


    국가 = pd.DataFrame(국가)
    누적확진자 = pd.DataFrame(누적확진자)
    신규확진자 = pd.DataFrame(신규확진자)
    사망자 = pd.DataFrame(사망자)
    사망율 = pd.DataFrame(사망율)

    좌표파일 = './source/xlsx/P009_세계코로나현황_네이버_좌표.xlsx'
    좌표 = pd.read_excel(좌표파일)
    좌표['위도'] = 좌표['위도'].round(3)
    좌표['경도'] = 좌표['경도'].round(3)

    날짜 = time.strftime('%Y-%m-%d', time.localtime(time.time()))   # 날짜
    날짜1 = ({'날짜' : [날짜] * 216})   
    날짜1 = pd.DataFrame(날짜1)     # 날짜 데이터프레임

    세계코로나현황 = pd.concat([국가, 누적확진자, 신규확진자, 사망자, 사망율, 날짜1], axis=1)
    세계코로나현황.columns = ['국가', '누적확진자', '신규확진자', '사망자', '사망율', '날짜']
    세계코로나현황.sort_values(by=['국가'], inplace=True)    # 이름순으로 정렬
    세계코로나현황.reset_index(drop=True, inplace=True)     # 인덱스 리셋
    세계코로나현황 = 세계코로나현황.drop(152).reset_index(drop=True) # 152행 일본크루즈 삭제
    세계코로나현황 = 세계코로나현황.drop(206).reset_index(drop=True) # 206번행 레위니옹 삭제
    세계코로나현황1 = pd.concat([세계코로나현황, 좌표], axis=1)
    세계코로나현황1.to_excel('./source/xlsx/P009/P009_날짜별_세계코로나현황_네이버_{0}.xlsx'.format(날짜))      # 일별 데이터

    세계코로나현황2 = pd.DataFrame()
    for f in glob.glob('./source/xlsx/P009/P009_날짜별*.xlsx'):  # 'P009_날짜별'로 시작하는 모든파일을 반복하며 추가
        df = pd.read_excel(f)
        세계코로나현황2 = 세계코로나현황2.append(df, ignore_index=True)  
        세계코로나현황2.drop('Unnamed: 0', axis=1, inplace=True)   
    
    세계코로나현황2.to_excel('./source/xlsx/P009_세계코로나현황_네이버.xlsx')       # 완성된 전체데이터

    # 데이터 프레임을 오라클 데이터베이스에 넣기
    # PROTOCOL=TCP / HOST = 서버주소 / PORT = 서버포트 / SERVICE_NAME = 데이터베이스이름
    dsn_tns = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))\
        (CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))"
    pwd = 'tiger'       # 사용자 비밀번호  / 아래 c##scott은 사용자명
    engine = create_engine('oracle+cx_oracle://c##scott:' + pwd + '@%s' % dsn_tns)
    세계코로나현황2.to_sql('P009_세계코로나현황_네이버', engine.connect(), if_exists='replace', index=False)

if __name__ == '__main__':
    코로나전세계_네이버()
    
