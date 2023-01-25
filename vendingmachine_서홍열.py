# 1. 화면상에 메뉴를 출력함 (종료를 선택할 때까지 반복, while문 사용)
# 2. 자판기 초깃값 설정
# 3. 메뉴에 따른 재료 차감
# 4. 재고현황에서 현상황 체크

def menu():
    print(f'      커피 자판기 (300원)')
    print(f'1.블랙커피')
    print(f'2.프림커피')
    print(f'3.설탕프림커피')
    print(f'4.재고현황커피')
    print(f'5.종료')
    
    return int(input("메뉴를 선택하세요 : "))
    


def start(coin):

    COFFEE = 300
    balance = 10000
    coffee_bean = 500
    coffee_cream = 500
    coffee_suger = 500
    water = 1000
    cupNum = 30
    coin = coin

    while True :
            
        #메뉴
        menuNum = menu()

        #메뉴선택

        # - 블랙커피: 커피 30g + 물 100ml
        # - 프림커피: 커피 15g + 프림 15g + 물 100ml
        # - 설탕커피: 커피 10g + 프림 10g + 설탕 10g + 물 100ml
        if coin < 300 :
            print(f'잔돈이 부족해서 종료합니다. : {coin}')
            break

        if menuNum == 1:
            #블랙커피
            print(f'블랙커피를 선택하셨습니다.',end='\t')
            if coin < 300 :
                print(f'잔돈이 부족해서 종료합니다.')
                print("-"*20)
                break

            if coffee_bean >= 30 and water >= 100 and cupNum > 0 :
                coffee_bean -= 30
                water -= 100
                cupNum -= 1
                coin -= 300
                balance += 300
                print(f'잔돈 : {coin}')
                print("-"*20)

        elif menuNum == 2:
            #프림커피
            print(f'프림커피를 선택하셨습니다.',end='\t')
            if coin < 300 :
                print(f'잔돈이 부족해서 종료합니다.')
                print("-"*20)
                break

            if coffee_bean >= 15 and coffee_cream >= 15 and water >= 100 and cupNum > 0 :
                coffee_bean -= 15
                coffee_cream -= 15
                water -= 100
                cupNum -= 1
                coin -= 300
                balance += 300
                print(f'잔돈 : {coin}')
                print("-"*20)
                
        elif menuNum == 3:
            print(f'설탕프림커피를 선택하셨습니다.',end='\t')
            
            if coin < 300 :
                print(f'잔돈이 부족해서 종료합니다.')
                print("-"*20)
                break#설탕프림커피
            
            if coffee_bean >= 10 and coffee_cream >= 10 and coffee_suger >= 10 and water >= 100 and cupNum > 0 :
                coffee_bean -= 10
                coffee_cream -= 10
                coffee_suger -= 10
                water -= 100
                cupNum -= 1
                coin -= 300
                balance += 300
                print(f'잔돈 : {coin}')
                print("-"*20)

        elif menuNum == 4:

            print(f'커피 : {coffee_bean}g',end=" ")
            print(f'프림: {coffee_cream}g',end=" ")
            print(f'설탕: {coffee_suger}g',end=" ")
            print(f'물: {water}ml',end=" ")
            print(f'컵: {cupNum}개',end=" ")
            print(f'잔돈현황:{coin}개',end=" ")
            print(f'자판기남은돈:{balance}원')

        elif menuNum == 5:
            print(f'커피 자판 동작을 종료합니다.')
            print("-"*20)
            break
        

coin = int(input('동전을 투입하세요. : '))

    #동전투입
if coin < 300 :
    print(f'돈이 부족합니다.')
    print("-"*20)
    print(f'커피 자판 동작을 종료합니다.')
    print("-"*20)
else :
    start(coin)

