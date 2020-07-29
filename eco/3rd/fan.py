import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.LOW)
GPIO.setup(6, GPIO.OUT)
GPIO.output(6, GPIO.LOW)

GPIO.output(5, GPIO.HIGH)
time.sleep(5)
GPIO.output(5, GPIO.LOW)

GPIO.cleanup()
