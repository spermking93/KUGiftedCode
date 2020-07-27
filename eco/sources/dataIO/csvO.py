# 2가지 방식을 이용해서 csv파일을 읽어옵니다.
import csv
import pandas as pd


# csvR라는 함수를 정의합니다.
def csvR(inData):
    # inData파일을 읽기 모드로 열어줍니다.
    f = open(inData, 'r', encoding='utf-8')
    
    # csv파일을 읽기 위한 객체를 생성합니다.
    r = csv.reader(f)
    
    # csv파일을 한 줄 씩 읽어옵니다.
    for line in r:
        print(line)

    # 열었던 파일을 닫아줍니다.
    f.close()


# csvR 함수를 호출해서 파일을 읽어줍니다.
csvR("df_outTest.csv")

# pandas를 이용해서 csv파일을 읽어줍니다.
dfTest = pd.read_csv("df_outTest.csv", index_col=0)

# dfTest의 data type을 출력합니다.
print(dfTest.dtypes)

# dfTest를 출력합니다.
print(dfTest)
