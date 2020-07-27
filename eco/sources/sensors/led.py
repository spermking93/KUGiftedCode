# LED를 제어합니다.

import RPi.GPIO as GPIO
import time

# 빨, 주, 노, 초, 파, 남, 보
colors = [0xFF0000, 0xFF0023, 0xFF00FF, 0x0000FF, 0x00FF00, 0x64EB00, 0x4BFB00]
# R, G, B의 핀을 각각 19, 21, 20 으로 지정합니다.
pins = {'pin_R':19, 'pin_G':21, 'pin_B':20}

# GPIO 핀 모드를 BCM으로 설정합니다.
GPIO.setmode(GPIO.BCM)

# 각 핀을 출력으로 설정하고, HIGH로 설정해 LED를 끕니다.
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)
    GPIO.output(pins[i], GPIO.HIGH)

# PWM 제어를 위해 설정합니다.
p_R = GPIO.PWM(pins['pin_R'], 2000)  # 주파수 설정 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)
p_B = GPIO.PWM(pins['pin_B'], 2000)

# 초기 듀티 사이클 = 0 (LED 끄기)
p_R.start(0)
p_G.start(0)
p_B.start(0)

# 간단한 사칙연산을 하는 함수 map을 정의합니다.
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


# LED 색을 설정하는 함수
def setColor(col):   # 예)  col = 0x112233
    R_val = (col & 0x110000) >> 16
    G_val = (col & 0x001100) >> 8
    B_val = (col & 0x000011) >> 0

    # R_val, G_val, B_val의 값을 업데이트 합니다.
    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    # 듀티사이클을 변경합니다.
    p_R.ChangeDutyCycle(100-R_val)
    p_G.ChangeDutyCycle(100-G_val)
    p_B.ChangeDutyCycle(100-B_val)


# 아래의 코드를 시도합니다.
try:
    # while문 안의 코드를 반복합니다.
    while True:
        # 1초의 텀을 두고 다음 색상으로 넘어갑니다.
        for col in colors:
            setColor(col)
            time.sleep(1.0)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    p_R.stop()
    p_G.stop()
    p_B.stop()

    # 각 핀에 대해 LED 조명을 끕니다.
    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)
    # GPIO의 설정을 초기화합니다.
    GPIO.cleanup()
