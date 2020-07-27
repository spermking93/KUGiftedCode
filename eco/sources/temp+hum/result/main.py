import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import modules
import RPi.GPIO as GPIO
import time
import spidev


w,b = modules.LinearRegression( 10 , 0.001 )

print(w,b)

timeNext = 1.

hum = w * timeNext + b 

print(hum)

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


if (60. > hum) :
    GPIO.output(w1,GPIO.HIGH)
    GPIO.output(w2,GPIO.LOW)
else :
    GPIO.output(w1,GPIO.LOW)
    GPIO.output(w2,GPIO.LOW)
time.sleep(0.5)


GPIO.cleanup()
spi.close()
