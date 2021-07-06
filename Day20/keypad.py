import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BOARD)

elements = [ [1,2,3,'A'],
             [4,5,6,'B'],
             [7,8,9,'C'],
             ['*',0,'#','D'] ]

row = [11,13,15,33]
column = [35,37,38,36]

def start_led():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)


    while True:
        if GPIO.input(40):
            GPIO.output(22, False)
            GPIO.output(32, True)
            GPIO.output(31, False)
            time.sleep(1)
            GPIO.output(32, False)
            GPIO.output(31, True)
            time.sleep(1)
        else:
            GPIO.output(31, False)
            GPIO.output(32, False)
            GPIO.output(22, True)

threading.Thread(target=start_led).start()

for i in range(4):
    GPIO.setup(column[i], GPIO.OUT)
    GPIO.output(column[i], 1)


for j in range(4):
    GPIO.setup(row[j], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while True:
        for j in range(4):
            GPIO.output(column[j], 0)
            for i in range(4):
                if GPIO.input(row[i]) == 0:
                    print(elements[i][j])
                    while(GPIO.input(row[i]) == 0):
                        pass
except KeyboardInterrupt:
    GPIO.cleanup()
