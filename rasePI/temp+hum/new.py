import Adafruit_DHT as dht
import time
import csv
import datetime
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

def gradient(x, y):
    W = tf.Variable( (y[9]-y[0]) / (x[9]-x[0])    )
    b = tf.Variable(y[0])

    learning_rate = 0.001

    with tf.GradientTape() as tape:
        hypothesis = W * x + b
        cost = tf.reduce_mean(tf.square(hypothesis - y))
    
    W_grad, b_grad = tape.gradient(cost, [W, b])
    W.assign_sub(learning_rate * W_grad)
    b.assign_sub(learning_rate * b_grad)

    return W, b, cost 


fTempHum = open('outputTime.csv', 'w', encoding='utf-8', newline='')
write = csv.writer(fTempHum)

timelist = []
humilist = []
templist = []

while True:

    h,t = dht.read_retry(dht.DHT22, 4)
 
    now = datetime.datetime.now()
    nowTime = now.strftime('%H:%M:%S')
    print(nowTime)
    print('Temp={0:0.01f}*C Humidity={1:0.01f}%'.format(t, h))
    
    timelist.append(now)
    humilist.append(h)
    templist.append(t)
    #print("humilist : ", humilist)
    time.sleep(.01)

    datalength = 10
    
    if len(humilist) == datalength:
       # plt.subplot(4, 1, 1)
       # plt.scatter(timelist, templist, label = "temp")
       # plt.legend()

       # plt.subplot(4, 1, 2)
       # plt.scatter(timelist, humilist, label = "humi")
       # plt.legend()
        
        # plt.show()
        
        time = np.arange(datalength).tolist()
        
        for i in range(100):
            W_temp, b_temp, cost_temp = gradient(time, templist)
            W_humi, b_humi, cost_humi = gradient(time, humilist)

            if i % 10 == 0:
               # print("{:5}|{:10.4}|{:10.4}|{:10.6f}".format(i, W_temp.numpy(), b_temp.numpy(), cost_temp))

                plt.subplot(2, 1, 1)
                plt.scatter(time, templist, label = "temp")
                
                x = np.arange(0, 11, 1)
                y = [(W_temp * num + b_temp) for num in x]

                plt.plot(x, y, c='r', label = "reg")
                plt.legend()

                plt.subplot(2, 1, 2)
                plt.scatter(time, humilist, label = "humi")

                x = np.arange(0, 11, 1)
                y = [(W_humi * num + b_humi) for num in x]

                plt.plot(x, y, c='r', label = "reg")
                plt.legend()

                plt.show()
                
                timelist = []
                humilist = []
                templist = []



              



