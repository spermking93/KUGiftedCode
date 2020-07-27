import modules_nk
import RPi.GPIO as GPIO
import datetime
import time
import spidev
import Adafruit_DHT as dht

step = 10

# 시간에 대한 리스트
timelist = []
# 습도에 대한 리스트
humilist = []
# 온도에 대한 리스트
templist = []

i = 0
# i가 step값 보다 작은 범위 한에서 아래 과정을 반복합니다. 
while i < step:
     # 센서값을 읽어서 저장합니다.
     h,t = dht.read_retry(dht.DHT22, 4)

     # 현재 시각에 대한 값을 저장합니다.  
     now = datetime.datetime.now()

     # 시각을 시,분,초로 나타냅니다. 
     nowTime = now.strftime('%H:%M:%S')
        
     # 시,분,초로 나타낸 현재 시각을 출력합니다.
     print(nowTime)
        
     # 온도 습도를  형식에 맞게 값을 출력합니다..
     print('Temp={0:0.01f}*C Humidity={1:0.01f}%'.format(t, h))
    
     # i를 시간의 리스트 값으로 추가합니다.
     timelist.append(i)
        
     # 측정된 습도값을 리스트값에 추가합니다.
     humilist.append(h)
        
     # 측정된 온도값을 리스트값에 추가합니다.
     templist.append(t)
        
     # 실제 시간간격을 0.01초로 설정합니다.
     time.sleep(.01)
        
     # i에다 1을 더한다. 즉 step값 보다 작은 범위안에서 위의 과정을 반복합니다.
     i = i + 1

timeNext = 1.

W_h, b_h = modules_nk.LinearRegression( step , 0.001, humilist, timelist )
W_t, b_t = modules_nk.LinearRegression( step , 0.001, templist, timelist )

print(W_h,b_h)
hum = W_h * timeNext + b_h
print(hum)

print(W_t,b_t)
temp = W_t * timeNext + b_t 
print(temp)

w1 = 23        # 펌프
w2 = 24

w3 = 5         # 팬
w4 = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(w1,GPIO.OUT)
GPIO.output(w1,GPIO.LOW)
GPIO.setup(w2,GPIO.OUT)
GPIO.output(w2,GPIO.LOW)

GPIO.setup(w3,GPIO.OUT)
GPIO.output(w3,GPIO.LOW)
GPIO.setup(w4,GPIO.OUT)
GPIO.output(w4,GPIO.LOW)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000000


if (60. > hum) :
     GPIO.output(w1,GPIO.HIGH)
     GPIO.output(w2,GPIO.LOW)
else :
     GPIO.output(w1,GPIO.LOW)
     GPIO.output(w2,GPIO.LOW)
time.sleep(0.5)


if (25. < temp) :
     GPIO.output(w3,GPIO.HIGH)
     GPIO.output(w4,GPIO.LOW)
else :
     GPIO.output(w3,GPIO.LOW)
     GPIO.output(w4,GPIO.LOW)
time.sleep(5.0)


GPIO.cleanup()
spi.close()                 
