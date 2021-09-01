from pandas.core.frame import DataFrame
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 타입이 bs4.element.ResultSet 이면 get_text가 사용불가
# bs4.element.Tag 일경우엔 사용가능
# to2 = today.select('li:nth-of-type(1)')   # 속성의 순서대로 검색


def 전국날씨():
    url = 'https://search.naver.com/search.naver?sm=tab_sug.top&where=nexearch&query=%EC%A0%84%EA%B5%AD%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hniG7lp0J14ssiOjmSCssssss7G-015724&acq=%EC%A0%84%EA%B5%AD%EB%82%A0%EC%94%A8&acr=10&qdt=0'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    # 날씨상태
    서울 = soup.find('a', attrs={'class':'w_box ct001013'}).get_text()
    춘천 = soup.find('a', attrs={'class':'w_box ct003007'}).get_text()
    강릉 = soup.find('a', attrs={'class':'w_box ct003007'}).get_text()
    대전 = soup.find('a', attrs={'class':'w_box ct004001'}).get_text()
    청주 = soup.find('a', attrs={'class':'w_box ct006005'}).get_text()
    대구 = soup.find('a', attrs={'class':'w_box ct007007'}).get_text()
    광주 = soup.find('a', attrs={'class':'w_box ct011005'}).get_text()
    전주 = soup.find('a', attrs={'class':'w_box ct010011'}).get_text()
    부산 = soup.find('a', attrs={'class':'w_box ct008008'}).get_text()
    백령도 = soup.find('a', attrs={'class':'w_box ct002001'}).get_text()
    울릉도 = soup.find('a', attrs={'class':'w_box ct009002'}).get_text()
    제주도 = soup.find('a', attrs={'class':'w_box ct012005'}).get_text()

    # 지역 = pd.DataFrame(['서울'] + ['춘천'] + ['강릉'] + ['대전'] + ['청주'] + ['대구'] + ['광주'] + ['전주'] + ['부산'] + ['백령도'] + ['울릉도'] + ['제주도'])
    날씨 = [서울, 춘천, 강릉, 대전, 청주, 대구, 광주, 전주, 부산, 백령도, 울릉도, 제주도]
    날씨1 = pd.DataFrame()

    for i in 날씨:
        a = i[:-3]   # 날씨상태
        b = i[-3] + i[-2]   # 현재기온
        c = pd.DataFrame([[a]+ [b]])
        날씨1 = 날씨1.append(c)
    위도 = DataFrame()
    경도 = DataFrame()

    날씨1['지역'] = pd.Series(['서울','춘천','강릉','대전','청주','대구','광주','전주','부산','백령','울릉','제주'], index=날씨1.index)
    날씨1['위도'] = pd.Series(['37.55277148225529','37.884604551086255', '37.7188738133609', '36.298443669486655', '36.7535834068629', '36.47429186120351', '35.0852405939778', '35.6823644990858', '35.43589255808068', '37.95109593665316', '37.52884596038456', '33.37508939020389'], index=날씨1.index)
    날씨1['경도'] = pd.Series(['126.80515370195922', '127.74316185221805', '128.80744728995975', '126.89837578409714', '128.105309906976', '129.0721448593317', '126.797385195114', '127.72762483852838', '128.81521579680458', '124.6729994007028', '130.87662844275005', '126.55323507614226'], index=날씨1.index)
    날씨1.columns = ['기상상황', '현재기온', '지역', '위도', '경도']
    날씨1.to_excel('./source/xlsx/004_네이버날씨_전국.xlsx', sheet_name='전국')



if __name__ == '__main__':
    전국날씨()           


