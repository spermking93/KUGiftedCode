# DHT22 센서를 이용해 습도 정보를 가져와봅니다.

import Adafruit_DHT as dht
import time

# 아래 코드를 시도합니다.
try:
    # while문 안에 있는 문장을 반복합니다.
    while True:
        # 센서를 통해 온습도 정보를 가져옵니다.
        h,t = dht.read_retry(dht.DHT22, 4)
        # 형식에 맞춰 습도 정보를 출력합니다.
        print( 'Humidity={0:0.1f}%'.format(h))
        # 1초간 텀을 줍니다.
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    print("done")
