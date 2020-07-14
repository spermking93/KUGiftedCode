# 주어진 데이터로 3D 그래프를 그려봅니다.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# calData 함수를 정의합니다.
def calData(inData,w,b):
    # inData에 w를 곱하고, b를 더해줍니다.
    outData = w * inData + b

    # outData를 반환합니다.
    return outData


# conDf 함수를 정의합니다.
def conDf(xData, yData, zData):
    # xData, yData, zData를 형식에 맞게 dfOut에 저장합니다.
    dfOut = pd.DataFrame({"x":xData, "y":yData, "z":zData})

    # dfOut을 반환합니다.
    return dfOut


# plot3D 함수를 정의합니다.
def plot3D(xIn, yIn, zIn):
    # figure을 생성합니다.
    fig = plt.figure()

    # 그래프가 그려질 위치와 차원을 정합니다.
    ax = fig.add_subplot(111, projection='3d')

    # xIn, yIn, zIn을 x, y, z값으로 하는 그래프를 그립니다.
    ax.scatter(xIn,yIn,zIn )

    # 그래프를 보여줍니다.
    plt.show()


# inCal에 0부터 99까지의 값을 넣어줍니다.
inCal = np.array(range(100))

# xIn에 inCal의 값을 넣어줍니다.
xIn = inCal

# calData를 호출해서 반환값을 yIn에 저장합니다.
yIn = calData( xIn , 10. , 10. )

# calData를 호출해서 반환값을 zIn에 저장합니다.
zIn = calData( xIn, 20. ,30. )

# conDf를 호출해서 반환값을 dfTest에 저장합니다.
dfTest = conDf(xIn, yIn, zIn)

# dfTest를 호출합니다.
print(dfTest)


# dfTest에서 x, y, z값을 추출합니다.
x3D = dfTest['x']
y3D = dfTest['y']
z3D = dfTest['z']

# 추출한 x, y, z 값을 출력합니다.
print(x3D, y3D, z3D)

# plot3D 함수를 호출해서 그래프를 그립니다.
plot3D(x3D, y3D, z3D)

