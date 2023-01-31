from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from wordcloud import WordCloud
from	konlpy.tag import	Okt
from	collections	import	Counter
import	matplotlib.pyplot as	plt
import	platform

#각링크주소바로가져오기

driver = webdriver.Chrome(r'C:\Users\seo\Desktop\exam_WEB\Day_0130\chromedriver.exe')
driver.get('https://helloworld.kurly.com/')

html = driver.page_source # page_source: 해당 웹페이지의 소스가 저장됨
soup = BeautifulSoup(html, 'html.parser')

print(soup)
# postTitle = soup.select("h3.post-title")
postUrl = (soup.select("a.post-link"))


# print(len(postTitle))
print(len(postUrl)) #54개

addrUrl = []

for i in postUrl:
    addrUrl.append(i.attrs['href'])
    print(i)


FILE = "https://helloworld.kurly.com/"

for i in range(1):
    #하나씩 들어가서, 정보 다 긁어오기

    print("테스트")
    print(addrUrl[i])

    driver.get('https://helloworld.kurly.com{}'.format(addrUrl[i]))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    test = soup.text.replace("\n","").replace("\t","").split(" ")
    
    counts = Counter(test)
    print(counts)

    tags = counts.most_common(40)


    
        #	WordCloud를 생성
    #	한글을 분석하기위해 font를 한글로 지정해주어야 된다.	
    #	macOS는 .otf ,	window는 .ttf 파일의 위치를 지정 (ex.	'/Font/GodoM.otf')
    if	platform.system()	==	'Windows':
        path	=	r'c:\Windows\Fonts\malgun.ttf'
    elif platform.system()	==	'Darwin':	#	Mac	OS
        path	=	r'/System/Library/Fonts/AppleGothic'
    else:
        path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'
    wc =	WordCloud(font_path=path,	background_color="white",	max_font_size=60)
    cloud	=	wc.generate_from_frequencies(dict(tags))
    #	생성된 WordCloud를 test.jpg로 보낸다.
    #cloud.to_file('test.jpg')
    plt.figure(figsize=(10,	8))
    plt.axis('off')
    plt.imshow(cloud)
    plt.show()


    # content = (soup.select("div.post > p"))
    # arr = []
    # #파일 이름을
    # for i in content:
    #     # writedata.py
    #     arr.append(i.text)
        

    # counts	=	Counter(content)
    # print("*"*50)
    # print(counts)
    # print("*"*50)


    #	WordCloud를 생성
    #	한글을 분석하기위해 font를 한글로 지정해주어야 된다.	
    #	macOS는 .otf ,	window는 .ttf 파일의 위치를 지정 (ex.	'/Font/GodoM.otf')


    # if	platform.system()	==	'Windows':
    #     path	=	r'c:\Windows\Fonts\malgun.ttf'
    # elif platform.system()	==	'Darwin':	#	Mac	OS
    #     path	=	r'/System/Library/Fonts/AppleGothic'
    # else:
    #     path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'
    # wc =	WordCloud(font_path=path,	background_color="white",	max_font_size=60)
    # cloud	=	wc.generate_from_frequencies(dict(tags))
    # #	생성된 WordCloud를 test.jpg로 보낸다.
    # #cloud.to_file('test.jpg')
    # plt.figure(figsize=(10,	8))
    # plt.axis('off')
    # plt.imshow(cloud)
    # plt.show()






    # #파일 이름을
    # for i in content:
    #     # writedata.py
    #     f = open("test.txt", 'a',encoding='utf-8')
    #     data = i.text
    #     f.write(data)
    #     f.close()

# driver = webdriver.Chrome(r'C:\Users\seo\Desktop\exam_WEB\Day_0130\chromedriver.exe')
# driver.get('https://helloworld.kurly.com/blog/aws-mlops-workshop-2022/')

# html = driver.page_source # page_source: 해당 웹페이지의 소스가 저장됨
# soup = BeautifulSoup(html, 'html.parser')
# content = (soup.select("div.post > p"))


# -------------------------------------


# from wordcloud import WordCloud
# from	konlpy.tag import	Okt
# from	collections	import	Counter
# import	matplotlib.pyplot as	plt
# import	platform

# # FILE = r'C:\Users\seo\Desktop\exam_WEB\Day_0130\test.txt'
# FILE = 'test.txt'

# text = open(FILE,encoding='utf-8').read()

# okt = Okt()	#	Open	Korean	Text	객체 생성
# #okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
# sentences_tag =	[]
# sentences_tag =	okt.pos(test)

# # print(sentences_tag)

# noun_adj_list =	[]
# #	tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
# for	word,	tag	in	sentences_tag:
#     if	tag	in	['Noun'	,	'Adjective']:
#         noun_adj_list.append(word)
#         # print(noun_adj_list)
# #	가장 많이 나온 단어부터 40개를 저장한다.

# counts	=	Counter(noun_adj_list)
# # print(f'갯수 {counts}')

# tags	=	counts.most_common(10)
# print(tags)


# #	WordCloud를 생성
# #	한글을 분석하기위해 font를 한글로 지정해주어야 된다.	
# #	macOS는 .otf ,	window는 .ttf 파일의 위치를 지정 (ex.	'/Font/GodoM.otf')
# if	platform.system()	==	'Windows':
#     path	=	r'c:\Windows\Fonts\malgun.ttf'
# elif platform.system()	==	'Darwin':	#	Mac	OS
#     path	=	r'/System/Library/Fonts/AppleGothic'
# else:
#     path	=	r'/usr/share/fonts/truetype/name/NanumMyeongjo.ttf'
# wc =	WordCloud(font_path=path,	background_color="white",	max_font_size=60)
# cloud	=	wc.generate_from_frequencies(dict(tags))
# #	생성된 WordCloud를 test.jpg로 보낸다.
# #cloud.to_file('test.jpg')
# plt.figure(figsize=(10,	8))
# plt.axis('off')
# plt.imshow(cloud)
# plt.show()