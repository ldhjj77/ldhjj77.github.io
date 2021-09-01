import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import glob
import os


# 타입이 bs4.element.ResultSet 이면 get_text가 사용불가
# bs4.element.Tag 일경우엔 사용가능
# to2 = today.select('li:nth-of-type(1)')   # 속성의 순서대로 검색


def 대구_중구():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EC%A4%91%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%82%A8%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnhJ%2BdprvN8ssvrmBmZssssssQw-143351'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()    # 맑음 흐림
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    min = "최저온도 : " + min_temp
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도
    max = "최고온도 : " + max_temp

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    morning = "오전 " + morning_rain_rate
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거
    afternoon = "오후 " + afternoon_rain_rate

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    pmp = "미세먼지 : " + pm
        
    # 오늘날씨
    today = pd.DataFrame([cast + min + max + morning + afternoon + pmp])
    today.columns = ['예보']
    today.loc[:, "지역"] = pd.Series([area], index=today.index)
    today.index = [area]

    # 주간 날씨
    tomorrow = soup.find('ul', attrs={'class':'list_area _pageList'})   # 전체데이터
    t1 = tomorrow.find_all('li')    # 리스트 데이터
    weekly = pd.DataFrame()

    for i in t1:
        day = i.find('span', attrs={'class': 'day_info'}).get_text()    # 날짜 정보
        num = i.find_all('span', attrs={'class': 'num'})    # 강수확률 수치 전체
        num1 = num[0].get_text()    # 강수확률 첫번째 자료 불러오기
        num2 = num[1].get_text()    # 강수확률 두번째 자료 불러오기
        dayp = day      # 날자
        nummin = num1       # 오전 강수확률
        nummax = num2       # 오휴 강수확률
        point = i.find('dd').get_text()     # 전체 기온
        pointp = point.replace("°" ,"")     # ° 삭제
        pointp = pointp.split("/")      # / 기준으로 문자열 분리
        point1 = pointp[0]      # 최저기온
        point2 = pointp[1]      # 최고기온
        wtarray = pd.DataFrame([[area] + [dayp] + [nummin] + [nummax] + [point1] + [point2] + ['35.865676774945136'] + ['128.59339991922084']])
        weekly = weekly.append(wtarray)

    weekly.columns = ['지역','날짜', '오전 강수확률', '오후 강수확률', '최저기온', '최고기온', '위도', '경도']
    # weekly.index = [area +" 당일",area +" 1일후",area +" 2일후",area +" 3일후",area +" 4일후" ]

    with pd.ExcelWriter('w1.xlsx') as writer:  # 엑셀파일 생성
        weekly.to_excel(writer, sheet_name=area+'weekly')
        today.to_excel(writer, sheet_name=area+'today')


def 대구_남구():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%82%A8%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%82%A8%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnhJHwprvmZss76xMXdssssstMC-076095'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()    # 맑음 흐림
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    min = "최저온도 : " + min_temp
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도
    max = "최고온도 : " + max_temp

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    morning = "오전 " + morning_rain_rate
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거
    afternoon = "오후 " + afternoon_rain_rate

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    pmp = "미세먼지 : " + pm
    
        # 오늘날씨
    today = pd.DataFrame([cast + min + max + morning + afternoon + pmp])
    today.columns = ['예보']
    today.loc[:, "지역"] = pd.Series([area], index=today.index)
    today.index = [area]

    # 주간 날씨
    tomorrow = soup.find('ul', attrs={'class':'list_area _pageList'})   # 전체데이터
    t1 = tomorrow.find_all('li')    # 리스트 데이터
    weekly = pd.DataFrame()

    for i in t1:
        day = i.find('span', attrs={'class': 'day_info'}).get_text()    # 날짜 정보
        num = i.find_all('span', attrs={'class': 'num'})    # 강수확률 수치 전체
        num1 = num[0].get_text()    # 강수확률 첫번째 자료 불러오기
        num2 = num[1].get_text()    # 강수확률 두번째 자료 불러오기
        dayp = day      # 날자
        nummin = num1       # 오전 강수확률
        nummax = num2       # 오휴 강수확률
        point = i.find('dd').get_text()     # 전체 기온
        pointp = point.replace("°" ,"")     # ° 삭제
        pointp = pointp.split("/")      # / 기준으로 문자열 분리
        point1 = pointp[0]      # 최저기온
        point2 = pointp[1]      # 최고기온
        wtarray = pd.DataFrame([[area] + [dayp] + [nummin] + [nummax] + [point1] + [point2] + ['35.835786350731176'] + ['128.58601516279393']])
        weekly = weekly.append(wtarray)

    weekly.columns = ['지역','날짜', '오전 강수확률', '오후 강수확률', '최저기온', '최고기온', '위도', '경도']
    # weekly.index = [area +" 당일",area +" 1일후",area +" 2일후",area +" 3일후",area +" 4일후" ]

    with pd.ExcelWriter('w2.xlsx') as writer:  # 엑셀파일 생성
        weekly.to_excel(writer, sheet_name='weekly')
        today.to_excel(writer, sheet_name='today')


def 대구_수성구():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EC%88%98%EC%84%B1%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EC%A4%91%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnh8ulprvxsssn0AvC0ssssst2d-020805'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()    # 맑음 흐림
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    min = "최저온도 : " + min_temp
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도
    max = "최고온도 : " + max_temp

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    morning = "오전 " + morning_rain_rate
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거
    afternoon = "오후 " + afternoon_rain_rate

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    pmp = "미세먼지 : " + pm
    
        # 오늘날씨
    today = pd.DataFrame([cast + min + max + morning + afternoon + pmp])
    today.columns = ['예보']
    today.loc[:, "지역"] = pd.Series([area], index=today.index)
    today.index = [area]

    # 주간 날씨
    tomorrow = soup.find('ul', attrs={'class':'list_area _pageList'})   # 전체데이터
    t1 = tomorrow.find_all('li')    # 리스트 데이터
    weekly = pd.DataFrame()

    for i in t1:
        day = i.find('span', attrs={'class': 'day_info'}).get_text()    # 날짜 정보
        num = i.find_all('span', attrs={'class': 'num'})    # 강수확률 수치 전체
        num1 = num[0].get_text()    # 강수확률 첫번째 자료 불러오기
        num2 = num[1].get_text()    # 강수확률 두번째 자료 불러오기
        dayp = day      # 날자
        nummin = num1       # 오전 강수확률
        nummax = num2       # 오휴 강수확률
        point = i.find('dd').get_text()     # 전체 기온
        pointp = point.replace("°" ,"")     # ° 삭제
        pointp = pointp.split("/")      # / 기준으로 문자열 분리
        point1 = pointp[0]      # 최저기온
        point2 = pointp[1]      # 최고기온
        wtarray = pd.DataFrame([[area] + [dayp] + [nummin] + [nummax] + [point1] + [point2] + ['35.83534521914002'] + ['128.66325476750768']])
        weekly = weekly.append(wtarray)

    weekly.columns = ['지역','날짜', '오전 강수확률', '오후 강수확률', '최저기온', '최고기온', '위도', '경도']
    # weekly.index = [area +" 당일",area +" 1일후",area +" 2일후",area +" 3일후",area +" 4일후" ]

    with pd.ExcelWriter('w3.xlsx') as writer:  # 엑셀파일 생성
        weekly.to_excel(writer, sheet_name='weekly')
        today.to_excel(writer, sheet_name='today')


def 대구_동구():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%8F%99%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EC%88%98%EC%84%B1%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hniPmsp0Jy0sstlROU0ssssstkK-093405'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()    # 맑음 흐림
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    min = "최저온도 : " + min_temp
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도
    max = "최고온도 : " + max_temp

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    morning = "오전 " + morning_rain_rate
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거
    afternoon = "오후 " + afternoon_rain_rate

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    pmp = "미세먼지 : " + pm
    
        # 오늘날씨
    today = pd.DataFrame([cast + min + max + morning + afternoon + pmp])
    today.columns = ['예보']
    today.loc[:, "지역"] = pd.Series([area], index=today.index)
    today.index = [area]

    # 주간 날씨
    tomorrow = soup.find('ul', attrs={'class':'list_area _pageList'})   # 전체데이터
    t1 = tomorrow.find_all('li')    # 리스트 데이터
    weekly = pd.DataFrame()

    for i in t1:
        day = i.find('span', attrs={'class': 'day_info'}).get_text()    # 날짜 정보
        num = i.find_all('span', attrs={'class': 'num'})    # 강수확률 수치 전체
        num1 = num[0].get_text()    # 강수확률 첫번째 자료 불러오기
        num2 = num[1].get_text()    # 강수확률 두번째 자료 불러오기
        dayp = day      # 날자
        nummin = num1       # 오전 강수확률
        nummax = num2       # 오휴 강수확률
        point = i.find('dd').get_text()     # 전체 기온
        pointp = point.replace("°" ,"")     # ° 삭제
        pointp = pointp.split("/")      # / 기준으로 문자열 분리
        point1 = pointp[0]      # 최저기온
        point2 = pointp[1]      # 최고기온
        wtarray = pd.DataFrame([[area] + [dayp] + [nummin] + [nummax] + [point1] + [point2] + ['35.885556427869986'] + ['128.6318876186057']])
        weekly = weekly.append(wtarray)

    weekly.columns = ['지역','날짜', '오전 강수확률', '오후 강수확률', '최저기온', '최고기온', '위도', '경도']
    # weekly.index = [area +" 당일",area +" 1일후",area +" 2일후",area +" 3일후",area +" 4일후" ]

    with pd.ExcelWriter('w4.xlsx') as writer:  # 엑셀파일 생성
        weekly.to_excel(writer, sheet_name='weekly')
        today.to_excel(writer, sheet_name='today')


def 대구_북구():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%B6%81%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%8F%99%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hniPEsp0JXossOIhBnVssssssQo-391917'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()    # 맑음 흐림
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    min = "최저온도 : " + min_temp
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도
    max = "최고온도 : " + max_temp

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    morning = "오전 " + morning_rain_rate
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거
    afternoon = "오후 " + afternoon_rain_rate

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    pmp = "미세먼지 : " + pm
    
        # 오늘날씨
    today = pd.DataFrame([cast + min + max + morning + afternoon + pmp])
    today.columns = ['예보']
    today.loc[:, "지역"] = pd.Series([area], index=today.index)
    today.index = [area]

    # 주간 날씨
    tomorrow = soup.find('ul', attrs={'class':'list_area _pageList'})   # 전체데이터
    t1 = tomorrow.find_all('li')    # 리스트 데이터
    weekly = pd.DataFrame()

    for i in t1:
        day = i.find('span', attrs={'class': 'day_info'}).get_text()    # 날짜 정보
        num = i.find_all('span', attrs={'class': 'num'})    # 강수확률 수치 전체
        num1 = num[0].get_text()    # 강수확률 첫번째 자료 불러오기
        num2 = num[1].get_text()    # 강수확률 두번째 자료 불러오기
        dayp = day      # 날자
        nummin = num1       # 오전 강수확률
        nummax = num2       # 오휴 강수확률
        point = i.find('dd').get_text()     # 전체 기온
        pointp = point.replace("°" ,"")     # ° 삭제
        pointp = pointp.split("/")      # / 기준으로 문자열 분리
        point1 = pointp[0]      # 최저기온
        point2 = pointp[1]      # 최고기온
        wtarray = pd.DataFrame([[area] + [dayp] + [nummin] + [nummax] + [point1] + [point2] + ['35.92827446221116'] + ['128.5775049653885']])
        weekly = weekly.append(wtarray)

    weekly.columns = ['지역','날짜', '오전 강수확률', '오후 강수확률', '최저기온', '최고기온', '위도', '경도']
    # weekly.index = [area +" 당일",area +" 1일후",area +" 2일후",area +" 3일후",area +" 4일후" ]

    with pd.ExcelWriter('w5.xlsx') as writer:  # 엑셀파일 생성
        weekly.to_excel(writer, sheet_name='weekly')
        today.to_excel(writer, sheet_name='today')
        
        
def 대구_서구():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EC%84%9C%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%B6%81%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnilldprvxZsseozVpsssssssXG-244070'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()    # 맑음 흐림
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    min = "최저온도 : " + min_temp
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도
    max = "최고온도 : " + max_temp

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    morning = "오전 " + morning_rain_rate
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거
    afternoon = "오후 " + afternoon_rain_rate

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    pmp = "미세먼지 : " + pm
    
        # 오늘날씨
    today = pd.DataFrame([cast + min + max + morning + afternoon + pmp])
    today.columns = ['예보']
    today.loc[:, "지역"] = pd.Series([area], index=today.index)
    today.index = [area]

    # 주간 날씨
    tomorrow = soup.find('ul', attrs={'class':'list_area _pageList'})   # 전체데이터
    t1 = tomorrow.find_all('li')    # 리스트 데이터
    weekly = pd.DataFrame()

    for i in t1:
        day = i.find('span', attrs={'class': 'day_info'}).get_text()    # 날짜 정보
        num = i.find_all('span', attrs={'class': 'num'})    # 강수확률 수치 전체
        num1 = num[0].get_text()    # 강수확률 첫번째 자료 불러오기
        num2 = num[1].get_text()    # 강수확률 두번째 자료 불러오기
        dayp = day      # 날자
        nummin = num1       # 오전 강수확률
        nummax = num2       # 오휴 강수확률
        point = i.find('dd').get_text()     # 전체 기온
        pointp = point.replace("°" ,"")     # ° 삭제
        pointp = pointp.split("/")      # / 기준으로 문자열 분리
        point1 = pointp[0]      # 최저기온
        point2 = pointp[1]      # 최고기온
        wtarray = pd.DataFrame([[area] + [dayp] + [nummin] + [nummax] + [point1] + [point2] + ['35.87505470483516'] + ['128.54975242049758']])
        weekly = weekly.append(wtarray)
    
    weekly.columns = ['지역','날짜', '오전 강수확률', '오후 강수확률', '최저기온', '최고기온', '위도', '경도']
    # weekly.index = [area +" 당일",area +" 1일후",area +" 2일후",area +" 3일후",area +" 4일후" ]

    with pd.ExcelWriter('w6.xlsx') as writer:  # 엑셀파일 생성
        weekly.to_excel(writer, sheet_name='weekly')
        today.to_excel(writer, sheet_name='today')


def 대구_달서구():
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%8B%AC%EC%84%9C%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%B6%81%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hniPWsp0JXVssmVHitlssssst5K-512391'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()    # 맑음 흐림
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    min = "최저온도 : " + min_temp
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도
    max = "최고온도 : " + max_temp

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    morning = "오전 " + morning_rain_rate
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거
    afternoon = "오후 " + afternoon_rain_rate

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    pmp = "미세먼지 : " + pm
    
        # 오늘날씨
    today = pd.DataFrame([cast + min + max + morning + afternoon + pmp])
    today.columns = ['예보']
    today.loc[:, "지역"] = pd.Series([area], index=today.index)
    today.index = [area]

    # 주간 날씨
    tomorrow = soup.find('ul', attrs={'class':'list_area _pageList'})   # 전체데이터
    t1 = tomorrow.find_all('li')    # 리스트 데이터
    weekly = pd.DataFrame()

    for i in t1:
        day = i.find('span', attrs={'class': 'day_info'}).get_text()    # 날짜 정보
        num = i.find_all('span', attrs={'class': 'num'})    # 강수확률 수치 전체
        num1 = num[0].get_text()    # 강수확률 첫번째 자료 불러오기
        num2 = num[1].get_text()    # 강수확률 두번째 자료 불러오기
        dayp = day      # 날자
        nummin = num1       # 오전 강수확률
        nummax = num2       # 오휴 강수확률
        point = i.find('dd').get_text()     # 전체 기온
        pointp = point.replace("°" ,"")     # ° 삭제
        pointp = pointp.split("/")      # / 기준으로 문자열 분리
        point1 = pointp[0]      # 최저기온
        point2 = pointp[1]      # 최고기온
        wtarray = pd.DataFrame([[area] + [dayp] + [nummin] + [nummax] + [point1] + [point2] + ['35.82758789651996'] + ['128.52908959379286']])
        weekly = weekly.append(wtarray)

    weekly.columns = ['지역','날짜', '오전 강수확률', '오후 강수확률', '최저기온', '최고기온', '위도', '경도']
    # weekly.index = [area +" 당일",area +" 1일후",area +" 2일후",area +" 3일후",area +" 4일후" ]

    with pd.ExcelWriter('w7.xlsx') as writer:  # 엑셀파일 생성
        weekly.to_excel(writer, sheet_name='weekly')
        today.to_excel(writer, sheet_name='today')




if __name__ == '__main__':
    대구_중구()           
    대구_남구()
    대구_수성구()
    대구_동구()
    대구_북구()
    대구_서구()
    대구_달서구()




all_data = pd.DataFrame()  
for f in glob.glob('w*.xlsx'):  # w로 시작하는 모든파일을 반복하며 추가
    df = pd.read_excel(f)       # 내용을 df에 넣기
    all_data = all_data.append(df, ignore_index=True)   # df의 내용을 all_data에 추가
    all_data.drop('Unnamed: 0', axis=1, inplace=True)   # Unnamed: 0 삭제

    all_data.to_excel('./source/xlsx/003_네이버날씨_대구.xlsx')


os.remove('w1.xlsx')
os.remove('w2.xlsx')
os.remove('w3.xlsx')
os.remove('w4.xlsx')
os.remove('w5.xlsx')
os.remove('w6.xlsx')
os.remove('w7.xlsx')