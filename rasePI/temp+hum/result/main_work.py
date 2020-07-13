import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import modules


W1,b1= modules.LinearRegression( 10 , 0.001 )

print(W1,b1)

timeNext = 1.

hum = W1 * timeNext + b1

print(hum)

w1 = 23
w2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(w1,GPIO.OUT)
GPIO.output(w1,GPIO.LOW)
GPIO.setup(w2,GPIO.OUT)
GPIO.output(w2,GPIO.LOW)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000000


if (60. > hum) :
     GPIO.output(w1,GPIO.HIGH)
     GPIO.output(w2,GPIO.LOW)
else :
     GPIO.output(w1,GPIO.LOW)
     GPIO.output(w2,GPIO.LOW)
time.sleep(0.5)


GPIO.cleanup()
spi.close()


W2,b2 = modules.LinearRegression( 10 , 0.001 )

print(W2,b2)

temp = W2 * timeNext + b2 

print(temp)

w1 = 5
w2 = 6

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(w1,GPIO.OUT)
GPIO.output(w1,GPIO.LOW)
GPIO.setup(w2,GPIO.OUT)
GPIO.output(w2,GPIO.LOW)
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 5000000


if (30. < temp) :
     GPIO.output(w1,GPIO.HIGH)
     GPIO.output(w2,GPIO.LOW)
else :
     GPIO.output(w1,GPIO.LOW)
     GPIO.output(w2,GPIO.LOW)
time.sleep(10.0)


GPIO.cleanup()
spi.close()                 
