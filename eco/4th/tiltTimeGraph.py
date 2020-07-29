# 기울기센서를 이용해서 기울기 정도를 측정합니다.

import time
import Adafruit_ADXL345
import csv

# 모듈을 읽어옵니다.
accel = Adafruit_ADXL345.ADXL345()

print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
fTiltT = open('TiltTime.csv', 'w', encoding='utf-8', newline='')


# 아래의 코드를 시도합니다.
try:
    # while문 안에 있는 코드를 계속 시행합니다.

    tlist = []
    xlist = []
    ylist = []
    zlist = []

    tOut = []
    xOut = []
    yOut = []
    zOut = []
    
    while True:
        # 센서를 통해 x, y, z축의 기울기 정도를 읽어옵니다.
        x, y, z = accel.read()
        now = datetime.datetime.now()
        nowTime = now.strftime('%H:%M:%S')        
        
        # 읽어온 기울기의 정도를 형식에 맞추어 출력합니다.
        print('X={0}, Y={1}, Z={2}, t{3}'.format(x, y, z, nowTime))
        
        write.writerow([nowTime, x, y, z])
        tlist.append(nowTime)
        xlist.append(x)
        ylist.append(y)
        zlist.append(z)

        # 1초의 텀을 줍니다.
        time.sleep(1.0)
        if len(timelist) == 100:
          tOut = len(tlist)
          xOut = xlist
          yOut = ylist
          zOut = zlist

          plt.subplot(3, 1, 1)
          plt.scatter(tlist, xlist, label = "x")
          plt.legend()

          plt.subplot(3, 1, 2)
          plt.scatter(tlist, ylist label = "y")
          

          plt.subplot(3, 1, 3)
          plt.scatter(tlist, zlist label = "z")

          plt.legend()
          plt.show()

          tlist = []
          xlist = []
          ylist = []    
          zlist = []
          
# 키 인터럽트가 발생하면 종료합니다.
except KeybordInterrupt:
    print("done")

# GPIO 핀 설정을 모두 초기화 해줍니다.
GPIO.cleanup()
