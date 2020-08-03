import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("humtempTime.csv", header=None)
x2D = df[0]
y2Dhum = df[1]
y2Dtemp = df[2]

plt.subplot(1, 2, 1)
plt.scatter(x2D, y2Dhum)
plt.xlabel("time")
plt.ylabel("hum")

plt.subplot(1, 2, 2)
plt.scatter(x2D, y2Dtemp)
plt.xlabel("time")
plt.ylabel("temp")


plt.show()


