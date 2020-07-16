# 데이터를 csv로 저장하고 저장한 csv파일을 읽어봅니다.

import csv
import numpy as np


# calData라는 함수를 정의합니다.
def calData(inData,w,b):
    # inData에 w를 곱해주고, b를 더해서 outData에 저장합니다.
    outData = w * inData + b

    # outData를 반환합니다.
    return outData


# csvWr라는 함수를 정의합니다.
def csvWr(i,inData):
    # outTest.csv라는 이름을 가진 파일을 쓰기모드로 열어줍니다. outTest.csv라는 이름을 가진 파일이 없다면 생성합니다.
    f = open('outTest.csv', 'w', encoding='utf-8', newline='')

    # 파일에 작성하기 위해 객체를 만들어줍니다.
    wr = csv.writer(f)

    # csv파일에 write 작업을 수행합니다.
    wr.writerow([i,inData])

    # 파일을 닫습니다.
    f.close()


# csvR이라는 함수를 정의합니다.
def csvR(inData):
    # 파일명이 inData인 파일을 읽기모드로 열어줍니다.
    f = open(inData, 'r', encoding='utf-8')
    
    # 파일을 읽기 위해 객체를 만들어줍니다.
    r = csv.reader(f)
    
    # csv파일을 한줄씩 읽어서 출력합니다.
    for line in r:
        print(line)

    # 파일을 닫습니다.
    f.close()


# inCal에 0부터 99까지의 숫자를 저장합니다.
inCal = np.array(range(100))

# inCal을 출력합니다.
print(inCal)

# calData를 호출해서 calData의 결과값을 testCal에 저장합니다.
testCal = calData( inCal , 10. , 10. )  

# testCal을 출력합니다.
print(testCal)

# csvWr함수를 호출헤서 csv파일을 작성합니다.
csvWr(0,testCal)

# csvR함수를 호출해서 outTest.csv파일을 읽습니다.
csvR("outTest.csv")

