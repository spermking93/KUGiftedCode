import csv
import pandas as pd
import matplotlib.pyplot as plt

# pandas를 이용해서 csv파일을 읽어줍니다.
dfTempHum = pd.read_csv("humTempTime.csv", index_col=0)

# dfTest의 data type을 출력합니다.
print(dfTempHum.dtypes)
# dfTest를 출력합니다.
print(dfTempHum)


dfT = dfTempHum['nowTime']
dfTemp = dfTempHum['t']
dfHum = dfTempHum['h']


plt.subplot(2, 1, 1)
plt.scatter(dfT, dfTemp, label = "temp")
plt.subplot(2, 1, 2)
plt.scatter(dfT, dfHum, label = "hum")
plt.legend()
plt.show()



