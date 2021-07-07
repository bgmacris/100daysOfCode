import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import I2C_LCD_driver
import time
import os

display = I2C_LCD_driver.lcd()
display.lcd_display_string("Hola Mundo", 1)

reader = SimpleMFRC522()

def cleanup():
    display.lcd_clear()

cleanup()
def write_card():
    try:
        text = input("New data:")
        print("Pase la targeta para escribir")
        reader.write(text=text)
        print("Written")
        print_lcd(text, 'write')
        time.sleep(3)
    finally:
        GPIO.cleanup()

def read_card():
    try:
        id, text = reader.read()
        print(id, text)
        print_lcd(text, 'read')
        time.sleep(3)
    finally:
        GPIO.cleanup()

def print_lcd(text, modo):
    cleanup()
    if modo == 'write':
        action = 'Se ha ecrito:'
    else:
        action = 'Lectura tarjeta'
    display.lcd_display_string(action, 1)
    display.lcd_display_string(text, 2)

if __name__ == '__main__':
    while True:
        os.system('clear')
        print("1 -> Write card")
        print("2 -> Read card")
        print("0 -> Exit")
        option = input("Selecceiona opcion: ")
        if option == '1':
            write_card()
        if option == '2':
            read_card()
        if option == '0':
            break
