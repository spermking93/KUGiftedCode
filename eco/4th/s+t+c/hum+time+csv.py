import Adafruit_DHT as dht
import time
import csv

fHumT = open('humTime.csv', 'w', encoding='utf-8', newline='')

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')
        
    print('time = {0:0.01f} Humidity={1:0.1f}%'.format(nowTime , h))
    write.writerow([nowTime, h])

    time.sleep(0.5)
