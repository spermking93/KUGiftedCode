import Adafruit_DHT as dht
import time

try:
    while True:
        h,t = dht.read_retry(dht.DHT22, 4)
        print( 'Temp={0:0.1f}*C '.format(t))
        time.sleep(0.5)

except KeyboardInterrupt:
    print("done")
