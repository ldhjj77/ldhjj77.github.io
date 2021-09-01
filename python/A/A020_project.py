# 프로젝트 : 웹 스크레핑을 통해 나만의 비서를 만들어 보자.

# [조 건]
# 1. 네이버에서 오늘 대구의 날씨를 가져온다.
# 2. 네이버에서 헤드라인 뉴스 3건을 가져온다.
# 3. IT 뉴스 3건을 가져온다.
# 4. 오늘의 영어 회화 지문을 가져온다.(해커스 어학원)

# [출력 예시]
# [ 오늘의 날씨]
# 맑음, 어제보다 00도 높아요
# 현재 00도 (최저 00도 / 최고 00도)
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지(  ) 좋음

# [헤드라인 뉴스]
# 1. 뉴스1제목
# ( 링크 : https://.... )
# 2. 뉴스2제목
# ( 링크 : https://.... )
# 3. 뉴스3제목
# ( 링크 : https://.... )

# [IT 뉴스]
# 1. 뉴스1제목
# ( 링크 : https://.... )
# 2. 뉴스2제목
# ( 링크 : https://.... )
# 3. 뉴스3제목
# ( 링크 : https://.... )

# [오늘의 영어 회화]
# (영어 지문)
# kim : How are you?
# lee : fine!
# (한글 지문)
# kim : 어때?
# lee : 좋아!

# 파이썬 기초 : w3school, python.org, 위키독스(점프투파이썬)


import requests
import re
from bs4 import BeautifulSoup


# 반복되는 부분을 함수로 생성
def create_soup(url, headers):         # 필요한 매개변수를 넣어줘야함
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

# 날씨 wed / 온도 tem / 강수확률 rain / 미세먼지 fdust / 초미세먼지 ufdust

def scrape_weather():
    print('[오늘의 날씨]')
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%8C%80%EA%B5%AC%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=h71ErlprvN8ss6l%2FnnCssssstk4-523554'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    # soup = create_soup(url, headers)
    
    # 맑음, 어제보다 0도 높아요
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()
    
    curr_temp = soup.find('p', attrs={'class':'info_temperature'}).get_text().replace('도씨', '')      # 현재온도
    # 가져온 텍스트중에 '도씨' 를 공백처리
    
    min_temp = soup.find('span', attrs={'class':'min'}).get_text()   # 최저온도
    max_temp = soup.find('span', attrs={'class':'max'}).get_text()   # 최고온도

    # 오전 오후 강수 확률
    morning_rain_rate = soup.find('span', attrs={'class': 'point_time morning'}).get_text().strip() # 오전 강수확률 / 공백제거
    afternoon_rain_rate = soup.find('span', attrs={'class': 'point_time afternoon'}).get_text().strip() # 오후 강수확률 / 공백제거

    # 미세 먼지
    dust = soup.find('dl', attrs={'class':'indicator'})
    pm = dust.find('dd', attrs={'class':'lv1'}).get_text()
    
    

    # print(dust)
    print(cast)
    print('현재 {0} (최저 {1} / 최고 {2})'.format(curr_temp, min_temp, max_temp))
    print('오전 {0} / 오후 {1}'.format(morning_rain_rate, afternoon_rain_rate))
    print()
    print('미세먼지 {0}'.format(pm))
    print()
    print()




# 헤드라인 뉴스
def scrape_headline_news():
    print('[헤드라인 뉴스]')
    url = 'https://news.naver.com'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    # res = requests.get(url, headers=headers)
    # res.raise_for_status()
    # soup = BeautifulSoup(res.text, 'lxml')
    soup = create_soup(url, headers)

    news_list = soup.find('ul', attrs={'class': 'hdline_article_list'}).find_all('li', limit=3)
    # ul 테그의 hdline_article_list 클레스에서 가져온 것들중에 li테그에 속한것을 3개만 가져옴
    for index, news in enumerate(news_list):        # 인덱스값 매기기 index는 번호를 매겨줌
        title = news.find('a').get_text().strip()
        link = news.find('a')['href']
        print('{0}. {1}'.format(index + 1, title))
        print('   (  링크 : {0}  )'.format(url + link))
    print()
        
    
# IT뉴스
def scrape_it_news():
    print('[IT 뉴스]')
    url = 'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    news_list = soup.find('ul', attrs={'class': 'type06_headline'}).find_all('li', limit=3)
    for index, news in enumerate(news_list):
        a_idx = 0       # 임의의 변수 설정
        img = news.find('img')  # img 라는 테그를 찾아서 img변수에 넣음
        if img:     # img 테그가 나온다면
            a_idx = 1   # a 태그가 있으면 1번인 a 태그의 정보를 가져옴( 두번째 a 태그를 가져옴)
        title = news.find_all('a')[a_idx].get_text().strip()    # 인덱스 값이 여러개이기 때문에 all로 검색해야함
        link = news.find_all('a')[a_idx]['href']
        print('{0}. {1}'.format(index + 1, title))
        print('   (  링크 : {0}  )'.format(link))
    print()
    


def scrape_english():
    print('[오늘의 영어회화]')
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')   
    print('[영어 지문]')
    sentences = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})
    # conv_kor_t2, conv_kor_t3 이런식으로 아이디의 이름이 다를경우
    # 정규 표현식인 re를 사용해 테그를 검색해서 자료 검출
    for sentence in sentences[len(sentences)//2:]:   # len(sentences)//2: = 4 ~ 끝까지(7)이 됨 //는 앞에 정수만 가져오는거
        print(sentence.get_text().strip())    
    print()
    print("[한글 지문]")
    for sentence in sentences[:len(sentences)//2]:   # :len(sentences)//2 = 처음부터 3까지
        print(sentence.get_text().strip())    
    print()
    




if __name__ == '__main__':  # scrape_weather()라는 함수가 같은파일(A020_project.py)안에 있다면 실행하게
    scrape_weather()        # 오늘 날씨 정보 가져오기
    # scrape_headline_news()  # 헤드라인 뉴스
    # scrape_it_news()          # 아이티 뉴스
    # scrape_english()          # 영어 회화




# 추가 내용

#  다음 뉴스에서 3개 뉴스의 제목과 링크 가져오기
# 1. 제목...
#    링크...

def scrape_daum_news():
    print('[다음 헤드라인 뉴스]')
    url = 'https://news.daum.net'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    news_list = soup.find('ul', attrs={'class': 'list_headline'}).find_all('li', limit=3)
    # ul 테그의 hdline_article_list 클레스에서 가져온 것들중에 li테그에 속한것을 3개만 가져옴
    for index, news in enumerate(news_list):        # 인덱스값 매기기 index는 번호를 매겨줌
        title = news.find('a').get_text().strip()
        link = news.find('a')['href']
        print('{0}. {1}'.format(index + 1, title))
        print('   (  링크 : {0}  )'.format(link))
    print()



# # 다음 경제 뉴스에서 2개 뉴스의 제목과 링크 가져오기
# 1. 제목...
#    링크...
def scrape_daum_economic_news():
    print('[다음 경제 뉴스]')
    url = 'https://news.daum.net/economic#1'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    news_list = soup.find('ul', attrs={'class': 'list_mainnews'}).find_all('li', limit=2)
    # ul 테그의 hdline_article_list 클레스에서 가져온 것들중에 li테그에 속한것을 3개만 가져옴
    for index, news in enumerate(news_list):
        a_idx = 0       # 임의의 변수 설정
        img = news.find('img')  # img 라는 테그를 찾아서 img변수에 넣음
        if img:     # img 테그가 나온다면
            a_idx = 1   # a 태그가 있으면 1번인 a 태그의 정보를 가져옴( 두번째 a 태그를 가져옴)
        title = news.find_all('a')[a_idx].get_text().strip()    # 인덱스 값이 여러개이기 때문에 all로 검색해야함
        link = news.find_all('a')[a_idx]['href']
        print('{0}. {1}'.format(index + 1, title))
        print('   (  링크 : {0}  )'.format(link))
    print()
    print()



# # 다음 게임에서 추천 게임 4개의 제목과 이미지 가져오기
# 1. 제목...
#    이미지
def scrape_daum_game():
    print('[다음 게임]')
    url = 'http://game.daum.net'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    game_list_pc = soup.find('div', attrs={'class': 'area_pc'}).find_all('li', limit=3)
    # ul 테그의 hdline_article_list 클레스에서 가져온 것들중에 li테그에 속한것을 3개만 가져옴
    for index, pc_game in enumerate(game_list_pc):        # 인덱스값 매기기 index는 번호를 매겨줌
        title = pc_game.find('a').get_text().strip()
        image_url = pc_game.find('img')['src']
        print('{0}. {1}'.format(index + 1, title))
        print('   (  이미지 : {0}  )'.format(image_url))
        print()
        print()
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open('./A/A020_pcgame{0}.jpg'.format(index+1), 'wb') as f: # 피씨게임 이미지 파일생성
            f.write(image_res.content)
        
    game_list_m = soup.find('div', attrs={'class': 'area_m'}).find_all('li', limit=1)
    # ul 테그의 hdline_article_list 클레스에서 가져온 것들중에 li테그에 속한것을 3개만 가져옴
    for index, m_game in enumerate(game_list_m):        # 인덱스값 매기기 index는 번호를 매겨줌
        title = m_game.find('a').get_text().strip()
        image_url = m_game.find('img')['src']
        print('{0}. {1}'.format(index + 1, title))
        print('   (  이미지 : {0}  )'.format(image_url))
        print()
        print()
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        with open('./A/A020_mgame{0}.jpg'.format(index+1), 'wb') as f: # 모바일 게임 이미지 파일생성
            f.write(image_res.content)

       




# 해커스에서 오늘의 한 줄 명언 가져오기
# (영어명언)
# (한글명언)
def scrape_wisesay():       
    print('[오늘의 명언]')
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/B_others_wisesay&keywd=haceng_submain_lnb_eng_B_others_wisesay&logger_kw=haceng_submain_lnb_eng_B_others_wisesay'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    print('[영어 명언]')
    sentence_eng = soup.find('div', attrs={'class':'text_en'}).get_text()
    print(sentence_eng)
    print("[한글 명언]")
    sentence_ko = soup.find('div', attrs={'class':'text_ko'}).get_text()
    print(sentence_ko)






# if __name__ == '__main__':  # scrape_weather()라는 함수가 같은파일(A020_project.py)안에 있다면 실행하게
    # scrape_daum_news()          # 다음 헤드라인 뉴스          
    # scrape_daum_economic_news()       # 다음 경제 뉴스
    # scrape_daum_game()            # 다음 게임
    # scrape_wisesay()              # 오늘의 명언 영어회화
    