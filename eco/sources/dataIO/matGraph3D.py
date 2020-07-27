# csv파일을 읽어서 3차원 그래프를 그려봅니다.
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd


# plot3D 함수를 정의합니다.
def plot3D(xIn, yIn, zIn):
    # 그래프 객체를 생성합니다.
    fig = plt.figure()

    # 3D축을 fig에 추가합니다.
    ax = fig.add_subplot(111, projection='3d')

    # x, y, z 축에 label을 달아줍니다.
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # x, y, z 데이터를 xIn, yIn, zIn으로 설정하고 그래프를 그립니다.
    ax.scatter(xIn,yIn,zIn )

    # 그래프를 보여줍니다.
    plt.show()


# csv파일을 읽어옵니다.
dfTest = pd.read_csv("output3D.csv")

# dfTest의 데이터 타입을 출력합니다.
print(dfTest.dtypes)

# plot3D 함수를 호출해서 그래프를 보입니다.
plot3D(dfTest['x'], dfTest['y'], dfTest['z'])
