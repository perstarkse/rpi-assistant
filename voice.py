#!/usr/bin/env python3
from gpiozero import Button, LED
from signal import pause
import time
import os
import subprocess
from datetime import datetime
import uuid
import signal

button = Button(27, hold_time=2)
green_led = LED(23)
recording_process = None
file_path = None

def record():
    uid = str(uuid.uuid4())
    print("Recording sound")
    global file_path
    file_path = os.path.join("inputs/", f"{uid}.wav")
    arecord_command = ["arecord", "--device=plughw:0,0", "--format", "S16_LE", "--rate", "44100", "-c1", "--nonblock", file_path]

    global recording_process
    recording_process = subprocess.Popen(arecord_command, preexec_fn=os.setsid)
    time.sleep(1)
    green_led.on()

def released():
    global recording_process
    global file_path

    print("Released at %s" % (time.time()))
    green_led.off()
    if recording_process is not None:
        print("Stopping recording process")
        
        # Send a signal to the entire process group
        os.killpg(os.getpgid(recording_process.pid), signal.SIGINT)

        time.sleep(1)
        
        # Play the recorded audio
        print("Playing the recorded audio")
        os.system(f"aplay -D plughw:0,0 -c1 {file_path}")

print("Press the button to record")
button.when_pressed = record
button.when_released = released

pause()

