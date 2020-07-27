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
    
    #위의 while구문에서 반복한 횟수 만큼 측정된 온도 데이터를 출력합니다. 
    #print(templist)
    
    # x값 데이터에 위에서 측정된 시간리스트를 저장합니다.
    x_data = timelist

    # y1값 데이터에 위에서 측정된 습도리스트를 저장합니다. 
    y_data = humilist
      
    # 구하고자 하는 습도의 일차함수의 y절편의 값을 i= t=0에서의 습도값으로 정합니다.
    b_initial = humilist[0]
    
    # 구하고자 하는 습도의 일차함수의 기울기를 i=1(t=0.01s)와 i=8(t=0.08s)일때의 습도값 데이터로 구합니다. 
    W_initial = (humilist[8] - humilist[1]) / 8.
  
      
    # 위에서 기울기를 구하는 방식을 텐서플로우에 활용 되게끔 형식에 맞게 변수로 초기화 합니다.  
    W = tf.Variable(W_initial)
    
    # 위에서 y절편을 구하는 방식을 텐서플로우에 활용 되게끔 형식에 맞게 변수로 초기화 합니다.
    b = tf.Variable(b_initial)
    
    # 학습 전 초기 기울기 값을 '0'으로 설정합니다.
    W_result = 0.
    
    # 학습 전 초기 y절편 값을 '0'으로 설정합니다.
    b_result = 0.
    
    # 학습 전 초기 습도 값을 '0'으로 설정합니다. 
    hum_result= 0.
           
    # 텐서플로우의 학습률을 나타냅니다.학습률이란 기울기 값을 얼마만큼 반영할지 결정하는 인자입니다. 
    learning_rate = lr
    
    # 100번 학습을 반복시킵니다. 
    for i in range(100):
        
        # 텐서플로우에서 제공하는 기울기를 구하는 API
        with tf.GradientTape() as tape:
            
            # 가설 변수 설정(추세선) 
            hypothesis = W * x_data + b
                        
            # 오차의 제곱의 평균을 cost에 저장합니다. 
            cost = tf.reduce_mean(tf.square(hypothesis - y_data))
            
    
        # cost의 W,b에 대한 미분 값을 순서대로 할당하며 이를 지속적으로 갱신합니다.즉,기울기를 업데이트하는 것.
        W_grad, b_grad = tape.gradient(cost, [W, b])
        

        # 업데이트된 순간 기울기가 양이면 왼쪽으로 이동, 음이면 오른쪽으로 이동합니다.
        W.assign_sub(learning_rate * W_grad)
        b.assign_sub(learning_rate * b_grad)
            
        # 50번마다 중간결과를 형식에 맞게 출력합니다.
        if i % 50 == 0:
            print("{:5}|{:10.4}|{:10.4}|{:10.6f}".format(i, W.numpy(), b.numpy(), cost))
                        
            # x데이터(시간) y데이터(습도,온도)를 x-y평면에 점분포로 나타냅니다.
            plt.scatter(x_data, y_data, label = 'data')
            
            
            # x를 0~10 까지 1간격으로 등차적으로 나타냅니다.
            x = np.arange(0, 10, 1)
            
            # 위에 짜여진 x값과 학습된 결과로 나온 W*x+b로 y값을 나타냅니다.
            y = [(W * num + b) for num in x]
                
            # 위에서 구한 x,y좌표를 토대로 일차함수 그래프를 그립니다. 
            plt.plot(x, y, c='r', label = 'W = '+ str(W.numpy()) + ',  b = ' + str(b.numpy()))
                        
            # 텐서플로우에서 꺼내온 데이터(W,b)를 numpy array로 바꿔줍니다.  
            W_result = W.numpy()
            b_result = b.numpy()
                        
            # 그래프의 제목을 'i값'으로 지정합니다.
            plt.title('i = ' + str(i))
            
            # 범례룰 입력합니다.
            plt.legend()
            
            # 그래프를 보여줍니다. 
            plt.show()
    
    # 위에서 구한 W,b를 최종적으로 반환C합니다. 
    return W_result, b_result  

