# For working with audio
from gtts import gTTS
from playsound import playsound

#######################################
# AlfredCore class
# Holds the basic tools for speech and communication between
# skills that AlfredProtocol will need.
#######################################
class AlfredCore:
  _tts = '' # text to speech engine
  _stt = '' # speech to text engine

  def __init__(self, tts=None, stt=None ):
    """Init for AlfredCore

    Args:
        tts (function, optional): Text to speech function. Should accept text. Defaults to None.
        stt (function, optional): Speech to text function. Should return text. Defaults to None.
    """
    if tts:
      self._tts = tts
    if stt:
      self.stt = stt
  

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