import Adafruit_DHT as dht
import time
import csv
import datetime
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

fTempHum = open('outputTime.csv', 'w', encoding='utf-8', newline='')
write = csv.writer(fTempHum)

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
    # print("humilist : ", humilist)
    time.sleep(.01)

    if len(humilist) == 10:
        
        timeOut = len(humilist)
        humiOut = humilist
        tempOut = templist

        plt.subplot(4, 1, 1)
        plt.scatter(timelist, templist, label = "temp")
        plt.legend()

        plt.subplot(4, 1, 2)
        plt.scatter(timelist, humilist, label = "humi")

        plt.legend()
       # plt.show()
        
        
        timelist = []
        humilist = []
        templist = []
    
    print(timeOut)


    x_data = timeOut
    y_data = humiOut
    
    W = tf.Variable(0.01)
    b = tf.Variable(y_data[0])
    
    learning_rate = 0.001
    
    for i in range(100):
        with tf.GradientTape() as tape:
            hypothesis = W * x_data + b
            cost = tf.reduce_mean(tf.square(hypothesis - y_data))
    
        W_grad, b_grad = tape.gradient(cost, [W, b])
        W.assign_sub(learning_rate * W_grad)
        b.assign_sub(learning_rate * b_grad)
    
        if i % 10 == 0:
            print("{:5}|{:10.4}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))
    
            plt.scatter(x_data, y_data, label = 'data')
    
            x = np.arange(0, 20, 1)
            y = [(W * num + b) for num in x]
    
    
            plt.plot(x, y, c='r', label = 'W = '+ str(W.numpy()) + ',  b = ' + str(b.numpy()))
    
            plt.title('i = ' + str(i))
            plt.legend()
            plt.show()
