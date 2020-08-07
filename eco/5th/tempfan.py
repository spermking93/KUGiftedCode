# 온습도 센서로 온도 정보를 추출하고 온도에 따라 팬을 제어해봅니다.

import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.LOW)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.LOW)

time.sleep(1)

try:
    while True:
        h,t = dht.read_retry(dht.DHT22, 4)
        
        if t>= 25:
            print("Temp: {0:0.1f}*C FAN ON".format(t))
            GPIO.output(5, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(5, GPIO.LOW)
        
        time.sleep(1.0)

except KeyboardInterrupt:
    GPIO.cleanup()
