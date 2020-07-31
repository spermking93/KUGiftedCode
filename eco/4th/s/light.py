# 조도센서를 이용해서 주변 환경의 밝기를 측정합니다.

import smbus   # i2c 라이브러리
import time

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

time.sleep(1)

# 아래의 코드를 시도합니다.
try:
    # while문 안에 있는 코드를 계속 시행합니다.
    while True:
        # 측정모드를 CONT_H_RES_MODE 설정하여 2 바이트 읽어옵니다.
        luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE, 2)
        # 바이트 배열을 int로 변환합니다.
        lux = int.from_bytes(luxBytes, byteorder='big')
        # 출력합니다.
        print('{0} lux'.format(lux))
        # 1초의 텀을 줍니다.
        time.sleep(1)

# 키 인터럽트가 발생하면 종료합니다.
except KeyboardInterrupt:
    print("done")
