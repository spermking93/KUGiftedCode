# 서보모터를 제어해봅니다.
import RPi.GPIO as GPIO
import time
 
# 서보모터를 GPIO 18에 연결합니다.
pin = 18
 
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
        p.ChangeDutyCycle(1)
        print("angle : 1")
        time.sleep(1)
        p.ChangeDutyCycle(5)
        print("angle : 5")
        time.sleep(1)
        p.ChangeDutyCycle(8)
        print("angle : 8")
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    p.stop()
    # GPIO 설정을 초기화 합니다.
    GPIO.cleanup()
