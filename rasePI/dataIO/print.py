# 10개의 숫자를 터미널에 출력해봅니다.

import random


# genRan이라는 함수를 정의합니다.
def genRan(inN, inRmin, inRmax):
    # inN번 만큼 inRmin과 inRmax 사이에 있는 값 중 하나를 선택합니다.
    outRanL = [random.randint(inRmin,inRmax) for i in range(inN)]
    
    # outRanL을 반환합니다.
    return outRanL


# genRan함수를 호출해서 testRan라는 list에 선택된 숫자를 넣습니다.
testRan = genRan(10, 1, 100)

# testRan안에 있는 숫자를 하나씩 출력합니다.
for i in range(10):
    print(testRan[i])
