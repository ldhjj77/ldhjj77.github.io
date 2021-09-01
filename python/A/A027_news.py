from bs4 import BeautifulSoup
import urllib.request
import time



def jtbc_news():
    url = "https://news.jtbc.joins.com/default.aspx"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('div', attrs={'class':'feed_img'}, limit=10)
    # print(soup)
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))
    # print(now)
    with open('./A/{0}_news.txt'.format(now), 'w') as f: # 피씨게임 이미지 파일생성
        f.write('오늘의 주요 뉴스\n\n')
    for index, news in enumerate(soup):
        data = news.find('a').get_text()
        link = news.find('a')['href']
        print('jtbc 뉴스 {0} : {1} '.format(index+1, data))
        print(' 링크 : {0} '.format(link))
        with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
            f.write('jtbc_news {0} : {1} \n\n'.format(index+1, data))
    with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
        f.write('\n\n\n')
    print()
    print()




def psy_cardnews():
    url = "http://www.psychiatricnews.net/news/articleList.html?sc_section_code=S1N23&view_type=sm"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('h4', attrs={'class':'titles'}, limit=10)
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))
    # print(soup)
    for index, news in enumerate(soup):
        data = news.find('a').get_text()
        link = news.find('a')['href']
        print('카드뉴스 {0} : {1} '.format(index+1, data))
        print(' 링크 : {0} '.format('http://www.psychiatricnews.net'+link))
        with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
            f.write('psy_cardnews {0} : {1} \n\n'.format(index+1, data))
    with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
        f.write('\n\n\n')
    print()
    print()


def sciencetimes():
    url = "https://www.sciencetimes.co.kr/category/sci-tech/"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('div', attrs={'class':'board_cont'}, limit=9)
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))
    # print(soup)
    for index, news in enumerate(soup):
        data = news.find('strong').get_text()
        link = news.find('a')['href']
        print('과학 기술 {0} : {1} '.format(index+1, data))
        print(' 링크 : {0} '.format(link))
        with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
            f.write('sciencetimes {0} : {1} \n\n'.format(index+1, data))
    with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
        f.write('\n\n\n')
    print()
    print()
    
    
def ilovepc():
    url = "http://www.ilovepc.co.kr/news/articleList.html?sc_section_code=S1N1&view_type=sm"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('div', attrs={'class':'list-titles'}, limit=8)
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))
    # print(soup)
    for index, news in enumerate(soup):
        data = news.find('strong').get_text()
        link = news.find('a')['href']
        print('피시 사랑 {0} : {1} '.format(index+1, data))
        print(' 링크 : {0} '.format('http://www.ilovepc.co.kr'+link))
        with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
            f.write('ilovepc {0} : {1} \n\n'.format(index+1, data))
    with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
        f.write('\n\n\n')
    print()
    print()


def kormedi():
    url = "http://kormedi.com/healthnews/"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('h2', attrs={'class':'title'}, limit=16)
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))
    # print(soup)
    for index, news in enumerate(soup):
        data = news.find('a').get_text().strip()
        link = news.find('a')['href']
        print('코메디 {0} : {1} '.format(index+1, data))
        print(' 링크 : {0} '.format(link))
        with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
            f.write('kormedi {0} : {1} \n\n'.format(index+1, data))
    with open('./A/{0}_news.txt'.format(now), 'a') as f: # 피씨게임 이미지 파일생성
        f.write('\n\n\n')
    print()
    print()




if __name__ == '__main__':  # scrape_weather()라는 함수가 같은파일(A020_project.py)안에 있다면 실행하게
    jtbc_news()            # jtbc 뉴스
    # psy_cardnews()    # 정신의학 카드뉴스
    # sciencetimes()    # 과학 뉴스
    # ilovepc()         # 피시사랑 뉴스
    # kormedi()         # 코메디 뉴스
    















