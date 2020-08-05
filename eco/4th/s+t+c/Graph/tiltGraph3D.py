import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

df = pd.read_csv("tiltTime.csv", header=None)
print(df[0])

df1 = df[(df[2] > -100) & (df[2] < 100) & (df[3] > 100) ]

df2 = df[(df[2] > 100) & (df[3] > -200) & (df[3] < 100) ]

df3 = df[(df[2] > -100) & (df[2] < 100) & (df[3] < -200) ]
        
df4 = df[(df[2] < -100) & (df[3] > -200) & (df[3] < 100) ]


fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('x', fontsize = 20)
ax.set_ylabel('y', fontsize = 20)
ax.set_zlabel('z', fontsize = 20)

#ax.scatter(df[1], df[2], df[3])
ax.scatter(df1[1], df1[2], df1[3], color = 'red',   s=200)
ax.scatter(df2[1], df2[2], df2[3], color = 'blue',  s=200)
ax.scatter(df3[1], df3[2], df3[3], color = 'green', s=200)
ax.scatter(df4[1], df4[2], df4[3], color = 'purple',s=200)

plt.show()


