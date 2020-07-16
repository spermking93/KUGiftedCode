# 앞에서 저장한 csv파일 데이터를 그래프로 그려봅니다.

import numpy as np
import matplotlib.pyplot as plt
import csv
import re


# plot2D라는 함수를 정의합니다.
def plot2D(xData, yData):
    # 그래프가 보여질 사진의 크기를 5 x 5로 정의합니다.
    plt.figure(figsize=(5, 5))

    # x값, y값, 그래프의 색상, 점의 크기를 정의합니다.
    plt.scatter(xData, yData, c='blue', alpha=0.2)

    # 그래프를 그립니다.
    plt.show()


# csvR이라는 함수를 정의합니다.
def csvR(inData):
    # 파일명이 inData인 파일을 읽기모드로 열어줍니다.
    f = open(inData, 'r', encoding='utf-8')

    # 파일을 읽기 위한 객체를 만들어줍니다.
    r = csv.reader(f)

    # csv 파일의 마지막 열만 한줄씩 읽어서 출력합니다.
    for line in r:
        print(line[-1])

    # 파일을 닫습니다.
    f.close()

    # line[-1]을 반환합니다.
    return line[-1]


# inCal에 0부터 99까지 숫자를 저장합니다.
inCal = np.array(range(100))

# inCal을 출력합니다.
print(inCal)

# csvR함수를 호출해서 csvR의 반환값을 out에 저장합니다.
out = csvR("outTest.csv")

# out에 저장되어 있는 값중 숫자만 골라서 outlist에 float형 list로 저장합니다.
outlist = list(map(float, re.findall("\d+", out)))

# outlist를 출력합니다.
print(outlist)

# plot2D함수를 호출해서 그래프를 그립니다.
plot2D(inCal, outlist)

