import matplotlib.pyplot as plt
import pandas as pd

def plot2D(xData, yData, lab):
    plt.figure(figsize=(5, 5))
    plt.scatter(xData, yData, c='red')
    plt.xlabel('time')
    plt.ylabel(lab)
    plt.show()

df = pd.read_csv("humtempTime.csv", header=None)
x2D = df[0]
y2D = df[1]

plot2D(x2D, y2D, 'hum')

y2D = df[2]
plot2D(x2D, y2D, 'temp')
