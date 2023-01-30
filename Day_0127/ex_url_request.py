from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
home_image = bs.find('img', {'class':'pagelayer-img'})
image_location = home_image['src'] # <img> 태그의 ‘src’ 속성값을 가져옴

print(image_location)
urlretrieve(image_location, 'logo.jpg')