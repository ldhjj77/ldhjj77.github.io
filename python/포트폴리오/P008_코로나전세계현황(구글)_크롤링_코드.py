from numpy.lib.function_base import append
import requests
from bs4 import BeautifulSoup
import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine


def 코로나전세계_구글():
    url = 'https://www.google.com/search?q=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4+%ED%86%B5%EA%B3%84&sxsrf=ALeKk039rbc7RrUiD3uqu1MtY-ai2yNKSQ%3A1627884520659&source=hp&ei=6IsHYaHaJYbS-Qa11bjABg&iflsig=AINFCbYAAAAAYQeZ-I1ac-vheRVEnaDHYl1UC3E_0GKU&oq=%EC%BD%94%EB%A1%9C%EB%82%98+%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4+%ED%86%B5%EA%B3%84&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIGCAAQBRAeMgYIABAFEB4yBggAEAUQHjIGCAAQBRAeMgYIABAFEB4yBggAEAUQHjIGCAAQBRAeMgYIABAFEB46BwgjEOoCECdQ0glY0glgohJoAXAAeACAAXGIAXGSAQMwLjGYAQCgAQKgAQGwAQo&sclient=gws-wiz&ved=0ahUKEwih7ti01pHyAhUGad4KHbUqDmgQ4dUDCAc&uact=5'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # 전세계 합계 데이터 추출
    세계통계전체 = soup.find('div', attrs={'class':'o6Yscf iB3eO'})
    세계통계확진자 = 세계통계전체.find_all('td', attrs={'class':'dZdtsb Pmvw7b QmWbpe ZDeom'})
    세계통계확진자수0 = []
    전세계사망자수0 = []
    for i in 세계통계확진자:
        a = i.get_text()
        if a.startswith('확진자'):
            b = a.replace(',','')       # 숫자형으로 변환하기위해 ,제거
            세계통계확진자수0.append(b)
        elif a.startswith('사망자'):
            b = a.replace(',','')
            전세계사망자수0.append(b)
        # print(a)

    
    세계통계확진자수1 = "".join(세계통계확진자수0)   # 리스트를 문자열로 변환
    전세계확진자수 = 세계통계확진자수1[8:19]      # 필요한 부분추출
    전세계사망자수1 = "".join(전세계사망자수0)
    전세계사망자수 = 전세계사망자수1[7:16]
    # 전세계코로나 합산수치
    전세계코로나현황 = pd.DataFrame({'국가':'전체', '확진자' : 전세계확진자수, '사망자' : 전세계사망자수}, index=[0])

    
    국가명 = []
    확진자수 = []
    사망자수 = []
    전체 = soup.find_all('tr', attrs={'class':'viwUIc'})
    국가명 = []
    # print(전체)
    for index, i in enumerate(전체):
        if index == 0:
            pass
        elif 0 < index < 200:
            
            국가명1 = i.find('div', attrs={'class':'OrdL9b'})
            확진자1 = i.find('div', attrs={'class':'ruktOc'})
            for index, ii in enumerate(i):
                if index == 3 :
                    사망자1 = ii.find('div', attrs={'class':'ruktOc'})
                    사망자2 = 사망자1.find('span').get_text()
                    사망자3 = 사망자2.replace(',', '')  # 숫자형으로 변환하기위해 ,제거
                    사망자수.append(사망자3)
            국가명2 = 국가명1.find('span').get_text()
            확진자2 = 확진자1.find('span').get_text()
            확진자3 = 확진자2.replace(',', '')
            국가명.append(국가명2)
            확진자수.append(확진자3)

    국가명2 = pd.DataFrame(국가명)
    확진자수2 = pd.DataFrame(확진자수)
    사망자수2 = pd.DataFrame(사망자수)
    전세계코로나현황1 = pd.concat([국가명2,확진자수2, 사망자수2], axis=1)
    전세계코로나현황1.columns = ['국가', '확진자', '사망자']
    전세계코로나현황2 = pd.concat([전세계코로나현황, 전세계코로나현황1])    # 전세계 합계와 국가별 데이터 합치기
    전세계코로나현황2.sort_values(by=['국가'], inplace=True)    # 이름순으로 정렬
    전세계코로나현황3 = 전세계코로나현황2.reset_index(drop=True)    # 인덱스 리셋
    
    좌표파일 = './source/xlsx/P008_세계코로나현황_구글_좌표.xlsx'
    좌표 = pd.read_excel(좌표파일)
    세계코로나현황 = pd.concat([전세계코로나현황3, 좌표], axis=1)
    세계코로나현황['확진자'] = pd.to_numeric(세계코로나현황['확진자'], errors='ignore')
    세계코로나현황['사망자'] = pd.to_numeric(세계코로나현황['사망자'], errors='ignore')
    세계코로나현황['사망률'] = round(((세계코로나현황['사망자'] / 세계코로나현황['확진자']) * 100 ),3)  # 사망률 추가하기
    세계코로나현황['위도'] = 세계코로나현황['위도'].round(3)
    세계코로나현황['경도'] = 세계코로나현황['경도'].round(3)
    세계코로나현황.to_excel('./source/xlsx/P008_세계코로나현황_구글.xlsx')
    return 세계코로나현황

    
if __name__ == '__main__':
    코로나전세계_구글()

세계코로나현황 = 코로나전세계_구글()

# 데이터 프레임을 오라클 데이터베이스에 넣기
# PROTOCOL=TCP / HOST = 서버주소 / PORT = 서버포트 / SERVICE_NAME = 데이터베이스이름
dsn_tns = "(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))\
       (CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))"
pwd = 'tiger'       # 사용자 비밀번호  / 아래 c##scott은 사용자명
engine = create_engine('oracle+cx_oracle://c##scott:' + pwd + '@%s' % dsn_tns)
세계코로나현황.to_sql('P008_세계코로나현황_구글', engine.connect(), if_exists='replace', index=False)



