import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plot3D(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    ax.scatter(x, y, z)

    plt.show()

df = pd.read_csv("tiltTime.csv", header=None)
print(df[0])

df1 = df[(df[2] > -100) & (df[2] < 100) & (df[3] > 200) ]

df2 = df[(df[2] > 100) & (df[3] > -100) & (df[3] < 200) ]

df3 = df[(df[2] > -100) & (df[2] < 100) & (df[3] < -100) ]
        
df4 = df[(df[2] < -200) & (df[3] > -100) & (df[3] < 200) ]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.scatter(df1[1], df1[2], df1[3])
ax.scatter(df2[1], df2[2], df2[3])
ax.scatter(df3[1], df3[2], df3[3])
ax.scatter(df4[1], df4[2], df4[3])

plt.show()


