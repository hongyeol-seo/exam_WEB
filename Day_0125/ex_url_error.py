Efrom urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url, tag):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        value = bsObj.body.find(tag)
    except AttributeError as e:
        return None

    return value

url = 'https://coop.knu.ac.kr/sub03/sub01_01.html?shop_sqno=85'
url = 'http://www.pythonscraping.com/pages/page1.html'

tag = 'h2'
value = getTitle(url , tag)
if value == None:
    print(f'{tag} could not be found')
else:
    print(value)