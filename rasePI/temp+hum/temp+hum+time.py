import Adafruit_DHT as dht
import time
import csv
import datetime

fTempHum = open('outputTime.csv', 'w', encoding='utf-8', newline='')
write = csv.writer(fTempHum)

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
 
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')
    print(nowTime)
    print( 'Temp={0:0.01f}*C Humidity={1:0.01f}%'.format(t, h))
    write.writerow([nowTime, t , h])
    time.sleep(60.)
