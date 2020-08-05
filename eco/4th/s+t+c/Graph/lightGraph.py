# 저장한 csv 파일을 이용해서 x축이 시간, y축이 lux인 그래프를 그려봅니다.

import matplotlib.pyplot as plt
import pandas as pd

# plot2D 함수를 정의합니다.
def plot2D(xData, yData):
    # 그래프의 사이즈를 정합니다.
    plt.figure(figsize=(30, 10))

    # 그래프 위의 (xData, yData) 위치에 빨간색의 크기는 100인 점을 찍습니다.
    plt.scatter(xData, yData, c='red', s = 100)

    # x축에 label을 붙여줍니다.
    plt.xlabel('time', fontsize = 20)
    # y축에 label을 붙여줍니다.
    plt.ylabel('lux', fontsize = 20)
    # 그래프를 화면에 띄웁니다.
    plt.show()

# lightTime.csv 파일을 읽어 데이터 프레임 형식으로 df에 저장합니다.
df = pd.read_csv("lightTime.csv", header=None)
# df의 첫번째 열을 x2D에 저장합니다.
x2D = df[0]
# df의 두번째 열을 y2D에 저장합니다.
y2D = df[1]

# plot2D 함수를 호출하여 x2D를 x값으로, y2D를 y값으로 하는 산점도 그래프를 그립니다.
plot2D(x2D, y2D)
