#데이터를 csv파일로 저장해봅니다.
import numpy as np

data = list(range(100))
print(data)

np.savetxt("outTest.csv", data, delimiter=",",header="num",comments='')