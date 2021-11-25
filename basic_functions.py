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
    tts = gtts.gTTS(text,lang='en',tld='com.jp')
    filename = f'.speech{"".join([str(random.randint(0,9)) for _ in range(8)])}.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

import pyaudio
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024

times = [time.time()]
audio = pyaudio.PyAudio() # 0.51
times.append(time.time())
stream = audio.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK) # 0.75
times.append(time.time())
stream.stop_stream() # 0.05
times.append(time.time())
stream.close() # 0.02
times.append(time.time())
audio.terminate() # 0
times.append(time.time())

v = times.pop(0)
for i,t in enumerate(times):
    print(i,t-v)
    # if i != 0:
    #     print(i,t-times[i-1])

def listen():
    text = ''

    return text

say('hello world!')

listen()

