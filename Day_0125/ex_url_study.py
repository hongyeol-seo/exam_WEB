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
<span class="red2">BeautifulSoup google Library Examples!</span>
<span class="red3">google</span>

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

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_example, 'html.parser')
# print(soup.find('div').p['id']) #div 태그를 찾아서 p태그 안에 있는 'id'를 속성값을 달라.

# 여러 <div> 태그 중 특정 속성을 가지는 항목 추출
# id속성의 값이 ‘text_id2’인 항목 검색

# print(soup.find('div', {'id':'text_id2'}))
print(soup.find('span', {'class':'red'}))
print(soup.find('span', {'class':'red'}).get_text())

print(soup.find('a', {'class':'internal_link'}))

href_link = soup.find('a', {'class':'internal_link'}) # 딕셔너리 형태
href_link = soup.find('a', class_ ='internal_link') # class는 파이썬 예약어


# <a> 태그 및 <a> 태그의 href 속성 추출

print(href_link) # <a class=”internal_link” …> 태그 전체를 추출
print(href_link['href']) # <a> 태그 내부 href 속성의 값(url)을 추출
print(href_link.get('href')) # ['href']와 동일 기능
print(href_link.text) # <a> Page1 </a>태그 내부의 텍스트(Page1) 추출

print(soup.find_all(keyword ='google'))
