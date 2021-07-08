import RPi.GPIO as GPIO
import mfrc522
import time

segments = [35,33,37,13,40,38,36]
#######     a, b, f, g, e, d, e

servoPin = 11

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


GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)

pos = GPIO.PWM(servoPin, 50)
#pos.start(12.5)
#time.sleep(2)

for pin in segments:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


op = False
while True:
    try:
        tagReader = mfrc522.MFRC522()
        (status, TagType) = tagReader.MFRC522_Request(tagReader.PICC_REQIDL)
        if status == tagReader.MI_OK:
            print("Tag detected")
            if not op:
                print(True)
                op = True
        if op:
            print("Run")
            pos.start(12.5)
            for i in range(10):
                for pin in segments:
                    print(pin)
                    index = segments.index(pin)
                    if numeros[i][index]:
                        print(numeros[i])
                        GPIO.output(pin, 0)
                    else:
                        GPIO.output(pin, 1)
                time.sleep(1)
            op = False
        if not(op):
            print("Stop")
            pos.stop()
    except Exception as e:
        print(e)
        break


#p.stop()
GPIO.cleanup()
