from urllib.request import	urlopen
from bs4	import	BeautifulSoup

html	=	urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
soup	=	BeautifulSoup(html,	"html.parser")

nameList =	soup.find_all('span',	{'class':	'green'})
for	name	in	nameList:
    print(name.get_text())

princeList = soup.find_all(text='the prince')

print(princeList)
print('the prince count: ', len(princeList))                                                                               

# breakpoint 실행
# F5 : 디버깅시작
# Step over(F10) : 한 라인씩 실행
# Step into(F11) : 
# - continue : 다음 번 breakpoint 에서 멈춤
# - breakpoint가 없으면, 프로그램 실행
# 호출스택
# 중단점

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id':'giftList'})
for child in table_tag.children:
    print(child)


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')
# 정규식: ('img.*\.jpg'): img 다음에 임의의 한 문자가 0회 이상: img.jpg, img1.jpg, imga.jpg 등
img_tag = re.compile('/img/gifts/img.*.jpg')

# find_all()에서 img의 src 속성값에 정규식 사용
images = soup.find_all('img', {'src': img_tag})
for image in images:
    print(image, end=" -> ['src'] 속성: ")
    print(image['src'])

lookbehind1 = re.search('(?<=am).+', '2023-01-26 am 11:10:01')
print(lookbehind1)