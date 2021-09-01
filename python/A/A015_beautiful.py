# 웹 크롤링 / 웹 스크레핑
# pip install --upgrade pip
# pip install requests
# pip install beautifulsoup4
# pip install lxml
from os import name
import requests
import re
from bs4 import BeautifulSoup

# 네이버 웹툰
# url = 'https://comic.naver.com/webtoon/weekday.nhn'
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)   # a 태그가 맨 처음 발견된거 출력
# print(soup.a['href'])   # a 태그로 시작하는것 중 href 라는 속성인 것을 출력
# print(soup.a.attrs)     # a 태크의 모든 속성 정보 출력
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# print(soup.find(attrs={"class": "Nbtn_upload"}))
# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a)
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)

# webtoon = soup.find('a', text="신의 탑")
# print(webtoon)


# 전체목록 가져오기
# cartoons = soup.find_all('a', attrs={'class':'title'})      
# # find는 한개만 찾고 find_all은 해당하는 모든걸 가져옴
# # print(cartoons)               # 테그를 포함한것들을 출력
# for cartoon in cartoons:
#     print(cartoon.get_text())   # 테그제외하고 텍스트만 출력








# 나노마신
nano = 'https://comic.naver.com/webtoon/list.nhn?titleId=747271'
res = requests.get(nano)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')


# 제목과 링크걸기
cartoons = soup.find_all('td', attrs={"class":"title"})
title = cartoons[0].a.get_text()
link = cartoons[0].a['href']
print(title)
print(link)
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = 'https://comic.naver.com' + cartoon.a['href']
    print(title, link) 



# 평점 구하기
total_rates = 0
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find('strong').get_text()    # 평점
    print(rate)
    total_rates += float(rate)
print('전체 점수 : ', round(total_rates, 2))
print('평균 점수 : ', round(total_rates / len(cartoons), 2))



# URL 요청이 안될경우
# 유저에이전트를 입력해주는 방법
# nano = 'https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user'
# headers = {'User=Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
# # 유저 에이전트 추가

# res = requests.get(nano, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, 'lxml')

# print(res.text)

# selenium framework 사용




# 이미지 가져오기

# res = requests.get('https://search.daum.net/search?w=tot&q=2020%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR')
# res.raise_for_status()
# soup = BeautifulSoup(res.text, 'lxml')

# images = soup.find_all('img', attrs={'class':'thumb_img'})

# for idx, image in enumerate(images):
#     # print(image['src'])
#     image_url = image['src']
#     if image_url.startswith('//'):
#         image_url = 'https:' + image_url
#     image_res = requests.get(image_url)
#     image_res.raise_for_status()
#     print(image_url)
    
#     with open('movie{0}.jpg'.format(idx+1), 'wb') as f: # 파일생성
#         f.write(image_res.content)
    
#     if idx >= 4:
#         break






































