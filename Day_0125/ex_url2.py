from bs4 import BeautifulSoup

html_example = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BeautifulSoup 활용</title>
</head>
<body>
<h1 id="heading">Heading 1</h1>
<p>Paragraph</p>
<span class="red">BeautifulSoup Library Examples!</span>
<div id="link">
<a class="external_link" href="www.google.com">google</a>
<div id="class1">
<p id="first">class1's first paragraph</p>
<a class="external_link" href="www.naver.com">naver</a>
<p id="second">class1's second paragraph</p>
<a class="internal_link" href="/pages/page1.html">Page1</a>
<p id="third">class1's third paragraph</p>
</div>
</div>
<div id="text_id2">
Example page
<p>g</p>
</div>
<h1 id="footer">Footer</h1>
</body>
</html>
'''

soup = BeautifulSoup(html_example, 'html.parser')
head = soup.select_one('head')
print(head)
h1 = soup.select_one('#footer').get_text # 첫 번째 <h1>태그 선택
print(h1)


div_urls = soup.select('div#class1 > a')
print(type(div_urls[0]))


# print(div_urls[0]['href'])

h1 = soup.select('#heading, #footer')
print(h1)



national_anthem = '''
<!DOCTYPE html>
<html lang="en">
<head>
<title>애국가</title>
</head>
<body>
<div>
<p id="title">애국가</p>
<p class="content">
동해물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세.<br>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
</p>
<p class="content">
남산 위에 저 소나무 철갑을 두른 듯 바람서리 불변함은 우리 기상일세.<br>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
</p>
<p class="content">
가을 하늘 공활한데 높고 구름 없이 밝은 달은 우리 가슴 일편단심일세.<br>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
</p>
<p class="content">
이 기상과 이 맘으로 충성을 다하여 괴로우나 즐거우나 나라 사랑하세.<br>
무궁화 삼천리 화려 강산 대한 사람 대한으로 길이 보전하세.<br>
</p>
</div>
</body>
</html>
'''
soup = BeautifulSoup(national_anthem, 'html.parser')
contents = soup.select('p.content')
for content in contents:
    print(content.text) 