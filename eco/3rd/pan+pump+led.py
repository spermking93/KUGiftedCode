import RPi.GPIO as GPIO
import time

pins = {'pan1':5, 'pan2':6, 'pump1':23, 'pump2':24}
led = {'r':19, 'g':21, 'b':20}

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)
    GPIO.output(pins[i], GPIO.LOW)

for j in led:
    GPIO.setup(led[j], GPIO.OUT)
    GPIO.output(led[j], GPIO.HIGH)
    
try:
    while True:
        GPIO.output(pins['pan1'], GPIO.HIGH)
        GPIO.output(pins['pump1'], GPIO.HIGH)
        
        GPIO.output(led['r'], GPIO.HIGH)
        GPIO.output(led['g'], GPIO.HIGH)
        GPIO.output(led['b'], GPIO.LOW)
        
        time.sleep(1)
        
        GPIO.output(pins['pan1'], GPIO.LOW)
        GPIO.output(pins['pump1'], GPIO.LOW)

        GPIO.output(led['r'], GPIO.LOW)
        GPIO.output(led['g'], GPIO.HIGH)
        GPIO.output(led['b'], GPIO.HIGH)
        
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
