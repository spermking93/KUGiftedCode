# 저장한 csv 파일을 이용해서 x축은 시간, y축은 각각 x / y / z 의 기울기로 하는 그래프를 한 화면에 그려봅니다.

import matplotlib.pyplot as plt
import pandas as pd

# tiltTime.csv 파일을 읽어서 데이터 프레임 형식으로 df에 저장합니다.
df = pd.read_csv("tiltTime.csv", header=None)

# df의 첫번째 열을 x2D에 저장합니다.
x2D = df[0]
# df의 두번째 열을 y2Dx에 저장합니다.
y2Dx = df[1]
# df의 세번째 열을 y2Dy에 저장합니다.
y2Dy = df[2]
# df의 네번째 열을 y2Dz에 저장합니다.
y2Dz = df[3]

# 그래프의 크기를 정합니다.
plt.figure(figsize=(30, 15))

# 그래프가 그려질 위치를 정합니다.
plt.subplot(3, 1, 1)
# 그래프 위에 (x2D, y2Dx)위치에 크기는 100인 점을 찍습니다.
plt.scatter(x2D, y2Dx, s = 100)
# x축에 라벨을 붙여줍니다.
plt.xlabel("time", fontsize = 20)
# y축에 라벨을 붙여줍니다.
plt.ylabel("x", fontsize = 20)

# 그래프가 그려질 위치를 정합니다.
plt.subplot(3, 1, 2)
# 그래프 위에 (x2D, y2Dy)위치에 크기는 100인 점을 찍습니다.
plt.scatter(x2D, y2Dy, s = 100)
# x축에 라벨을 붙여줍니다.
plt.xlabel("time", fontsize = 20)
# y축에 라벨을 붙여줍니다.
plt.ylabel("y", fontsize = 20)

# 그래프가 그려질 위치를 정합니다.
plt.subplot(3, 1, 3)
# 그래프 위에 (x2D, y2Dz)위치에 크기는 100인 점을 찍습니다.
plt.scatter(x2D, y2Dz, s = 100)
# x축에 라벨을 붙여줍니다.
plt.xlabel("time", fontsize = 20)
# y축에 라벨을 붙여줍니다.
plt.ylabel("z", fontsize = 20)

# 그래프를 보여줍니다.
plt.show()

