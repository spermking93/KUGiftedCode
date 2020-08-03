# 펌프를 제어합니다.

import RPi.GPIO as GPIO
import time

# GPIO의 핀 모드를 BCM으로 설정합니다.
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO의 23번, 24번 핀을 출력으로 설정하고 LOW로 설정합니다.
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, GPIO.LOW)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

# GPIO의 23번 핀을 HIGH로 설정하여 펌프를 작동시킵니다.
GPIO.output(23, GPIO.HIGH)
# 3초간 유지합니다.
time.sleep(3)
# GPIO의 23번 핀을 다시 LOW로 설정하여 펌프 작동을 중지합니다.
GPIO.output(23, GPIO.LOW)

# GPIO 핀의 설정을 초기화합니다.
GPIO.cleanup()
