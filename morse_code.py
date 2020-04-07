#### IMPORTING LIBRARIES ####

from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

#### ASSIGNING THE LED's ####

led = LED(18)

#### CREATING WINDOWS/GUI DEFINATION ####

win = Tk()
win.title("Morse Code")
my_font = tkinter.font.Font(family = 'Helvetica', size = 12, weight ="bold")

text = StringVar()

def limit_text(*args):
    entry = text.get()
    if ( len(entry) > 12 ):
        text.set( entry[:12])

text.trace_variable("w", limit_text)

#### SETTING THE DOT AND DASH ####

def dot():
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.8)

def dash():
    led.on()
    time.sleep(1.5)
    led.off()
    time.sleep(0.8)

#### MORSE CODE FOR ALPHABET ####

def morse_code(alp):
    if (alp == "a"):
        dot()
        dash()

    if (alp == "b"):
        dash()
        dot()
        dot()
        dot()

    if (alp == "c"):
        dash()
        dot()
        dash()
        dot()

    if (alp == "d"):
        dash()
        dot()
        dot()

    if (alp == "e"):
        dot()

    if (alp == "f"):
        dot()
        dot()
        dash()
        dot()

    if (alp == "g"):
        dash()
        dash()
        dot()

    if (alp == "h"):
        dot()
        dot()
        dot()
        dot()

    if (alp == "i"):
        dot()
        dot()
    if (alp == "j"):
        dot()
        dash()
        dash()
        dash()

    if (alp == "k"):
        dash()
        dot()
        dash()

    if (alp == "l"):
        dot()
        dash()
        dot()
        dot()

    if (alp == "m"):
        dash()
        dash()
        
    if (alp == "n"):
        dash()
        dot()

    if (alp == "o"):
        dash()
        dash()
        dash()

    if (alp == "p"):
        dot()
        dash()
        dash()
        dot()

    if (alp == "q"):
        dash()
        dash()
        dot()
        dash()

    if (alp == "r"):
        dot()
        dash()
        dot()

    if (alp == "s"):
        dot()
        dot()
        dot()

    if (alp == "t"):
        dash()

    if (alp == "u"):
        dot()
        dot()
        dash()

    if (alp == "v"):
        dot()
        dot()
        dot()
        dash()

    if (alp == "w"):
        dot()
        dash()
        dash()

    if (alp == "x"):
        dash()
        dot()
        dot()
        dash()

    if (alp == "y"):
        dash()
        dot()
        dash()
        dash()

    if (alp == "z"):
        dash()
        dash()
        dot()
        dot()

def start():
    name = text_box.get()
    for i in name:
        morse_code(i.lower())

def close():
    RPi.GPIO.cleanup()
    win.destroy()

#### TABS/WIDGETS/TEXTBOX ####
label = Label(win, text = "Name: ")
label.grid(row = 0, column = 0)

text_box = Entry(win, bd=5, textvariable=text)
text_box.grid(row = 0, column = 1)

startButton = Button(win, text = 'Start', font = my_font, command = start, bg = 'bisque1', height = 1, width = 6)
startButton.grid(row = 1, column = 1)

exitButton = Button(win, text = 'Exit', font = my_font, command = close, bg = 'bisque1', height = 1, width = 6)
exitButton.grid(row = 1, column = 2)
    
#### CLOSING THE WINDOW CLEANLY ####

win.protocol("WM_DELETE_WINDOW", close)

#### INFINITE/NEVER-ENDING LOOP ####

win.mainloop()

