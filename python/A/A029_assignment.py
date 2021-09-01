from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# 네이버 IT/과학뉴스 3개의 제목과 링크 가져오기
# 네이버 웹툰 배스트첼린지에 등록된 웹툰 제목과 평점 가져오기
# 크롬웹드라이브를 활용해 네이버 로그인 하기

def IT_news():
    print('[IT/과학 뉴스]')
    url = 'https://news.naver.com/'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    news_list = soup.find('div', attrs={'id':'section_it'})
    news_list1 = news_list.find_all('li', limit=3)
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))

    for index, news in enumerate(news_list1):        
        title = news.find('a').get_text().strip()
        link = news.find('a')['href']
        print('{0}. {1}'.format(index + 1, title))
        print('(  링크 : {0}  )'.format(link))
        with open('./{0}_news.txt'.format(now), 'a') as f: 
            f.write('[IT/과학 뉴스] {0} : {1} \n\n'.format(index+1, title))
    with open('./{0}_news.txt'.format(now), 'a') as f:
        f.write('\n\n\n')
    print()
    print()
    print()


def bestChallenge():
    print('[bestChallenge]')
    url = 'https://comic.naver.com/genre/bestChallenge.nhn'
    headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')
    now = time.strftime('%Y-%m-%d %H-%M', time.localtime(time.time()))  
    bast = soup.find_all('dl', attrs={'class':'mainTodayGrade'})
    bast1 = soup.find('div', attrs={'class':'mainTodayBox'})
    bast2 = bast1.find_all('h4')
    i = ['1', '2', '3']
    
    for toon, toon1, i1 in zip(bast2, bast, i):
        title = toon.find('a').get_text().strip()
        star = toon1.find('strong').get_text()
        print(' {0}  제목 : {1}  (  평점 : {2}  ) '.format(i1, title, star))
        with open('./{0}_news.txt'.format(now), 'a') as f: 
            f.write('[bestChallenge] {0} 제목 : {1} ( 평점 : {2} ) \n\n'.format(i1, title, star))
    with open('./{0}_news.txt'.format(now), 'a') as f: 
        f.write('')

            

def naver_login():
    naver = 'https://www.naver.com/'
    browser = webdriver.Chrome()
    browser.get(naver)

    browser.find_element_by_xpath('//*[@id="account"]/a').click()
    time.sleep(2)
    browser.find_element_by_id('id').send_keys('naverid')
    time.sleep(1)  
    browser.find_element_by_id('pw').send_keys('naverpw')
    time.sleep(1)  
    browser.find_element_by_id('log.login').click()
    time.sleep(2)  





if __name__ == '__main__':  
    IT_news()          
    bestChallenge()
    # naver_login()












