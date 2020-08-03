# 팬과 펌프 그리고 LED를 제어해봅니다.

import RPi.GPIO as GPIO
import time

# 팬의 핀을 5번, 6번 핀으로 설정하고 펌프의 핀을 23번, 24번으로 설정합니다.
pins = {'pan1':5, 'pan2':6, 'pump1':23, 'pump2':24}
# R, G, B의 핀을 각각 19, 21, 20으로 설정합니다.
led = {'r':19, 'g':21, 'b':20}

# GPIO 핀 모드를 BCM으로 설정합니다.
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

# 팬과 펌프의 핀을 출력으로 설정하고, LOW로 지정합니다.
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)
    GPIO.output(pins[i], GPIO.LOW)

# R, G, B의 핀을 출력으로 설정하고 HIGH로 지정하여 LED를 끕니다.
for j in led:
    GPIO.setup(led[j], GPIO.OUT)
    GPIO.output(led[j], GPIO.HIGH)
    
# 다음 코드를 시도합니다.
try:
    # while문 안의 코드를 반복합니다.
    while True:
        # 팬의 핀 중 하나를 HIGH로 지정해서 팬이 작동하게 합니다.
        GPIO.output(pins['pan1'], GPIO.HIGH)
        # 펌프의 핀 중 하나를 HIGH로 지정해서 펌프가 작동하게 합니다.
        GPIO.output(pins['pump1'], GPIO.HIGH)
        
        # R, G의 핀을 HIGH로 설정하고 B를 LOW로 설정하여 LED에서 파란색 빛이 나게 합니다.
        GPIO.output(led['r'], GPIO.HIGH)
        GPIO.output(led['g'], GPIO.HIGH)
        GPIO.output(led['b'], GPIO.LOW)
        
        # 1초간의 텀을 줍니다.
        time.sleep(1)
        
        # 위에서 HIGH로 지정했던 팬의 핀을 다시 LOW로 지정하여 팬이 작동을 멈추게 합니다.
        GPIO.output(pins['pan1'], GPIO.LOW)
        # 위에서 HIGH로 지정했던 펌프의 핀을 다시 LOW로 지정하여 펌프가 작동을 멈추게 합니다.
        GPIO.output(pins['pump1'], GPIO.LOW)

        # R의 핀을 LOW로 하고, G와 B의 핀을 HIGH로 설정하여 LED가 빨간색 빛을 내게 합니다.
        GPIO.output(led['r'], GPIO.LOW)
        GPIO.output(led['g'], GPIO.HIGH)
        GPIO.output(led['b'], GPIO.HIGH)
        
        # 0.5초간의 텀을 줍니다.
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
