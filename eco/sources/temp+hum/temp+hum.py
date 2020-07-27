import Adafruit_DHT as dht
import time
import csv

fTempHum = open('output2.csv', 'w', encoding='utf-8', newline='')
write = csv.writer(fTempHum)

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    print( 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
    write.writerow([t , h])
    time.sleep(60.)
