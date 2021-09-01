from bs4 import BeautifulSoup
import urllib.request as req
import urllib.request






#####################            리포터 뉴스
def repoter():
    url = "https://www.inven.co.kr/webzine/news/?site=diablo2"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('td', attrs={'class':'left name game-review-no-score'})
    data = soup[0].find('span', attrs={'class':'title'}).get_text()
    data1 = soup[1].find('span', attrs={'class':'title'}).get_text()
    data2 = soup[2].find('span', attrs={'class':'title'}).get_text()
    link = soup[0].find('a')['href']
    link1 = soup[1].find('a')['href']
    link2 = soup[2].find('a')['href']
    print('리포터 뉴스1 : '+data)
    print('링크 : '+link)
    print('리포터 뉴스2 : '+data1)
    print('링크 : '+link1)
    print('리포터 뉴스3 : '+data2)
    print('링크 : '+link2)
    print()
    print()
    
    

def usernews():
    url = "https://www.inven.co.kr/board/diablo2/5733"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('td', attrs={'class':'bbsSubject'}, limit=5)
    for index, news in enumerate(soup):
        data = news.find('a').get_text()
        link = news.find('a')['href']
        print('유저소식 {0} : {1} '.format(index+1, data))
        print(' 링크 : {0} '.format(link))
    print()
    print()
        

    

def tip():
    url = "https://www.inven.co.kr/board/diablo2/5734"
    res = urllib.request.urlopen(url)
    source = res.read()
    res.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('td', attrs={'class':'bbsSubject'}, limit=10)
    for index, news in enumerate(soup):
        data = news.find('a').get_text()
        link = news.find('a')['href']
        print('유저소식 {0} : {1} '.format(index+1, data))
        print(' 링크 : {0} '.format(link))
    
    
    
   
    
    
if __name__ == '__main__':  # scrape_weather()라는 함수가 같은파일(A020_project.py)안에 있다면 실행하게
    repoter()     # 리포터 게시판
    usernews()    # 유저정보 게시판
    tip()           # 팁게시판
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    