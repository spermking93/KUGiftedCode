import matplotlib.pyplot as plt
import pandas as pd

def plot2D(xData, yData, i):
    plt.figure(figsize=(30, 10))
    plt.scatter(xData, yData, c ='red', s = 100)
    plt.xlabel("time", fontsize = 20)
    plt.ylabel(i, fontsize = 20)
    plt.show()

df = pd.read_csv("tiltTime.csv", header=None)
x2D = df[0]
y2D = df[1]
plot2D(x2D, y2D,'x')

y2D = df[2]
plot2D(x2D, y2D, 'y')

y2D = df[3]
plot2D(x2D, y2D, 'z')

