from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.maximize_window()     # 제어창 크기를 최대로

url = 'https://flight.naver.com/flights/'
browser.get(url)   # 제어창의 주소 입력

# 가는날 선택 버튼이 클릭됨     element 에 s가 없는것 사용
browser.find_element_by_link_text('가는날 선택').click()    

# 실제 가는날 선택  elements 에 s가 있는것 사용 [0]은 이번달 [1]은 다음달 등
browser.find_elements_by_link_text('5')[0].click()

# 오는날 선택
browser.find_elements_by_link_text('7')[0].click()


# 목적지 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 검색 시작
browser.find_element_by_link_text('항공권 검색').click()


# 예외 처리

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    print(elem.text)    # 첫번째 결과 출력
finally:
    browser.quit()  # 예외처리가 끝나면 브라우저 종료
    















