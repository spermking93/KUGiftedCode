import Adafruit_DHT as dht
import datetime
import time

time.sleep()

try:
    while True:
        h,t = dht.read_retry(dht.DHT22, 4)
        now = datetime.datetime.now()
        nowTime = now.strftime('%H:%M:%S')        
        print('time={0} temp={1:0.1f}*C '.format(nowTime , t))
        time.sleep(0.5)

except KeyboardInterrupt:
    print("done")
