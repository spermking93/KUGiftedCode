import Adafruit_DHT as dht
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np

timelist = []
humilist = []
templist = []

timeOut = []
humiOut = []
tempOut = []

while True:
    h,t = dht.read_retry(dht.DHT22, 4)
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')
    print(nowTime)
    print('Temp={0:0.01f}*C Humidity={1:0.01f}%'.format(t, h))   
    timelist.append(now)
    humilist.append(h)
    templist.append(t)
 
    time.sleep(.01)

    if len(timelist) == 100:
        timeOut = len(humilist)
        humiOut = humilist
        tempOut = templist

        plt.subplot(2, 1, 1)
        plt.scatter(timelist, templist, label = "temp")
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.scatter(timelist, humilist, label = "hum")

        plt.legend()
        plt.show()

        timelist = []
        humilist = []
        templist = []    

