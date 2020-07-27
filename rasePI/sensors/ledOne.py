# LED를 제어합니다.

import RPi.GPIO as GPIO
import time

# R, G, B의 핀을 각각 19, 21, 20 으로 지정합니다.
pins = {'pin_R':19, 'pin_G':21, 'pin_B':20}

# GPIO 핀 모드를 BCM으로 설정합니다.
GPIO.setmode(GPIO.BCM)

# 각 핀을 출력으로 설정하고, HIGH로 설정해 LED를 끕니다.
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)
    GPIO.output(pins[i], GPIO.HIGH)

# 아래의 코드를 시도합니다.
try:
    # while문 안의 코드를 반복합니다.
    while True:
        # 초록색 LED를 킵니다.
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.LOW)

        # 1초 동안 텀을 줍니다.
        time.sleep(1.0)
        
        # 파란색 LED를 킵니다.
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(20, GPIO.LOW)
        GPIO.output(21, GPIO.HIGH)

        # 1초 동안 텀을 줍니다.
        time.sleep(1.0)

        # 빨간색 LED를 킵니다.
        GPIO.output(19, GPIO.LOW)
        GPIO.output(20, GPIO.HIGH)
        GPIO.output(21, GPIO.HIGH)

        # 1초 동안 텀을 줍니다.
        time.sleep(1.0)
        

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    # 각 핀에 대해 LED 조명을 끕니다.
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)
    # GPIO의 설정을 초기화합니다.
    GPIO.cleanup()
