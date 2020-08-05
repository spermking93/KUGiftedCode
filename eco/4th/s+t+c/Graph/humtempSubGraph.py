import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("humtempTime.csv", header=None)
x2D = df[0]
y2Dhum = df[1]
y2Dtemp = df[2]

plt.figure(figsize=(30, 10))

plt.subplot(1, 2, 1)
plt.scatter(x2D, y2Dhum, s = 100)
plt.xlabel("time", fontsize = 20)
plt.ylabel("hum", fontsize = 20)

plt.subplot(1, 2, 2)
plt.scatter(x2D, y2Dtemp, s = 100)
plt.xlabel("time", fontsize = 20)
plt.ylabel("temp", fontsize = 20)


plt.show()


