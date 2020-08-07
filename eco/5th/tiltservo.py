import Adafruit_ADXL345
import time
import RPi.GPIO as GPIO

accel = Adafruit_ADXL345.ADXL345()

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
p = GPIO.PWM(13, 50)
p.start(0)

time.sleep(1)

try:
    while True:
        x, y, z = accel.read()
        if y < -100:
            print("x, y, z: {0}, {1}, {2} SERVO ROtATED".format(x, y, z))
            p.ChangeDutyCycle(10)
            print("angle : 90")
        elif y > 100:
            print("x, y, z: {0}, {1}, {2} SERVO ROtATED".format(x, y, z))
            p.ChangeDutyCycle(5)
            print("angle : 0")
        
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
