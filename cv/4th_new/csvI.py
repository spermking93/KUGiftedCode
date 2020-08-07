#데이터를 csv파일로 저장해봅니다.
import numpy as np

data = list(range(100))
print(data)

#txt를 저장하는 함수(delimiter는 구분자, header는 문서첫줄에 들어갈 머리말, comments는 머리말에 처음 들어가는 단어 default는 '#'
np.savetxt("outTest.csv", data, delimiter=",",header="num",comments='')
