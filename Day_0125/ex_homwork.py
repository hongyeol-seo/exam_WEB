'''
데이터크롤링과 정제
과제 #1

National Weather Service 웹사이트 (샌프란시스코 지역)
- https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

def parse_use_find(html):
    '''
    find() 함수를 사용하여 html  내용을 크롤링
    :param html:
    :return:
    '''
    print('[find 함수 사용]')
    
    seven_day = html.find(id='seven-day-forecast-container')
    forecast_items = seven_day.find_all(class_='tombstone-container') #리스트로 반환 #호출에 의한 참조
    print('총 tomestone-container 검색 개수: ', len(forecast_items))

    for day in forecast_items:             
        period = day.find('p', {'class' : 'period-name'}).text
        img_desc = day.find('img')['title'] # img의 'title' 속성값 가져오기
        short_desc = day.find('p', class_='short-desc').text
        temp = day.find('p', class_='temp').text
            
        print('-' * 80)
        print('[Period]: {0}'.format(period))
        print('[Short desc]:  {0}'.format(short_desc))
        print('[Temperature]: {0}'.format(temp))
        print('[Image desc]: {0}'.format(img_desc))
        
    print('-' * 80)

def parse_use_select(html):
    '''
    select 함수를 사용하여 html 내용을 크롤링
    '''
    print('[select 함수 사용]')
    seven_day = html.select_one('div #seven-day-forecast-container')
    forecast_items = seven_day.select('.tombstone-container')
    print('총 tomestone-container 검색 개수: ', len(forecast_items))
    #중간에 break 포인트를 넣는 이유 : 디버깅. #적당한 위치에서 프린티하는 법 / #시스템의 부화를 안주는 선에서 디버깅 메시지를 
    #기지국 통신에서 갑작스런 전화가 발생하는 상황이 아닌 이상, 적절한 프린트 문을 만들어주는 것이 좋다.
    for day in forecast_items:        
        period = day.select_one('.period-name').text
        img_desc = day.select_one('img')['title']
        short_desc = day.select_one('.short-desc').text
        temp = day.select_one('.temp').text
        # img의 'title' 속성값 가져오기
        
        print('-' * 80)
        print('[Period]: {0}'.format(period))
        print('[Short desc]:  {0}'.format(short_desc))
        print('[Temperature]: {0}'.format(temp))
        print('[Image desc]: {0}'.format(img_desc))

def main():
    page = urlopen('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')
    html = BeautifulSoup(page.read(), 'html.parser')

    print('National Weather Service Scraping')
    print('----------------------------------')

    parse_use_find(html)
    parse_use_select(html)

main()

# 
import requests
from bs4 import BeautifulSoup

url='https://search.naver.com/search.naver?query=대구+날씨'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

# 위치 
address_area = soup.find('div', {'class':'title_area _area_panel'})
address = address_area.find('h2', {'class':'title'}).text
print('현재 위치: ', address)

# 날씨 정보 
weather_data = soup.find('div', {'class':'weather_info'})

# 현재 온도 
weather_temp = weather_data.find('div', 
                                  {'class': 'temperature_text'}).text.strip() #뒤에 공백을 업애주기 위해서
print('현재 온도: ', weather_temp)

# 날씨 상태 
weather_status = weather_data.find('span', {'class':'weather before_slash'}).text
print('날씨 상태: ', weather_status)

# 미세 먼지, 초미세 먼지, 자외선, 일출
# clss="today_chart_list"
air = soup.find('ul', {'class':'today_chart_list'})

air_all_info = air.find_all('li', {'class':'item_today'})
print('공기 상태: ')
for info in air_all_info:
    print(info.text.strip())

# 날씨, 강수 
weather_time = soup.find_all('li', {'class': '_li'})
print('-----------------------')
print('시간대별 날씨 및 온도')
print('-----------------------')
for i in weather_time:
    print(i.text.strip())