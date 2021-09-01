# deguwedurl = 'https://weather.naver.com/today/06110101' # 날씨1 주소
# deguwed1 = requests.get(deguwedurl)
# deguwed1.raise_for_status()
# deguwedso1 = BeautifulSoup(deguwed1.text, 'lxml')

# deguwedurl1 = 'https://weather.naver.com/today/06140530' # 날씨2 주소
# deguwed11 = requests.get(deguwedurl1)
# deguwed11.raise_for_status()
# deguwedso11 = BeautifulSoup(deguwed11.text, 'lxml')


# deguwedur2 = 'https://weather.naver.com/air/06110101'   # 미세먼지1 주소
# deguwed2 = requests.get(deguwedur2)
# deguwed2.raise_for_status()
# deguwedso2 = BeautifulSoup(deguwed2.text, 'lxml')

# deguwedur22 = 'https://weather.naver.com/air/06140530'   # 미세먼지2 주소
# deguwed22 = requests.get(deguwedur22)
# deguwed22.raise_for_status()
# deguwedso22 = BeautifulSoup(deguwed22.text, 'lxml')

# # 맑음 어제보다 00도 높아요
# wed1 = deguwedso1.find("span", attrs={"class": "weather before_slash"}).get_text()
# wed2 = ', 어제보다 ' + deguwedso1.find("p", attrs={"class": "summary"}).span.get_text()
# print(wed1 + wed2)

# # 현제온도 00도
# print(deguwedso1.find("div", attrs={"class": "weather_area"}).strong.get_text())
# # 최저 평균기온 00도
# print('최저', deguwedso1.find("span", attrs={"class": "data lowest"}).get_text())
# # 최고 평균기온 00도
# print('최고', deguwedso1.find("span", attrs={"class": "data highest"}).get_text())

# #강수 확률 오전 오후 클레스 이름이 같아서 같은값이 설정됨
# print('오전', deguwedso1.find("span", attrs={"class": "rainfall"}).get_text())
# print('오후', deguwedso1.find("span", attrs={"class": "rainfall"}).get_text())

# # 미세먼지 마찬가지로 클레스 이름이 같아서 같은값이 설정됨
# print('미세먼지', deguwedso2.find("span", attrs={"class": "grade_value level4_1"}).get_text())
# print('초미세먼지', deguwedso2.find("span", attrs={"class": "grade_value level4_1"}).get_text())

# # 날씨 끝


# # 해드라인 뉴스

# newsurl = 'https://news.naver.com/main/home.nhn'
# headers  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
# news1 = requests.get(newsurl, headers=headers)
# news1.raise_for_status()
# newsso = BeautifulSoup(news1.text, 'lxml')

# # head1 = newsso.find_all("ul", attrs={"class": "hdline_article_list"})
# # headnewsall = newsso.find("ul", attrs={"class": "hdline_article_list"}).get_text()  # 제목을 텍스트만
# # headnewsall = headnewsall.strip()

# # print(headnewsall)

# headnewsall1 = newsso.find("ul", attrs={"class": "hdline_article_list"})    # 제목부분 전체
# newstitle = headnewsall1[0].a.get_text()

# print(newstitle)



# link = head1[00].a['href']
# link1 = 'https://news.naver.com' + link
# print(link1)
# print(headnewsall1)


# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href']
# print(title)
# print(link)
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = 'https://comic.naver.com' + cartoon.a['href']
#     print(title, link) 
                                    
