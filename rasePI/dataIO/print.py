# 10개의 숫자를 터미널에 출력해봅니다.
import random


# genRan함수를 정의합니다.
def genRan(inN, inRmin, inRmax):
    # inN만큼 for문을 반복하면서 inRmin과 inRmax 사이에 있는 값을 고릅니다.
    outRanL = [random.randint(inRmin,inRmax) for i in range(inN)]
    
    # outRanL을 반환합니다.
    return outRanL


# genRan함수를 호출해서 반환값을 genRan에 저장합니다.
testRan = genRan(10, 1, 100)

# testRan안에 있는 숫자를 하나씩 출력합니다.
for i in range(10):
    print(testRan[i])
