import requests
from bs4 import BeautifulSoup
import pandas as pd
import glob
import os

# 타입이 bs4.element.ResultSet 이면 get_text가 사용불가
# bs4.element.Tag 일경우엔 사용가능
# to2 = today.select('li:nth-of-type(1)')   # 속성의 순서대로 검색
# 딕셔너리로 데이터프레임 만들면 같은내용 복사가 가능함(좌표)


def 대구날씨():
    urllist = ['https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EC%A4%91%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%82%A8%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnhJ%2BdprvN8ssvrmBmZssssssQw-143351',
               'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%82%A8%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%82%A8%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnhJHwprvmZss76xMXdssssstMC-076095',
               'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EC%88%98%EC%84%B1%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EC%A4%91%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnh8ulprvxsssn0AvC0ssssst2d-020805',
               'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%8F%99%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EC%88%98%EC%84%B1%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hniPmsp0Jy0sstlROU0ssssstkK-093405',
               'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%B6%81%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%8F%99%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hniPEsp0JXossOIhBnVssssssQo-391917',
               'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EC%84%9C%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%B6%81%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hnilldprvxZsseozVpsssssssXG-244070',
               'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%8B%AC%EC%84%9C%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%8C%80%EA%B5%AC%EB%B6%81%EA%B5%AC%EB%82%A0%EC%94%A8&tqi=hniPWsp0JXVssmVHitlssssst5K-512391'
               ]

    for u in urllist:
        url = u
        headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        area = soup.find('span', attrs={'class':'btn_select'}).get_text()   # 지역명

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
            wtarray = pd.DataFrame({'지역' : [area], '날짜' :  [dayp], '오전 강수확률' : [nummin],
                                    '오후 강수확률' : [nummax], '최저기온' : [point1], '최고기온' : [point2]})
            weekly = weekly.append(wtarray)
            weekly.to_excel('{0}.xlsx'.format(area))   # weekly 시트 내용
        
    # 파일 합치기
    all_data = pd.DataFrame()  
    for f in glob.glob('*.xlsx'):  # w로 시작하는 모든파일을 반복하며 추가
        df = pd.read_excel(f)       # f파일의 내용을 df에 넣기
        all_data = all_data.append(df, ignore_index=True)   # df의 내용을 all_data에 추가
        all_data.drop('Unnamed: 0', axis=1, inplace=True)   # Unnamed: 0 삭제

    좌표 = pd.DataFrame({'위도' : ['35.8357'] * 5 + ['35.8275'] * 5 + ['35.8855'] * 5 +
                      ['35.9282'] * 5 + ['35.8750'] * 5 + ['35.8353'] * 5 + ['35.8656'] * 5,                   
              '경도' : ['128.5860'] * 5 + ['128.5290'] * 5 + ['128.6318'] * 5 + 
                        ['128.5775'] * 5 + ['128.5497'] * 5 + ['128.6632'] * 5 + ['128.5933'] * 5}) 

    all_data['위도'] = 좌표['위도']     # 위도 추가
    all_data['경도'] = 좌표['경도']     # 경도 추가
    all_data.to_excel('./source/xlsx/005_네이버날씨_대구.xlsx')   # 대구날씨 파일

    # 필요없어진 파일 삭제 리스트
    remove = ['대구광역시 남구 이천동', '대구광역시 달서구 성당동',
          '대구광역시 동구 신암동', '대구광역시 북구 칠성동1가',
          '대구광역시 서구 내당동', '대구광역시 수성구 범어동',
          '대구광역시 중구 동인동1가']

    for i in remove:
        os.remove('{0}.xlsx'.format(i))
    
                

if __name__ == '__main__':
    대구날씨()           

