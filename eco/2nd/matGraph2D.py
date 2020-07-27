# 주어진 csv파일을 읽어서 2차원 그래프를 그려봅니다.
import matplotlib.pyplot as plt
import pandas as pd


# plot2D 함수를 정의합니다.
def plot2D(xData, yData):
    # 그래프가 그려질 크기를 정합니다.
    plt.figure(figsize=(5, 5))

    # 그래프의 색상, 데이터, 점의 크기 등을 정하고 그래프를 그립니다.
    plt.scatter(xData, yData, c='blue', alpha=0.2)

    # x축에 label을 달아줍니다.
    plt.xlabel('x')

    # y축에 label을 달아줍니다.
    plt.ylabel('y')

    # 그래프를 보입니다.
    plt.show()


# csv파일을 읽어옵니다.
df = pd.read_csv("output2D.csv")

# x 데이터를 가져옵니다.
x2D = df['x']

# y 데이터를 가져옵니다.
y2D = df['y']

# df의 데이터 타입을 출력합니다.
print(df.dtypes)

# plot2D 함수를 호출하여 그래프를 보입니다.
plot2D(x2D, y2D)
