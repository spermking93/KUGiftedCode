# 조도센서를 이용해서 주변의 밝기를 측정하고 그에 따라 LED의 색을 바꿔봅니다.

import smbus
import time
import RPi.GPIO as GPIO

# GPIO의 핀 모드를 BCM으로 설정합니다.
GPIO.setmode(GPIO.BCM)

GPIO.setup(19,GPIO.OUT)     # R
GPIO.setup(20,GPIO.OUT)     # G
GPIO.setup(21,GPIO.OUT)     # B


# 사용할 i2c 채널 번호
I2C_CH = 1
# BH1750 주소
BH1750_DEV_ADDR = 0x23

# 조도의 측정 모드
# 값이 1lx 단위로 측정되며 샘플링 시간은 120ms이고 계속 측정하는 모드
CONT_H_RES_MODE     = 0x10
# 0.5lx 단위로 측정되며 샘플링 시간은 120ms이고 계속 측정하는 모드
CONT_H_RES_MODE2    = 0x11
# 4lx 단위로 측정되며 샘플링 시간은 16ms이고 계속 측정하는 모드
CONT_L_RES_MODE     = 0x13
# 아래 3가지 모드는 위와 비슷하지만, 한 번 측정하고 센서가 절전 모드로 진입합니다.
ONETIME_H_RES_MODE  = 0x20
ONETIME_H_RES_MODE2 = 0x21
ONETIME_L_RES_MODE  = 0x23

# 사용할 I2C 채널 라이브러리를 생성합니다.
i2c = smbus.SMBus(I2C_CH)

# 아래의 코드를 시도합니다.
try:
    # while문 안에 있는 코드를 계속 시행합니다.
    while True:
        # 측정모드를 CONT_H_RES_MODE 설정하여 2 바이트 읽어옵니다.
        luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE, 2)
        # 바이트 배열을 int로 변환합니다.
        lux = int.from_bytes(luxBytes, byteorder='big')
        # 출력합니다.
        print('{0} lux LED ON'.format(lux))

        # lux가 10 이하로 떨어지면 LED의 색상을 빨간색으로 설정합니다.
        if lux <= 10:
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(19, GPIO.LOW)

        # lux가 10보다 크고, 850이하라면 LED의 색상을 초록색으로 설정합니다.
        elif 10 < lux <= 850:
            GPIO.output(21, GPIO.HIGH)
            GPIO.output(20, GPIO.LOW)
            GPIO.output(19, GPIO.HIGH)

        # 위의 경우가 아닌 경우, 850보다 큰 경우 LED의 색상을 파란색으로 설정합니다.
        else:
            GPIO.output(21, GPIO.LOW)
            GPIO.output(20, GPIO.HIGH)
            GPIO.output(19, GPIO.HIGH)
        
        # 1초의 텀을 줍니다.
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    # GPIO 설정을 초기화합니다.
    GPIO.cleanup()

GPIO.cleanup()
