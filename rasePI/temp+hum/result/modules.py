import Adafruit_DHT as dht
import time
import csv
import datetime
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np

#LInearRegression이라는 함수를 정의합니다.
def LinearRegression(step, lr):
    # 시간에 대한 리스트
    timelist = []
    # 습도에 대한 리스트
    humilist = []
    # 온도에 대한 리스트
    templist = []

    timeOut = []
    humiOut = []
    tempOut = []
    
    # while 반복문 
    i = 0

    # i가 step값 보다 작은 범위 한에서 아래 과정을 반복합니다. 
    while i < step:
        # 센서값을 읽어서 저장합니다.
        h,t = dht.read_retry(dht.DHT22, 4)

        # 현재 시각에 대한 값을 저장합니다.  
        now = datetime.datetime.now()

        # 시각을 시,분,초로 나타냅니다. 
        nowTime = now.strftime('%H:%M:%S')
        
        # 시,분,초로 나타낸 현재 시각을 출력합니다.
        print(nowTime)
        
        # 온도 습도를  형식에 맞게 값을 출력합니다..
        print('Temp={0:0.01f}*C Humidity={1:0.01f}%'.format(t, h))
    
        # i를 시간의 리스트 값으로 추가합니다.
        timelist.append(i)
        
        # 측정된 습도값을 리스트값에 추가합니다.
        humilist.append(h)
        
        # 측정된 온도값을 리스트값에 추가합니다.
        templist.append(t)
        
        # 실제 시간간격을 0.01초로 설정합니다.
        time.sleep(.01)
        
        # i에다 1을 더한다. 즉 step값 보다 작은 범위안에서 위의 과정을 반복합니다.
        i = i + 1;

    #위의 while구문에서 반복한 횟수 만큼 측정된 습도 데이터를 출력합니다.
    print(humilist)  
    
    # x값 데이터에 위에서 측정된 시간리스트를 저장합니다.
    x_data = timelist
    # y값 데이터에 위에서 측정된 습도리스트를 저장합니다. 
    y_data = humilist
    # 구하고자 하는 일차함수의 y절편의 값을 i= t=0에서의 습도값으로 정합니다.
    b_initial = humilist[0]
    # 구하고자 하는 일차함수의 기울기를 i=1(t=0.01s)와 i=8(t=0.08s)일때의 습도값 데이터로 구합니다. 
    W_initial = (humilist[8] - humilist[1]) / 8.

    print(W_initial)
    
    W = tf.Variable(W_initial)
    b = tf.Variable(b_initial)
    W_result = 0.
    b_result = 0.
    hum_result= 0.
    learning_rate = lr
    
    for i in range(100):
        with tf.GradientTape() as tape:
            hypothesis = W * x_data + b
            cost = tf.reduce_mean(tf.square(hypothesis - y_data))
    
        W_grad, b_grad = tape.gradient(cost, [W, b])
        W.assign_sub(learning_rate * W_grad)
        b.assign_sub(learning_rate * b_grad)
    
        if i % 50 == 0:
            print("{:5}|{:10.4}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))
    
            plt.scatter(x_data, y_data, label = 'data')
    
            x = np.arange(0, 10, 1)
            y = [(W * num + b) for num in x]
    
            
            plt.plot(x, y, c='r', label = 'W = '+ str(W.numpy()) + ',  b = ' + str(b.numpy()))
            
            W_result = W.numpy()
            b_result = b.numpy()
            plt.title('i = ' + str(i))
            plt.legend()
            plt.show()
    
    return W_result, b_result

