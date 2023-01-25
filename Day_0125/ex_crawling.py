from urllib.request import urlopen
from bs4 import BeautifulSoup as bt
from urllib.error import HTTPError
from urllib.error import URLError

# html = urlopen('https://www.daangn.com/hot_articles')
# html = urlopen('https://blog.naver.com/napolehong92/222992080189')

try : 
    html = urlopen('https://www.chosun.com/')

except HTTPError as e :
    print(e)
except URLError as e :
    print('The server could not be found!')
else :
    print('It worked!')

bs = bt(html.read(),'html.parser')
print(bs.title)

# print(type(html))
# # print(html.read())