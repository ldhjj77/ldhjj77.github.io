# 네이버 로그인 (Webdriver를 이용)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


naver = 'https://www.naver.com/'
browser = webdriver.Chrome()
browser.get(naver)
# browser.find_element_by_class_name('link_login').click()
browser.find_element_by_xpath('//*[@id="da_timeboard"]/div').click()
time.sleep(5)
# browser.find_element_by_id('id').send_keys('naverid')   
# browser.find_element_by_id('pw').send_keys('naverpw')
# browser.find_element_by_id('id').clear()   # 입력했던 택스트를 지움
# browser.find_element_by_id('id').send_keys('idnaver')
# browser.find_element_by_id('log.login').click()

# print(browser.page_source)  # 네이버페이지 소스 출력














