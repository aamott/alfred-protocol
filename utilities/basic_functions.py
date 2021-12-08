# Development Environment information:
# OS: Windows 10
# Python 3.9

# pip installs
# pyaudio
# 

from typing import ChainMap
import gtts
import playsound
import os
import random
import time

def say(text):
    '''
    Sends text:str to google api for text to speech services.
    Plays the returned audio
    returns None
    '''
    if text == '':
        return
    tts = gtts.gTTS(text,lang='en')
    filename = f'.speech{"".join([str(random.randint(0,9)) for _ in range(8)])}.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

import speech_recognition as sr
r = sr.Recognizer()
def transcribe(f):
    '''
    Sends audio to speech to text api
    returns text:str
    '''
    if type(f) is not str:
        f.seek(0)
    with sr.AudioFile(f) as source:
        audio = r.record(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return -1


import io,wave
import pyaudio
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
def get_mic_frames(length):
    '''
    Gets audio from mic and returns it as a list
    returns audio-frames:list and sample_size:int
    '''
    frames = []
    audio = pyaudio.PyAudio()
    stream = audio.open(format = pyaudio.paInt16,channels=CHANNELS,rate = RATE,input=True,frames_per_buffer=CHUNK)
    for i in range(0, int(RATE / CHUNK * length)):
        data = stream.read(CHUNK)
        frames.append(data)
    stream.stop_stream() # 0.05
    stream.close() # 0.02
    audio.terminate() # 0
    return frames,audio.get_sample_size(FORMAT)

def record(length,file=None):
    '''
    Records audio from microphone, 
    return file object
    If optional parameter file is given then saves audio to file
    '''
    print("Recording")
    frames,sample_size = get_mic_frames(length)
    print('Finished recording')
    # If no file name is given then create temporary file (defined in memory not storage)
    if file is None:
        file = io.BytesIO()
    # insert audio data to file
    with wave.open(file,'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(sample_size)
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    return file

def listen(length):
    f = record(length)
    return transcribe(f)

# TODO: 
# add options for the length of the recording. Have it stop when it hears words and no longer hears them?
# Create class that houses all of these functions, possible name: Audio_UI
'''
class AudioUI:
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.CHUNK = 1024
    def record(self,length,file=None):
        print("Recording")
        frames,sample_size = get_mic_frames    
        print('Finished recording')
        # If no file name is given then create temporary file (defined in memory not storage)
        if file is None:
            file = io.BytesIO()
        # insert audio data to file
        with wave.open(file,'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(sample_size)
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
        return file

'''