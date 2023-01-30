from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome(r'C:\Users\seo\Desktop\exam_WEB\Day_0130\chromedriver.exe')
driver.get('https://blog.naver.com/napolehong92/222996863091')

driver.switch_to.frame('mainFrame')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

whole_border = soup.find('div', {'id': 'whole-border'})
results = whole_border.find_all('div', {'class': 'se-module'})

result1=[]
for result in results:
    print(result.text.replace('\n', ''))
    result1.append(result.text)