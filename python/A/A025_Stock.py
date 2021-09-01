from bs4 import BeautifulSoup
import urllib.request as req
import urllib.request


######################                 환율
def Exchange_Rate():
    url = 'https://finance.naver.com/marketindex/'
    res = req.urlopen(url)
    soup = BeautifulSoup(res,'html.parser', from_encoding='euc-kr')
    name_nation = soup.select('h3.h_lst > span.blind')
    name_price = soup.select('span.value')

    i = 0
    for c_list in soup:
        try:
            print(i+1, name_nation[i].text, name_price[i].text)
            i = i + 1
        except IndexError:
            pass




#####################            코스피 지수
def kospi():
    url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
    fp = urllib.request.urlopen(url)
    source = fp.read()
    fp.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('div', attrs={'id':'quotient'})
    kos = soup[0].get_text().strip()
    print()
    print('코스피 지수 : ' + kos)




#####################            코스닥 지수
def kosdaq():
    url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ"
    fp = urllib.request.urlopen(url)
    source = fp.read()
    fp.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.find_all('div', attrs={'id':'quotient'})
    kos = soup[0].get_text().strip()
    print()
    print('코스닥 지수 : ' + kos)





####################             다우지수 
def dau():
    url = "https://finance.naver.com/world/sise.nhn?symbol=DJI@DJI"
    fp = req.urlopen(url)
    source = fp.read()
    fp.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("em")
    # print(soup)
    dau = soup[2].get_text().strip()
    dau1 = soup[3].get_text().strip()
    dau2 = soup[4].get_text().replace("\n", "").strip()
    print()
    print('다우지수 : '+ dau )
    print('전일대비 : '+ dau1 + dau2)  



####################             나스닥 지수 
def nasdaq():
    url = "https://finance.naver.com/world/sise.nhn?symbol=NAS@IXIC"
    fp = req.urlopen(url)
    source = fp.read()
    fp.close()
    soup = BeautifulSoup(source, 'html.parser')
    soup = soup.findAll("em")
    # print(soup)
    dau = soup[2].get_text().strip()
    dau1 = soup[3].get_text().strip()
    dau2 = soup[4].get_text().replace("\n", "").strip()
    print()
    print('나스닥지수 : '+ dau )
    print('전일대비 : '+ dau1 + dau2)


    
if __name__ == '__main__':  # scrape_weather()라는 함수가 같은파일(A020_project.py)안에 있다면 실행하게
    Exchange_Rate()
    kospi()
    kosdaq()
    dau()
    nasdaq()




   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    