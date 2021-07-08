import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)

Button = 36
GPIO.setup(Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    button_state = GPIO.input(Button)
    print(button_state)
    sleep(1)
