# 주어진 csv파일을 읽어서 2차원 그래프를 그려봅니다.
import matplotlib.pyplot as plt
import pandas as pd

def plotEmo(emotions):
    # 그래프가 그려질 크기를 정합니다.
    plt.figure(figsize=(5, 5))

    # 그래프의 색상, 데이터, 점의 크기 등을 정하고 그래프를 그립니다.
    plt.plot(emotions)

    #그래프에 제목을 붙여줍니다.
    plt.title('Angry')
    
    # x축에 label을 달아줍니다.
    plt.xlabel('time')

    # y축에 label을 달아줍니다.
    plt.ylabel('probability')

    # 그래프를 보입니다.
    plt.show()

# csv파일을 읽어옵니다.
df = pd.read_csv("emotion.csv") 

# 시간에 따른 감정값을 가져옵니다(y축)
emotions = df['Angry']

# df의 데이터 타입을 출력합니다.
print(df.dtypes)

# plot2D 함수를 호출하여 그래프를 보입니다.
plotEmo(emotions)