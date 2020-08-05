# 현재 시간을 출력해봅니다.

import datetime
import time

# 아래 코드의 시행을 시도합니다.
try:
    # while문 안의 코드를 반복합니다.
    while True:
        # 현재 시간을 now에 저장합니다.
        now = datetime.datetime.now()

        # now에 저장한 현재 시간을 시, 분, 초의 형태로 nowTime에 저장합니다.
        nowTime = now.strftime('%H:%M:%S')

        # nowTime을 출력합니다.
        print(nowTime)

        # 1초간의 텀을 줍니다.
        time.sleep(1)

# 키보드 인터럽트가 발생하면 중지합니다.
except KeyboardInterrupt:
    # done을 출력합니다.
    print("done")
