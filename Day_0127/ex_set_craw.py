from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set() # 세트 선언
count = 0

def getLinks(pageUrl):
    global pages
    html = urlopen('https://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:    
            if link.attrs['href'] not in pages:
                # 새로운 페이지 발견
                newPage = link.attrs['href']
                count += 1
                print('[{0}]: {1}'.format(count, newPage))
                pages.add(newPage)

                return 

                getLinks(newPage)

# 재귀를 보여주기 위해서 만든 함수 
# 파이썬에서

# while True :
#     newPage = ""
#     result = getLinks(newPage)

#     if result != False :
#         getLinks(result)

#     else :
#         break 


# getLinks('')


html = urlopen('https://www.mk.co.kr/news/society/10620094')
bs = BeautifulSoup(html, 'html.parser')
trlist = bs.find_all('p')

for i in trlist:
    print(i)


from urllib.parse import urlparse
urlString1 = 'https://blog.naver.com/napolehong92'
url = urlparse(urlString1)

print(url.scheme)
print(url.netloc) #인터넷 주소
print(url.path)

