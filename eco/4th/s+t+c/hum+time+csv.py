import Adafruit_DHT as dht
import time
import datetime
import csv

fHumT = open('humTime.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(fHumT)
time.sleep(1)

try:
    while True:
        h,t = dht.read_retry(dht.DHT22, 4)
        now = datetime.datetime.now()
        nowTime = now.strftime('%H:%M:%S')
            
        print('time={0} Humidity={1:0.1f}%'.format(nowTime , h))
        wr.writerow([nowTime, h])
    
        time.sleep(1)

except KeyboardInterrupt:
    print("done")
