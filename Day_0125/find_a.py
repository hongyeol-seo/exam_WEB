# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import operator 
import platform 
import os 

'''
    Homework: 알파벳 빈도수 계산 프로그램
    - 파일 입력: 사용자 입력 파일(loremipsum.txt 파일)
    - 딕셔너리 사용: 문자열을 읽어서 각 알파벳 소문자, 대문자의 빈도수를 계산
    - 정렬: 글자의 빈도수를 딕셔너리에 저장하고 내림차순으로 정려
    - 그래프 출력: 내림차순으로 정렬된 딕셔너리를 이용하여 bar chart 출력

'''

def draw_barchart_dict(path, outfile, upper_dict, lower_dict):
    '''
        dictionary를 활용한 bar chart 그리기 
        - subplot을 사용하여 대, 소문자를 한번에 그림  
    '''
    # 한글 폰트 사용 
    if platform.system() == 'Windows':
        plt.rc('font', family='Malgun Gothic')
    elif platform.system() == 'Darwin':  
        # MacOS: Darwin
        plt.rc('font', family='AppleGothic')
    else:
        print('Unsupported System')

    # subplot 사용    
    # figsize=(x, y)  
    fig, axes=plt.subplots(1, 2, figsize=(20, 10))
    fig.suptitle(f'알파벳 카운트: {outfile}')

    # 대문자 bar chart 
    plt.subplot(1, 2, 1)
    plt.title('대문자 개수')
    plt.bar(upper_dict.keys(), upper_dict.values())
    plt.xlabel('Alphabet')
    plt.ylabel("Count")

    # 소문자 bar chart 
    plt.subplot(1, 2, 2)
    plt.title('소문자 개수')
    plt.bar(lower_dict.keys(), lower_dict.values())
    plt.xlabel('Alphabet')
    plt.ylabel("Count")

    # 그래프 파일 저장 

    plt.savefig(path + '/' + outfile+'_count.png')
    print(outfile + "_count.png is saved.")
    plt.close()


def count_alphabet(fname):
    infile = open(fname, "r")
    upperdict = dict()      # Alphabet 대문자 빈도수를 저장하는 딕셔너리
    lowerdict = dict()      # Alphabet 소문자 빈도수 저장하는 딕셔너리

    ch = infile.read(1)
    while ch != "":
        if(ch.isalpha()):
            if(ch.isupper()):
                if(ch not in upperdict):
                    upperdict[ch] = 1
                else:
                    upperdict[ch] += 1
            else:
                if(ch not in lowerdict):
                    lowerdict[ch] = 1
                else:
                    lowerdict[ch] += 1
        ch = infile.read(1)
    infile.close() # 파일 닫기 

    # 두개의 dict를 value 기준으로 내림 차순 정리하고 list 형태로 리턴함
    
    # dictionary의 값을 기준으로 정렬 
    # 람다 사용 
    sorted_upperlist = sorted(upperdict.items(), 
                            key = lambda u : u[1], reverse=True)
    sorted_upperdict = dict(sorted_upperlist)                         

    sorted_lowerlist = sorted(lowerdict.items(), 
                            key = lambda l : l[1], reverse=True)
    sorted_lowerdict = dict(sorted_lowerlist)
    
    # dictionary의 값을 기준으로 내림차순 정렬 
    # opreator.itemgetter(인덱스) 사용
    '''
    sorted_upperlist = sorted(upperdict.items(), 
                            key=operator.itemgetter(1), reverse=True)
    sorted_upperdict = dict(sorted_upperlist) # dict -> list로 변환

    sorted_lowerlist = sorted(lowerdict.items(), 
                              key=operator.itemgetter(1), reverse=True)
    sorted_lowerdict = dict(sorted_lowerlist)
    '''
    return sorted_upperdict, sorted_lowerdict

def main():
    #input_filename = input('Input file name: ')
    input_filename = 'loremipsum.txt'
    #input_filename = 'python.txt'
    print(input_filename)

    # 파일 이름에서 확장자만 제거 
    fname = input_filename.rsplit('.')[0]
    print('파일이름: ', fname)

    # img 폴더에 저장: 폴더가 없으면 새롭게 생성 
    path = 'img'
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            print()
    except Exception as e:
        print('Exception 발생: ', e)

    sorted_upper_dict, sorted_lower_dict = count_alphabet(input_filename)
    
    print('대문자: \n', sorted_upper_dict)
    print('소문자: \n', sorted_lower_dict)

    draw_barchart_dict(path, fname, sorted_upper_dict, sorted_lower_dict) 


main()

