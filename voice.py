#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import time
import random
import os
from datetime import datetime

# Create a directory to store recorded sounds

button = Button(27, hold_time=10)

def pressed():
    global press_time
    press_time = time.time()
    print("Pressed at %s" % (press_time));

def released():
    release_time = time.time()
    pressed_for = release_time - press_time
    print("Released at %s after %.2f seconds" % (release_time, pressed_for))
    if pressed_for < button.hold_time:
        print("This is a short press")
        os.system('aplay ' + "-D plughw:0,0 " + "test.wav")

def held():
    print("This is a long press")
    # os.system('aplay ' + burp)
    # os.system('arecord --format S16_LE --duration=5 --rate 48000 -c2 /home/pi/sounds/$(date +"%d_%m_%Y-%H_%M_%S")_voice.m4a');

button.when_pressed = pressed
button.when_released = released
button.when_held = held

pause()
