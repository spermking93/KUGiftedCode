# 100개의 숫자와 간단히 계산한 결과를 출력해봅니다.
# list 생성을 위한 패키지 입니다.
import numpy as np


# calData라는 함수를 정의합니다.
def calData(inData,w,b):
    # inData에 w를 곱해주고, b를 더해서 outData에 저장합니다.
    outData = w * inData + b

    # outData를 반환합니다.
    return outData


# inCal에 0부터 99까지 숫자를 저장합니다.
inCal = np.array(range(100))

# inCal을 출력합니다.
print(inCal)

# calData를 호출해서 결과값을 testCal에 저장합니다.
testCal = calData( inCal , 10. , 10. )

# testCal을 출력합니다.
print(testCal)
