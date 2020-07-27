import Adafruit_DHT as dht
import time
import csv

fTempT = open('TempTime.csv', 'w', encoding='utf-8', newline='')

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')        
    print('time = {0:0.01f} emp={0:0.1f}*C '.format(nowTime , t))
    write.writerow([nowTime, t])

    time.sleep(0.5)
