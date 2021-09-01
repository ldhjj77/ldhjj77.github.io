# 구글 무비 정보 가져오기

import requests
from bs4 import BeautifulSoup


url = 'https://play.google.com/store/movies/top'
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div', attrs={'class': 'WsMG1c nnK0zc'})
print(len(movies))

with open('movie.html', 'w', encoding='utf8') as f:
    # f.write(res.text)     # 일반적인 방식
    f.write(soup.prettify())    # html 파일을 다듬어서 출력해줌




















