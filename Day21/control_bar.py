import RPi.GPIO as GPIO
import time

ledPins = [12,11,13,15,16,18,22,3,5,24]
segments = [35,37,31,29,32,36,38]
########    a, b, f, g, e, d, c

numeros = {
        0: (1,1,1,0,1,1,1),
        1: (0,1,0,0,0,0,1),
        2: (1,1,0,1,1,1,0),
        3: (1,1,0,1,0,1,1),
        4: (0,1,1,1,0,0,1),
        5: (1,0,1,1,0,1,1),
        6: (1,0,1,1,1,1,1),
        7: (1,1,0,0,0,0,1),
        8: (1,1,1,1,1,1,1),
        9: (1,1,1,1,0,0,1)
    }

def setup():
    GPIO.setmode(GPIO.BOARD)
    for i in ledPins:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    for j in segments:
        GPIO.setup(j, GPIO.OUT)
        GPIO.output(j, 1)

def destroy():
    for i in ledPins:
        GPIO.output(i, GPIO.HIGH)
    for j in segments:
        GPIO.output(j, 1)
    GPIO.cleanup()


def draw_num(num):
    for j in segments:
        index = segments.index(j)
        if numeros[num][index]:
            GPIO.output(j, 0)
        else:
            GPIO.output(j, 1)

def starting():
    count = 0
    for i in ledPins:
        GPIO.output(i, GPIO.LOW)
        draw_num(count)
        count = count + 1
        time.sleep(0.5)


def on_bar():
    while True:
        try:
            num = int(input())
            if num >= 10:
                break
            for i in ledPins:
                GPIO.output(ledPins, GPIO.HIGH)
            for i in range(num):
                GPIO.output(ledPins[i], GPIO.LOW)
            draw_num(num)
        except:
            pass


setup()
#starting()
on_bar()
destroy()
