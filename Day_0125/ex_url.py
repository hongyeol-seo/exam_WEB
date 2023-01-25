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
print(soup.title) # <title> 태그 전체를 가져옴
print(soup.title.text) # <title>태그의 텍스트만 리턴
print(soup.title.get_text()) # .text와 동일한 기능
print("-" * 50)
print(soup.title.parent)
print("-" * 50)
print(soup.body)
print("-" * 50)
print(soup.h1)
print("-" * 50)
print(soup.h1.text)
print("-" * 50)
print(soup.find('div'))
print(soup.find('div').get_text)
print("-" * 50)
div_text = soup.find('div', {'id':'text_id2'}).find('p').get_text()
print(div_text)


# tr = '''
# <table>
# <tr class="passed a b c" id="row1 example"><td>t1</td></tr>
# <tr class="failed" id="row2"><td>t2</td></tr>
# </table>
# '''
# table = BeautifulSoup(tr, 'html.parser')
# for row in table.find_all('tr'):
#     print(row)
#     print(row.attrs)

print('-----------------------------------------------')
div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))

list_div_tags = list(div_tags)


for i in range(len(div_tags)):
    print('-----------------------------------------------')
    print(list_div_tags[i])
    # print(div)


links = soup.find_all('a')
for alink in links:
    print(alink)
    print('url:{0}, text:{1}'.format(alink['href'], alink.get_text()))
    print()