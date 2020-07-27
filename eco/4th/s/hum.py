import Adafruit_DHT as dht
import time

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    print( 'Humidity={1:0.1f}%'.format(h))
    time.sleep(0.5)
