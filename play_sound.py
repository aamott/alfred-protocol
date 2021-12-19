import pyaudio
import wave
import sys

CHUNK = 1024


def play_wav_pyaudio(f):
    wf = wave.open(f, 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()

# requires pygame
from pygame import mixer
def play_mp3_pygame(f):
    mixer.init()
    mixer.music.load(f)
    mixer.music.play()

# requires: pydub, ffmpeg(search online how to get)
from pydub import AudioSegment
from pydub.playback import play
import io
def play_pydub(f):
    audio = AudioSegment.from_file(f)
    play(audio)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)
    f = open(sys.argv[1],'rb')
    play_wav_pyaudio(f)

