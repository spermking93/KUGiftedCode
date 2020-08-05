import matplotlib.pyplot as plt
import pandas as pd

def plot2D(xData, yData, lab):
    plt.figure(figsize=(30, 10))
    plt.scatter(xData, yData, c='red', s = 100)
    plt.xlabel('time', fontsize = 20)
    plt.ylabel(lab, fontsize = 20)
    plt.show()

df = pd.read_csv("humtempTime.csv", header=None)
x2D = df[0]
y2D = df[1]

plot2D(x2D, y2D, 'hum')

y2D = df[2]
plot2D(x2D, y2D, 'temp')
