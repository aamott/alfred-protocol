# For working with audio
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from os import remove

#######################################
# AlfredUtils class
# Holds the basic tools for speech and communication between
# skills that AlfredProtocol will need.
#######################################
class AlfredUtils:
  _tts = None # text to speech engine
  _stt = None # speech to text engine

  def __init__(self, tts=None, stt=None ):
    """Init for AlfredUtils

    Args:
        tts (function, optional): Text to speech function. Should accept text. Defaults to None.
        stt (function, optional): Speech to text function. Should return text. Defaults to None.
    """
    if tts:
      self._tts = tts
    if stt:
      self._stt = stt
    else:
      self._recognizer = sr.Recognizer() # Initialize a Speech Recognizer object
      self._mic = sr.Microphone() # initialize a microphone

      with self._mic as source:
        self._recognizer.adjust_for_ambient_noise(source)
  

  def say(self, text):
    """Turns a string of text into audible speech

    Args:
        text (string): text to turn into speech
    """
    
    print(text)
    
    if self._tts:
      self._tts(text)
    else:
      # send audio to google
      google_audio = gTTS(text)

      # save audio
      filename = "speech.mp3"
      google_audio.save(filename)

      # play speech
      playsound(filename)

      # Remove file
      remove(filename)


  def listen(self):
    if (self._stt):
      phrase = self._stt()
      return phrase
    else:

      with self._mic as source:
        print("Listening...")
        audio = self._recognizer.listen(source, timeout = 10, phrase_time_limit=5)
        print("Finished listening")

      # Send audio to Google for processing
      phrase = self._recognizer.recognize_google(audio)

      return phrase