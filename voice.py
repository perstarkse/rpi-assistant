#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import time
import random
import os
from datetime import datetime
import uuid

# Create a directory to store recorded sounds

button = Button(27, hold_time=2)

def record() -> str:
    uid = str(uuid.uuid4())
    print("Recording sound")
    file_path = os.path.join("inputs/", f"{uid}.wav")
    arecord_command = f"arecord --device=plughw:0,0 --format S16_LE --rate 44100 -c1 {file_path}"
    os.system(arecord_command)
    return file_path

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
    file_path = record()
    aplay_command = f"aplay -D plughw:0,0 {file_path}"
    os.system(aplay_command)
    # os.system('aplay ' + burp)
    # os.system('arecord --format S16_LE --duration=5 --rate 48000 -c2 /home/pi/sounds/$(date +"%d_%m_%Y-%H_%M_%S")_voice.m4a');

button.when_pressed = pressed
button.when_released = released
button.when_held = held

pause()
