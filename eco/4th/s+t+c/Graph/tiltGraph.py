# 저장한 csv 파일을 이용해서 x축은 시간, y축은 각각 x / y / z 의 기울기로 하는 그래프를 그려봅니다.

import matplotlib.pyplot as plt
import pandas as pd

# plot2D 라는 함수를 정의합니다.
def plot2D(xData, yData, i):
    # 그래프의 크기를 정합니다.
    plt.figure(figsize=(30, 10))
    # 그래프 위의 (xData, yData) 위치에 크기가 100인 빨간색 점을 찍습니다.
    plt.scatter(xData, yData, c ='red', s = 100)
    # x축에 라벨을 붙여줍니다.
    plt.xlabel("time", fontsize = 20)
    # y축에 라벨을 붙여줍니다.
    plt.ylabel(i, fontsize = 20)
    # 그래프를 보여줍니다.
    plt.show()

# tiltTime.csv 파일을 읽어서 데이터 프레임 형식으로 df에 저장합니다.
df = pd.read_csv("tiltTime.csv", header=None)
# df의 첫번째 열을 x2D에 저장합니다.
x2D = df[0]
# df의 두번째 열을 y2D에 저장합니다.
y2D = df[1]
# plot2D를 호출해서 x축과 y축 값이 각각 x2D, y2D인 그래프를 그립니다.
plot2D(x2D, y2D,'x')

# df의 세번째 열을 y2D에 저장합니다.
y2D = df[2]
# plot2D를 호출해서 x축과 y축 값이 각각 x2D, y2D인 그래프를 그립니다.
plot2D(x2D, y2D, 'y')

# df의 네번째 열을 y2D에 저장합니다.
y2D = df[3]
# plot2D를 호출해서 x축과 y축 값이 각각 x2D, y2D인 그래프를 그립니다.
plot2D(x2D, y2D, 'z')

