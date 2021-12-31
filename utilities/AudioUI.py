# General purpose 
import os,random,io
# Audio (input or output)
import pyaudio
from playsound import playsound
from pydub import AudioSegment
import speech_recognition
import gtts
from pydub.playback import play
import wave
# Self made files
from utilities.basic_functions import get_mic_frames

class AudioUI:
    '''
    Audio object meant to take care of all audio functions, including
    recording audio, playing audio, speech-to-text services, and text-
    -to-speech services
    '''
    def __init__(self,speech_file=None):
        self.CHANNEL = 2
        self.RATE = 44100
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self._sayfile = speech_file if speech_file else ''.join([str(random.randint(0,9)) for _ in range(8)])
        self._sayobject = io.BytesIO()
        self.r = speech_recognition.Recognizer()

    def play_sound(self,audio_file):
        '''
        Plays audio, uses the library playsound if input is a file path
        uses the library pydub if input is a file like object
        I believe it uses ffmpeg if file like object input is mp3 type
        '''
        if type(audio_file) is str:
            playsound(audio_file)
        else:
            try:
                audio_file.seek(0)
            except:
                pass
            audio = AudioSegment.from_file(audio_file)
            play(audio)
            # raise Exception("Audio to play must be file path for now")
    
    def say(self,text,file=None):
        '''
        Sends text:str to google api for text to speech services
        a. file:str -> Saves speech to mp3 file
        b. file:None -> Saves speech to self file object
        c. file:filelike object -> Saves speech to external file object
        Plays speech
        '''
        if text == '':
            return
        tts = gtts.gTTS(text,lang='en')
        if type(file) is str:
            tts.save(file)
        else:
            if file is None:
                self._sayobject.seek(0)
                self._sayobject.truncate(0)
                file = self._sayobject
            try:
                tts.write_to_fp(file)
            except:
                print("Could not write to file like object")
                raise
        self.play_sound(file)

    def record(self,time,file=None):
        '''
        Records time:int||float seconds of audio from microphone, 
        return file object
        If optional parameter file is given then saves audio to file
        TODO: record while person is talking
        '''
        print("Recording")
        frames,sample_size = get_mic_frames(time)
        print("Finished Recording")
        if file is None:
            file = io.BytesIO()
        with wave.open(file,'wb') as wf:
            wf.setnchannels(self.CHANNEL)
            wf.setsampwidth(sample_size)
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
        return file

    def transcribe(self,audio_file):
        '''
        Provides speech to text services using the speech_recognition
        library. Does require internet services.
        audio_file can be file path or file like object
        '''
        if type(audio_file) is not str:
            try:
                audio_file.seek(0)
            except:
                pass
        with speech_recognition.AudioFile(audio_file) as source:
            audio = self.r.record(source)
        try:
            return self.r.recognize_google(audio)
        except speech_recognition.UnknownValueError:
            return -1
    
    def listen(self):
        audio = self.record(5)
        return self.transcribe(audio)
        



if __name__ == '__main__':
    aui = AudioUI()
    # aui.say_nofile("Hello!")