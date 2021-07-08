import RPi.GPIO as GPIO
import time

servoPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)

p = GPIO.PWM(servoPin, 50)
p.start(1.0)
time.sleep(60)
