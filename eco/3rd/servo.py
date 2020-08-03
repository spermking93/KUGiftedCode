# 서보모터를 제어해봅니다.

import RPi.GPIO as GPIO
import time
 
# 서보모터를 GPIO 13에 연결합니다.
pin = 13
 
# GPIO의 핀 모드를 BCM으로 설정합니다. 
GPIO.setmode(GPIO.BCM)

# 핀을 출력으로 설정합니다.
GPIO.setup(pin, GPIO.OUT)

# PWM 제어를 위해 설정해줍니다.
p = GPIO.PWM(pin, 50)
p.start(0)

# 아래의 코드를 시도합니다.
try:
    # while문 안에 있는 코드를 계속 반복합니다.
    while True:
        # PWM 제어를 통해 서보모터를 제어합니다.
        # 서보모터에 대한 ChagneDutyCycle 함수는 5~10까지만 값으로 받으며 0도에서 90도 범위에서 움직입니다.
        p.ChangeDutyCycle(5)
        print("angle : 0")
        time.sleep(1)
        p.ChangeDutyCycle(10)
        print("angle : 90")
        time.sleep(1)
       

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    p.stop()
    # GPIO 설정을 초기화 합니다.
    GPIO.cleanup()
