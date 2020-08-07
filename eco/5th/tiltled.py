# 기울기 센서를 통해 기울기를 측정하고, 기울기에 따라 LED를 제어해봅니다.

import Adafruit_ADXL345
import time
import RPi.GPIO as GPIO

accel = Adafruit_ADXL345.ADXL345()

GPIO.setmode(GPIO.BCM)

GPIO.setup(19,GPIO.OUT)     # R
GPIO.output(19, GPIO.HIGH)
GPIO.setup(20,GPIO.OUT)     # G
GPIO.output(20, GPIO.HIGH)
GPIO.setup(21,GPIO.OUT)     # B
GPIO.output(21, GPIO.HIGH)

time.sleep(1)

initx, inity, initz = accel.read()
print("initial x, y, z: {0}, {1}, {2}".format(initx, inity, initz))

time.sleep(3)       # 3초 쉬고

try:
    while True:
        x, y, z = accel.read()
        subx = abs(x - initx)
        suby = abs(y - inity)
        subz = abs(z - initz)        # x, y, z 기울기 차이 구하기 (절댓값)

        '''
        이 코드 처음 실행했을 때와 비교해서 x, y, z 중 어디로 가장 치우쳤는지!
        기준은 가장 처음 코드를 실행했을 때의 기울기.
        x쪽으로 가장 치우쳤으면 빨간색, y쪽으로 가장 치우쳤으면 초록색, z축으로 가장 치우쳤으면 파란색
        '''

        if max(subx, suby, subz) == subx:
            print("x, y, z: {0}, {1}, {2} RED LED ON".format(x, y, z))
            GPIO.output(19, GPIO.LOW)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.HIGH)
        elif max(subx, suby, subz) == suby:
            print("x, y, z: {0}, {1}, {2} GREEN LED ON".format(x, y, z))
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(20, GPIO.LOW)
            GPIO.output(21, GPIO.HIGH)
        else:
            print("x, y, z: {0}, {1}, {2} BLUE LED ON".format(x, y, z))
            GPIO.output(19, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(21, GPIO.LOW)

        time.sleep(1)
        

except KeyboardInterrupt:
    GPIO.cleanup()
