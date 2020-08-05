# 센서를 이용해서 온습도를 측정하고, 측정한 정보를 측정 시각과 함께 csv 파일로 저장해봅니다.

import Adafruit_DHT as dht
import time
import datetime
import csv

# humtempTime.csv 파일을 쓰기 모드로 열어줍니다.
fHumT = open('humtempTime.csv', 'w', encoding='utf-8', newline='')
# csv 파일에 쓰기 위한 객체를 만들어줍니다.
wr = csv.writer(fHumT)

# 1초간의 텀을 줍니다.
time.sleep(1)

# 아래의 코드를 시도합니다.
try:
    # while문 안에 있는 코드를 반복합니다.
    while True:
        # DHT22 센서를 통해 온습도 정보를 받아옵니다.
        h,t = dht.read_retry(dht.DHT22, 4)

        # 현재 시간을 now에 저장합니다.
        now = datetime.datetime.now()
        # now에 저장한 현재 시간을 시, 분, 초의 형태로 nowTime에 저장합니다.
        nowTime = now.strftime('%H:%M:%S')
        
        # 형식에 맞게 시간과 습도, 온도를 출력합니다.
        print('time={0} Humidity={1:0.1f}% Temp={1:0.1f}*C '.format(nowTime , h, t))
        # 형식에 맞게 시간과 습도, 온도를 csv 파일에 작성합니다.
        wr.writerow([nowTime, h, t])

        # 1초간의 텀을 줍니다.
        time.sleep(1)

# 키보드 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    print("done")

