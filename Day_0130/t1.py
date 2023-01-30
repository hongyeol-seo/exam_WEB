from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By

#driver = webdriver.Chrome('C:/workspace/chromedriver.exe’) # Windows 사용자

chrome_option = Options() 
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(r'C:\Users\seo\Desktop\exam_WEB\Day_0130\chromedriver.exe')
driver.get('https://nid.naver.com/nidlogin.login')
driver.implicitly_wait(10)
driver.find_element(By.NAME, 'id').send_keys("napolehong92")
driver.find_element(By.NAME, 'pw').send_keys("8583name@@")

# driver.find_element_by_xpath('//*[@id="log.login"]').click()
# driver.get('http://www.pythonscraping.com/pages/warandpeace.html')

# driver.get('https://www.google.com')
# print(driver.current_url)
# print(driver.title)
# print(driver.page_source) # HTML 소스 가져오기
# driver.implicitly_wait(time_to_wait=10)

# name = driver.find_element_by_class_name('green')
# print(name.text)
# print('-' * 20)

# nameList = driver.find_elements_by_class_name('green')
# for name in nameList:
#     print(name.text)

# driver.close() # 하나의 탭만 종료
# driver.quit() # webdriver 전체 종료
