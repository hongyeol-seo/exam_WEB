from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\seo\Desktop\exam_WEB\Day_0130\chromedriver.exe')
driver.get('https://www.coffeebeankorea.com/store/store.asp')

driver.execute_script('storePop2(158)')

html = driver.page_source # page_source: 해당 웹페이지의 소스가 저장됨
soup = BeautifulSoup(html, 'html.parser')

store_names = soup.select("div.store_txt > p.name > span")
store_name_list = []
for name in store_names:
    store_name_list.append(name.get_text())
    print(name.text)



# store_names = soup.select('div.store_txt > p.name > span')
# store_name_list = []
# for name in store_names:
#     store_name_list.append(name.get_text())

# print('매장 개수: ', len(store_name_list))

# print(store_name_list)
# store_addresses = soup.select('p.address > span')
# store_address_list = []
# for addr in store_addresses:
#     print(addr.get_text())
# driver.quit() # web driver 종료