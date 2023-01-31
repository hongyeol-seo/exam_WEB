from wordcloud import WordCloud
from	konlpy.tag import	Okt
from	collections	import	Counter
import	matplotlib.pyplot as	plt
import	platform

# FILE = r'C:\Users\seo\Desktop\exam_WEB\Day_0130\test.txt'
FILE = 'test.txt'

text	=	open(FILE,encoding='utf-8').read()

okt =	Okt()	#	Open	Korean	Text	객체 생성
#	okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag =	[]
sentences_tag =	okt.pos(text)

# print(sentences_tag)

noun_adj_list =	[]
#	tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for	word,	tag	in	sentences_tag:
    if	tag	in	['Noun'	,	'Adjective']:
        noun_adj_list.append(word)
        # print(noun_adj_list)
#	가장 많이 나온 단어부터 40개를 저장한다.

counts	=	Counter(noun_adj_list)
# print(f'갯수 {counts}')

tags	=	counts.most_common(10)
print(tags)


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

