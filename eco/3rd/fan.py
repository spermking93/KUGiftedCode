# 팬을 제어합니다.

import RPi.GPIO as GPIO
import time

# GPIO의 핀 모드를 BCM으로 설정합니다.
GPIO.setmode(GPIO.BCM)

# GPIO의 5번, 6번 핀을 출력 핀으로 설정하고, LOW로 설정합니다.
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.LOW)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.LOW)

# 5번 핀을 HIGH로 설정해서 팬을 작동시킵니다.
GPIO.output(5, GPIO.HIGH)
# 5초 동안 유지합니다.
time.sleep(5)
# 5번 핀을 LOW로 설정해서 팬의 작동을 중지합니다.
GPIO.output(5, GPIO.LOW)

# GPIO 설정을 초기화 합니다.
GPIO.cleanup()
