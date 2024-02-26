# AI Assistant

This project combines various technologies to create an AI assistant that can transcribe audio, respond to messages, and convert text to speech. The hardware used is a Raspberry Pi Zero with an IQaudIO Codec Zero.

## Components

### Raspberry Pi Zero

The Raspberry Pi Zero is a compact and affordable single-board computer that serves as the brain of the AI assistant. It runs the operating system and hosts the various software components.

### IQaudIO Codec Zero

The IQaudIO Codec Zero is an audio codec board that provides high-quality audio input and output. It connects to the Raspberry Pi Zero and handles the recording and playback of audio.

### Deepgram

Deepgram is a cloud-based speech recognition service that transcribes audio into text. It is used to convert the recorded audio into a text format that the AI assistant can understand.

### OpenAI

OpenAI is a research and deployment company in the field of artificial intelligence. Its GPT-3.5-turbo model is used to respond to user messages in a natural and engaging way.

### ElevenLabs

ElevenLabs is a text-to-speech service that converts text into high-quality audio. It is used to generate the AI assistant's responses in a clear and human-like voice.

## Functionality

The AI assistant works by recording audio from the user, transcribing it into text, and sending the text to the OpenAI model for processing. The model generates a response, which is then converted into speech using ElevenLabs and played back to the user.

## Usage

To use the AI assistant, simply press the button on the Raspberry Pi Zero. The assistant will start recording audio and transcribing it into text. Once the transcription is complete, the assistant will respond with a text message and play it back in a synthesized voice.

## Features

- Speech recognition
- Natural language processing
- Text-to-speech
- Compact and portable design

## Benefits

- Provides a convenient and intuitive way to interact with an AI assistant
- Can be used for a variety of tasks, such as answering questions, setting reminders, and playing games
- Can be modified and improved upon.
- Helps to make technology more accessible to people of all ages and abilities

## Issues

- Latency, both for recording audio and generating answers. It needs to load after pressing the button to record. The latency to generate answers can be improved by using a LLM that takes audio as input.
