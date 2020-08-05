# 저장한 csv 파일을 이용해서 x, y, z 축의 값을 각각 x, y, z 기울기로 하는 3D 그래프를 그려봅니다.

import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# # humtempTime.csv 파일을 읽어서 데이터 프레임 형식으로 df에 저장합니다.
df = pd.read_csv("tiltTime.csv", header=None)
print(df[0])

# 각 군집별로 색깔을 다르게 하기 위해 범위를 나눠줍니다. 
df1 = df[(df[2] > -100) & (df[2] < 100) & (df[3] > 100) ]

df2 = df[(df[2] > 100) & (df[3] > -200) & (df[3] < 100) ]

df3 = df[(df[2] > -100) & (df[2] < 100) & (df[3] < -200) ]
        
df4 = df[(df[2] < -100) & (df[3] > -200) & (df[3] < 100) ]


# 그래프 크기를 정합니다.
fig = plt.figure(figsize = (10,10))
# 3D 그래프를 그리기 위해 설정합니다.
ax = fig.add_subplot(111, projection='3d')

# x, y, z축에 라벨을 달아줍니다.
ax.set_xlabel('x', fontsize = 20)
ax.set_ylabel('y', fontsize = 20)
ax.set_zlabel('z', fontsize = 20)

# 그래프 위의 (df1[1], df1[2], df1[3]) 위치에 크기가 200인 점을 찍습니다.
ax.scatter(df1[1], df1[2], df1[3], color = 'red',   s=200)
# 그래프 위의 (df2[1], df2[2], df2[3]) 위치에 크기가 200인 점을 찍습니다.
ax.scatter(df2[1], df2[2], df2[3], color = 'blue',  s=200)
# 그래프 위의 (df3[1], df3[2], df3[3]) 위치에 크기가 200인 점을 찍습니다.
ax.scatter(df3[1], df3[2], df3[3], color = 'green', s=200)
# 그래프 위의 (df4[1], df4[2], df4[3]) 위치에 크기가 200인 점을 찍습니다.
ax.scatter(df4[1], df4[2], df4[3], color = 'purple',s=200)

plt.show()


