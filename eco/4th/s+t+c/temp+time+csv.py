import Adafruit_DHT as dht
import time
import datetime
import csv

fTempT = open('tempTime.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(fTempT)
time.sleep(1)

try:
    while True:
        h,t = dht.read_retry(dht.DHT22, 4)
        now = datetime.datetime.now()
        nowTime = now.strftime('%H:%M:%S')        
        print('time={0} Temp={1:0.1f}*C '.format(nowTime , t))
        wr.writerow([nowTime, t])
    
        time.sleep(1)
except KeyboardInterrupt:
    print("done")
