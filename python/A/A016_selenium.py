# pip install selenium
# 크롬웹드라이브 다운받아서 작업폴더에 넣기
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')
# 크롬의 웹드라이브 위치 지정(chromedriver.exe 파일이 있는 위치)




# 터미널 창에서 python 쳐서 쉘창으로 전환
# from selenium import webdriver 쳐서 모듈불러오기
# browser = webdriver.Chrome()  제어된 크롬창이 뜸
# browser.get('http://naver.com')   제어창에 네이버 창이 뜸
# elem = browser.find_element_by_class_name('link_login') 
# 로그인 페이지의 정보를 elem 변수에 저장
# elem.click() 로그인 버튼을 클릭함
# browser.back   페이지가 뒤로 감 browser.forword  다시 로그인 페이지로 감              
# elem = browser.find_element_by_id('query')  elem에 검색창 정보를 저장
# elem 정보 저장
# from selenium.webdriver.common.keys import Keys  키 모듈 불러오기
# elem.send_keys('영화순위')    검색창에 영화순위 라는 글자가 입력됨
# elem.send_keys(Keys.ENTER)    검색시작됨
# browser.close() # browser = webdriver.Chrome() 명령어도 띄워놓은 창 닫기
# browser.quit() 브라우저 종료











