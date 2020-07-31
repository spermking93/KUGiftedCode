import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("tiltTime.csv", header=None)
x2D = df[0]
y2Dx = df[1]
y2Dy = df[2]
y2Dz = df[3]

plt.subplot(3, 1, 1)
plt.scatter(x2D, y2Dx)
plt.xlabel("time")
plt.ylabel("x")

plt.subplot(3, 1, 2)
plt.scatter(x2D, y2Dy)
plt.xlabel("time")
plt.ylabel("y")

plt.subplot(3, 1, 3)
plt.scatter(x2D, y2Dz, label = "z")
plt.xlabel("time")
plt.ylabel("z")

plt.show()

