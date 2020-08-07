# 온습도 센서를 이용해 온습도 정보를 알아내고, 그에 따라 펌프와 팬을 제어해봅니다.

import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)        # pump
GPIO.output(23, GPIO.LOW)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

GPIO.setup(5, GPIO.OUT)         # fan
GPIO.output(5, GPIO.LOW)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.LOW)

time.sleep(1)

# 아래 코드를 시도합니다.
try:
    # while문 안에 있는 문장을 반복합니다.
    while True:
        # 센서를 통해 온습도 정보를 가져옵니다.
        h,t = dht.read_retry(dht.DHT22, 4)
        
        if h < 70:
            print("Hum: {0:0.1f}% PUMP ON".format(h))
            GPIO.output(23, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(23, GPIO.LOW)
        
        if t>= 25:
            print("Temp: {0:0.1f}*C FAN ON".format(t))
            GPIO.output(5, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(5, GPIO.LOW)

        # 1초간 텀을 줍니다.
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    GPIO.cleanup()
