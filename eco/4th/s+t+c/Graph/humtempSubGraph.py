# 저장한 csv 파일을 이용해서 x좌표는 시간, y좌표는 각각 습도와 온도인 그래프를 한 화면에 그려봅니다.

import matplotlib.pyplot as plt
import pandas as pd

# humtempTime.csv 파일을 읽어서 데이터 프레임 형식으로 df에 저장합니다.
df = pd.read_csv("humtempTime.csv", header=None)
# df의 첫번째 열을 x2D에 저장합니다.
x2D = df[0]
# df의 두번째 열을 y2Dhum에 저장합니다.
y2Dhum = df[1]
# df의 세번째 열을 y2Dtemp에 저장합니다.
y2Dtemp = df[2]

# 그래프 크기를 정합니다.
plt.figure(figsize=(30, 10))

# 그래프가 그려질 위치를 정합니다.
plt.subplot(1, 2, 1)
# 그래프 위에 (x2D, y2Dhum)위치에 크기는 100인 점을 찍습니다.
plt.scatter(x2D, y2Dhum, s = 100)
# x축에 라벨을 붙여줍니다.
plt.xlabel("time", fontsize = 20)
# y축에 라벨을 붙여줍니다.
plt.ylabel("hum", fontsize = 20)

# 그래프가 그려질 위치를 정합니다.
plt.subplot(1, 2, 2)
# 그래프 위에 (x2D, y2Dtemp) 위치에 크기는 100인 점을 찍습니다.
plt.scatter(x2D, y2Dtemp, s = 100)
# x축에 라벨을 붙여줍니다.
plt.xlabel("time", fontsize = 20)
# y축에 라벨을 붙여줍니다.
plt.ylabel("temp", fontsize = 20)

# 그래프를 보여줍니다.
plt.show()


