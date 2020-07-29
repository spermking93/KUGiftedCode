import csv
import pandas as pd
import matplotlib.pyplot as plt

# pandas를 이용해서 csv파일을 읽어줍니다.
dfTilt = pd.read_csv("TiltTime.csv", index_col=0)

# dfTest의 data type을 출력합니다.
print(dfTilt.dtypes)
# dfTest를 출력합니다.
print(dfTilt)


dfT = dfTilt['t']
dfX = dfTilt['x']
dfY = dfTilt['y']
dfZ = dfTilt['z']


plt.subplot(3, 1, 1)
plt.scatter(dfT, dfX, label = "x")
plt.subplot(3, 1, 2)
plt.scatter(dfT, dfY, label = "y")
plt.subplot(3, 1, 3)
plt.scatter(dfT, dfZ, label = "z")
plt.legend()
plt.show()



