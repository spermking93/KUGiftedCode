# 2가지 방법을 이용해서 데이터를 csv파일로 저장해봅니다.
import csv
import pandas as pd


# csvWr이라는 함수를 정의합니다.
def csvWr(i,inData):
    #outTest.csv 파일을 엽니다.
    f = open('outTest.csv', 'a', encoding='utf-8', newline='')

    # csv파일에 적기 위해 객체를 선언합니다.
    wr = csv.writer(f)
    
    # 파일에 데이터를 적습니다.
    wr.writerow([i,inData])
    
    # 열었던 파일을 닫습니다.
    f.close()


# conDf라는 함수를 정의합니다.
def conDf(inData):
    # inData의 header를 num으로 지정하여, dataframe 형식으로 저장합니다.
    dfOut = pd.DataFrame({'num': inData})

    #dfOute을 return 합니다.
    return dfOut


# 0부터 99까지를 list형태로 inCal에 저장합니다.
inCal = list(range(100))

# inCal형태로 출력합니다.
print(inCal)


# for문을 반복하면서 inCal에 있는 데이터를 csv파일에 작성합니다.
for i in range(0, 100):
    csvWr(i, inCal[i])

# list형식의 inCal을 dataframe 형식으로 바꿔서 dfTest에 저장합니다.
dfTest = conDf(inCal)

# dfTest를 출력합니다.
print(dfTest)

# dfTest를 csv형태로 저장합니다.
dfTest.to_csv("df_outTest.csv")
