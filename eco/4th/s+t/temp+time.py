import Adafruit_DHT as dht
import time

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')        
    print('time = {0:0.01f} emp={0:0.1f}*C '.format(nowTime , t))
    time.sleep(0.5)
