#!/usr/bin/env python3
from gpiozero import Button, LED
from signal import pause
import os
import uuid
import threading
import io
import wave
import signal
from deepgram import transcribe_audio
from llm import respond_to_message
import sys
from elevenlabs import text_to_speech
import pyaudio

button = Button(27, hold_time=2)
green_led = LED(23)
red_led = LED(24)
recording_process = None
file_path = None

chunk = 512  # Record in chunks of 512 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 16000  # Record at 16000 samples per second

p = pyaudio.PyAudio()  # Create an interface to PortAudio

recording = False

def signal_handler(sig, frame):
    print("Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def play_audio(file_path):
    print("Playing the recorded audio")
    # os.system(f"aplay -D plughw:0,0 --format S16_LE -c1 {file_path}")
    os.system(f"ffplay -autoexit {file_path}")

# Define a function to transcribe audio
def transcribe_and_print_result(buffer: io.BytesIO) -> str:
    print("Transcribing audio")
    transcription = transcribe_audio(buffer)
    message = transcription['results']['channels'][0]['alternatives'][0]['transcript']
    print(message)
    return message

def record():
    global recording_thread
    recording_thread = threading.Thread(target=start_record)
    recording_thread.start()

def start_record():
    print('Recording')
    global stream
    global recording
    recording = True
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)
    green_led.on()
    global frames
    frames = []  

    # Store data in chunks
    while recording: 
        data = stream.read(chunk, exception_on_overflow=False)
        
        # Append the data to the frames array
        frames.append(data)

def play_recording():
    play_stream = p.open(format=sample_format,
                         channels=channels,
                         rate=fs,
                         output=True,
                         frames_per_buffer=chunk
                         )
    
    # Play the recorded audio
    for frame in frames:
        play_stream.write(frame)

    frames.clear()

    play_stream.stop_stream()
    play_stream.close()

def released():
    print("Stopping recording process")
    green_led.off()

    global recording

    recording = False

    recording_thread.join()

    stream.stop_stream()
    stream.close()

    wav_data = io.BytesIO()
    wav_format = wave.open(wav_data, 'wb')
    wav_format.setnchannels(channels)
    wav_format.setsampwidth(p.get_sample_size(sample_format))
    wav_format.setframerate(fs)
    for frame in frames:
        wav_format.writeframes(frame)
    wav_format.close()

    # Rewind the BytesIO object
    wav_data.seek(0)

    # Play the recorded audio
    # recording_audio_thread = threading.Thread(target=play_recording)
    # recording_audio_thread.start()

    # Send the transcription request
    message = transcribe_and_print_result(wav_data)

    # Send the transcription to the AI model
    response = respond_to_message(message)

    # Print the response
    print(response)

    # Convert the response to speech
    print("Converting the response to speech")
    audio_file = text_to_speech(response, str(uuid.uuid4()))

    # Play the response
    audio_thread = threading.Thread(target=play_audio, args=(audio_file,))
    audio_thread.start()

    # Wait for the audio playback thread to finish
    audio_thread.join()
    # recording_audio_thread.join()
    print("Finished playing the response")

print("Press the button to record")
button.when_pressed = record
button.when_released = released

red_led.on()

pause()

