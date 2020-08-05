import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("tiltTime.csv", header=None)
x2D = df[0]
y2Dx = df[1]
y2Dy = df[2]
y2Dz = df[3]

plt.figure(figsize=(30, 15))

plt.subplot(3, 1, 1)
plt.scatter(x2D, y2Dx, s = 100)
plt.xlabel("time", fontsize = 20)
plt.ylabel("x", fontsize = 20)

plt.subplot(3, 1, 2)
plt.scatter(x2D, y2Dy, s = 100)
plt.xlabel("time", fontsize = 20)
plt.ylabel("y", fontsize = 20)

plt.subplot(3, 1, 3)
plt.scatter(x2D, y2Dz, s = 100)
plt.xlabel("time", fontsize = 20)
plt.ylabel("z", fontsize = 20)

plt.show()

