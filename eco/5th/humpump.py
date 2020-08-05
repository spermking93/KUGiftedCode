# 온습도 센서를 이용해 습도 정보를 알아내고, 습도에 따라 펌프를 제어해봅니다.

import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

# 아래 코드를 시도합니다.
try:
    # while문 안에 있는 문장을 반복합니다.
    while True:
        # 센서를 통해 온습도 정보를 가져옵니다.
        h,t = dht.read_retry(dht.DHT22, 4)
        
        if h < 70:
            print("pump on")
            # GPIO의 23번 핀을 HIGH로 설정하여 펌프를 작동시킵니다.
            GPIO.output(23, GPIO.HIGH)
            # 3초간 유지합니다.
            time.sleep(3)
            # GPIO의 23번 핀을 다시 LOW로 설정하여 펌프 작동을 중지합니다.
            GPIO.output(23, GPIO.LOW)

        # 1초간 텀을 줍니다.
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    GPIO.cleanup()