from urllib.request import	urlopen
from bs4	import	BeautifulSoup
import pandas as pd


def save_to_csv() :

    FLIE = r'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store='

        
    a = "https://www.hollys.co.kr/store/korea/korStore2.do?pageNo="
    b = "&sido=&gugun=&store="

    loc = []
    marketName = []
    address = [] 
    tel = []

    # globals()[f'url{i}']=url.format(i)
    # original_html = requests.get(globals()[f'url{i}'])
    # soup = BeautifulSoup(original_html.text, "html.parser")

    for i in range(35):
        
        #30번의 리스트가 돌면서 

        html = urlopen(a+str(i)+b)
        soup = BeautifulSoup(html,"html.parser")
        info = soup.select("tr") #태그 내부
        

        for i in range(1,len(info)):
            loc.append(info[i].select("td")[0].text) #지역
            marketName.append(info[i].select("td")[1].text) #매장명
            address.append(info[i].select("td")[3].text) #현황
            tel.append(info[i].select("td")[5].text) 
            #번호 . 아니면 숫자

    import pandas as pd

    t1 = pd.DataFrame([loc,marketName,address,tel])
    t1 = t1.transpose()
    t1.rename(columns={0:"지역",1:"매장명",2:"현황",3:"번호"},inplace=True)
    print(t1)

    t1.to_csv('s.csv',index=False)


def search_scv() :
    while True :
        location = input("검색할 매장의 도시를 입력해주세요 : ")
        if location == "quit":
            break
        df = pd.read_csv('s.csv')
        df = df[df["지역"].str.contains(location)]
        
        for i in range(len(df)):
            
            print(f'[{i+1}] : {df.iloc[i][0]} ,{df.iloc[i][1]},{df.iloc[i][2]},{df.iloc[i][3]}')

def main():
    save_to_csv()
    search_scv()


main()

