# dht22 센서를 이용해서 온도 정보를 알아봅니다.

import Adafruit_DHT as dht
import time

# 아래 문장을 시도합니다.
try:
    # while문 안의 코드를 반복합니다.
    while True:
        # 센서로부터 온습도 정보를 가져옵니다.
        h,t = dht.read_retry(dht.DHT22, 4)
        # 형식에 맞춰 온도 정보를 출력합니다.
        print( 'Temp={0:0.1f}*C '.format(t))
        # 1초간의 텀을 줍니다.
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    print("done")
