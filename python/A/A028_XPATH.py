from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('http://naver.com')

# elem = browser.find_element_by_class_name('link_login')
# elem.click()
elem = browser.find_element_by_id('query')
elem.send_keys('영화순위')
elem.send_keys(Keys.ENTER)
time.sleep(60)


















