# 기울기센서를 이용해서 기울기 정도를 측정하고 시간과 함께 csv 파일에 저장합니다.

import datetime
import time
import Adafruit_ADXL345
import csv

# 모듈을 읽어옵니다.
accel = Adafruit_ADXL345.ADXL345()

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')

# tiltTime.csv 파일을 쓰기모드로 열어줍니다.
fTiltT = open('tiltTime.csv', 'w', encoding='utf-8', newline='')
# csv 파일에 쓰기 위한 객체를 만들어줍니다.
wr = csv.writer(fTiltT)
# 1초의 텀을 줍니다.
time.sleep(1)

# 아래의 코드를 시도합니다.
try:
    # while문 안에 있는 코드를 계속 시행합니다.
    while True:
        # 센서를 통해 x, y, z축의 기울기 정도를 읽어옵니다.
        x, y, z = accel.read()

        # 현재 시간을 알아와서 now에 저장합니다.
        now = datetime.datetime.now()      
        # now에 저장한 현재 시간을 시, 분, 초의 형태로 nowTime에 저장합니다.
        nowTime = now.strftime('%H:%M:%S')        
        
        # 읽어온 기울기의 정도를 형식에 맞추어 출력합니다.
        print('time={3} X={0}, Y={1}, Z={2}'.format(x, y, z, nowTime))
        # 형식에 맞춰 csv 파일에 작성합니다.
        wr.writerow([nowTime, x, y, z])

        # 1초의 텀을 줍니다.
        time.sleep(1)
       
# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    print("done")
