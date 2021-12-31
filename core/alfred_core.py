# For working with audio
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from os import remove
import sys
if __name__ == '__main__':
  sys.path.append('..\\utilities')
  from AudioUI import AudioUI
else:
  from utilities.AudioUI import AudioUI
#######################################
# AlfredCore class
# Holds the basic tools for speech and communication between
# skills that AlfredProtocol will need.
#######################################
class AlfredCore:
  _tts = None # text to speech engine
  _stt = None # speech to text engine

  def __init__(self, tts=None, stt=None ):
    """Init for AlfredCore

    Args:
        tts (function, optional): Text to speech function. Should accept text. Defaults to None.
        stt (function, optional): Speech to text function. Should return text. Defaults to None.
    """
    self.audioui = AudioUI()
    if tts:
      self._tts = tts
    if stt:
      self._stt = stt
    else:
      self._recognizer = sr.Recognizer() # Initialize a Speech Recognizer object
      self._mic = sr.Microphone() # initialize a microphone


  def say(self, text):
    """Turns a string of text into audible speech
    Output:
        Audible speech through device speaker
    Args:
        text (string): text to turn into speech
    """
    self.audioui.say(text)
    return
  def listen(self):
    """Record audio with mic and returns text
    Output:
        return: text (string): text from audio text
    Input:
        audio from device mic
    """
    return self.audioui.listen()


    '''
  def say(self, text):
    """Turns a string of text into audible speech

    Args:
        text (string): text to turn into speech
    """
    self.audioui.say(text)
    return
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
    '''

    '''
  def listen(self):
    return self.audioui.listen()
    if (self._stt):
      phrase = self._stt()
      return phrase
    else:

      with self._mic as source:
        print("Listening...")
        audio = self._recognizer.listen(source)
        print("Finished listening")

      # Send audio to Google for processing
      phrase = self._recognizer.recognize_google(audio)

      return phrase
    '''