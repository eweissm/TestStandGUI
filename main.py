import serial
import time
import tkinter

def quit():
    global tkTop
    ser.write(bytes('L', 'UTF-8'))
    tkTop.destroy()

def set_button1_state():
        b += 1
        varLabel.set("LED ON ")
        ser.write(bytes('H', 'UTF-8'))
        varLabel2.set(b)
        print(b)

def set_button2_state():
        varLabel.set("LED OFF")
        ser.write(bytes('L', 'UTF-8')

        ser = serial.Serial('com7', 9600)
        print("Reset Arduino")
        time.sleep(3)
        ser.write(bytes('L', 'UTF-8'))