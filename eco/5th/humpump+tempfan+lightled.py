# 온습도 센서를 이용해 온습도 정보를 알아내고, 조도센서로 밝기 정보를 알아냅니다.
# 그에 따라 펌프와 팬 그리고 LED를 제어해봅니다.

import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time
import smbus

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)        # pump
GPIO.output(23, GPIO.LOW)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)

GPIO.setup(5, GPIO.OUT)         # fan
GPIO.output(5, GPIO.LOW)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.LOW)

GPIO.setup(19,GPIO.OUT)     # R
GPIO.setup(20,GPIO.OUT)     # G
GPIO.setup(21,GPIO.OUT)     # B

for i in range(3):
    GPIO.output(19+i, GPIO.HIGH)

# 사용할 i2c 채널 번호
I2C_CH = 1
# BH1750 주소
BH1750_DEV_ADDR = 0x23
# 사용할 I2C 채널 라이브러리를 생성합니다.
i2c = smbus.SMBus(I2C_CH)
# 조도의 측정 모드
CONT_H_RES_MODE     = 0x10

time.sleep(1)

# 아래 코드를 시도합니다.
try:
    # while문 안에 있는 문장을 반복합니다.
    while True:
        # 센서를 통해 온습도 정보를 가져옵니다.
        # 측정모드를 CONT_H_RES_MODE 설정하여 2 바이트 읽어옵니다.
        luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE, 2)
        # 바이트 배열을 int로 변환합니다.
        lux = int.from_bytes(luxBytes, byteorder='big')

        h,t = dht.read_retry(dht.DHT22, 4)
        
        '''습도값에 따라서 펌프 제어'''
        if h < 70:
            print("Hum: {0:0.1f}% PUMP ON".format(h))
            GPIO.output(23, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(23, GPIO.LOW)
        
        '''온도값에 따라서 팬 제어'''
        if t>= 25:
            print("Temp: {0:0.1f}*C FAN ON".format(t))
            GPIO.output(5, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(5, GPIO.LOW)

        '''조도값에 따라서 LED 제어'''
        # lux가 10 이하로 떨어지면 LED의 색상을 빨간색으로 설정합니다.
        if lux <= 10:
            print('{0}lux RED LED ON'.format(lux))
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)

        # lux가 10보다 크고, 850이하라면 LED의 색상을 초록색으로 설정합니다.
        elif 10 < lux <= 850:
            print('{0}lux GREEN LED ON'.format(lux))
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)

        # 위의 경우가 아닌 경우, 850보다 큰 경우 LED의 색상을 파란색으로 설정합니다.
        else:
            print('{0}lux BLUE LED ON'.format(lux))
            GPIO.output(21, GPIO.LOW)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)

        # 1초간 텀을 줍니다.
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    GPIO.cleanup()
