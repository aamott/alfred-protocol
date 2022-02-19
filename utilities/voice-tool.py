# For loading keys and data
import json

# For working with audio
from playsound import playsound
import speech_recognition as sr
from os import remove

# Temporary fix for playsound is to specify the entire filepath like so:
# path.abspath(filename).replace("\\", "/")
from os import path

#######################################
# Mozilla DeepSpeech
# Requires:
#     /python39.scripts/pip3.9.exe install deepspeech-gpu deepspeech
#     pip install -U TTS
#######################################
from deepspeech import Model
# For listening to mic
import io
import soundfile as sf
class DeepSpeech_STT:
    # The id of the object as it will appear in the json
    id = "DeepSpeech_STT"
    
    def __init__(self, model_file = 'deepSpeech/deepspeech-0.9.3-models.pbmm'):
        # Initialize stuff for recording with SpeechRecognition package
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()
        with self.mic as source:
            self.r.adjust_for_ambient_noise(source)

        self.ds = Model(model_file)


    def record_mic(self, samplerate=16000):
        """Records audio, stopping at first silence
            
            Records audio using the SpeechRecognition library
            then converts it to a wav file in Numpy array form
            for DeepSpeech.
            For information on the SpeechRecognition AudioData object, visit
            https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst

            Args:
                int samplerate  --  Samplerate the file should be returned with. 
            Returns:
                int samplerate  -- Must match the samplerate of the model trained!
                numpy.int16[] data -- wav audio file as an int16 Numpy array
        """
        # record
        print("Listening...")
        with self.mic as source:
            audioData = self.r.listen(source)
        print("Done listening")

        # convert to an int16 numpy array for DeepSpeech
        raw_wav = audioData.get_wav_data(convert_rate=samplerate)
        data, samplerate = sf.read(io.BytesIO(raw_wav), dtype="int16")
        return samplerate, data


    def listen(self):
        samplerate, data = self.record_mic()
        # get text with DeepSpeech (ds)
        return self.ds.stt(data)

#######################################
# IBM Text to Speech - Requires an API key
#######################################
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    
class IBM_TTS:
    # The id of the object as it will appear in the json
    id = "IBM_TTS"
    voices = ["en-US_EmilyV3Voice", "en-US_AllisonVoice", "en-US_HenryV3Voice", "en-AU_CraigVoice"]

    def __init__(self, api_key, service_url, voice = 'en-US_AllisonVoice'):
        """ IBM's Text to Speech wrapper for Alfred

            Parameters:
                key: key obtained from an IBM developer account
                service_url: Service URL from the same IBM developer account
                voice: The voice to be used
        """
        self.voice = voice
        authenticator = IAMAuthenticator(api_key)
        self.text_to_speech = TextToSpeechV1(
            authenticator=authenticator
        )

        self.text_to_speech.set_service_url(service_url)
            
    def say(self, text):
        filename = "tts.mp3"
        with open(filename,'wb') as audio_file:
            audio_data = self.text_to_speech.synthesize(text,voice=self.voice,accept='audio/mp3').get_result().content
            audio_file.write(audio_data)
        
        playsound(path.abspath(filename).replace("\\", "/"))
        remove(filename)
            
######################################
# Google Text to Speech
#
######################################
from gtts import gTTS
class Google_TTS:
    # The id of the object as it will appear in the json
    id="Google_TTS"

    def __init__(self, ):
        pass
        
    def say(self, text):
        # send audio to google and save it as a file
        filename = "tts.mp3"
        google_audio = gTTS(text)
        google_audio.save(filename)

        # play speech then remove the file
        playsound(path.abspath(filename).replace("\\", "/"))
        remove(filename)

###########################################
# Microsoft Text to Speech
# Documentation:
#    https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-text-to-speech?tabs=script%2Cbrowserjs%2Cwindowsinstall&pivots=programming-language-python
# For a list of voices, please visit
#    https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support#prebuilt-neural-voices
# Requirements
#    pip install azure-cognitiveservices-speech
###########################################
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech.audio import AudioOutputConfig # for audio output
class MS_Voice:
    # The id of the object as it will appear in the json
    id = "MS_Voice"

    def __init__(self, api_key, location_region, voice_name = "en-IE-EmilyNeural", language = None):
        """ Microsoft's Text to Speech wrapper for Alfred
            Find your key and resource region under the 'Keys and Endpoint' tab in your Speech resource in Azure Portal

            Parameters:
                api_key: key obtained from a developer account
                location_region: Location Region associated with the key (ex. "usgovarizona", "westus")
                voice_name: Name of voice
        """
        self.speech_config = speechsdk.SpeechConfig(subscription=api_key, region=location_region)
        if voice_name: 
            self.speech_config.speech_synthesis_voice_name = voice_name
        if language:
            self.speech_config.speech_synthesis_language = language # For example, "de-DE"
            
        #specific to listening
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config)

    def say(self, text, synthesize_to_file = False, filename="synthesized_speech.wav", synthesize_to_stream = False, is_ssml = False):
        #In this sample we are using the default speaker 
        #Learn how to customize your speaker using SSML in Azure Cognitive Services Speech documentation
        if synthesize_to_file:
            audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
        elif synthesize_to_stream: # Return the pure audio stream as a bytes object
            synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=None)
            result = synthesizer.speak_text_async(text).get()
            stream = AudioDataStream(result)
            return stream # a bytes object
        else:
            audio_config = AudioOutputConfig(use_default_speaker=True)
            
        synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)
        
        if is_ssml:
            synthesizer.speak_ssml_async(text)
        else:
            synthesizer.speak_text_async(text)
        
    def listen(self):
        
        #Asks user for mic input and prints transcription result on screen
        print("Listening...")
        result = self.speech_recognizer.recognize_once_async().get()
        print(result.text)
        
        return result.text
        
#######################################
# AlfredUtils class
# Holds the basic tools for speech
#######################################
class AlfredUtils:
    def __init__(self, tts=None, stt=None):
        """Init for AlfredUtils
            Params:
                tts: a class that has a "say" function. 
                    Should already be initialized. 
                tts: a class that has a "listen" function. 
                    Should already be initialized. 
        """
        if tts: 
            self.say = tts.say
        if stt:
            self.listen = stt.listen
        
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

        # send audio to google and save it as a file
        filename = "speech.mp3"
        google_audio = gTTS(text)
        google_audio.save(filename)

        # play speech then remove the file
        playsound(path.abspath(filename).replace("\\", "/"))
        remove(filename)


    def listen(self):
        audio = None
        with self._mic as source:
            print("Listening...")
            audio = self._recognizer.listen(source, timeout = 10, phrase_time_limit=5)
            print("Finished listening")

        # Send audio to Google for processing
        phrase = self._recognizer.recognize_google(audio)

        return phrase


if __name__ == "__main__":
    ################
    # load keys 
    api_keys = None
    with open('utilities\\keys.json') as file:
        api_keys = json.load(file)

    ################
    # Load Engines
    deepspeech = DeepSpeech_STT()

    google_tts = Google_TTS()
    if api_keys[IBM_TTS.id]["enabled"]:
        api_key = api_keys[IBM_TTS.id]["key"]
        service_url = api_keys[IBM_TTS.id]["service_url"]
        ibm_tts = IBM_TTS( api_key=api_key, service_url=service_url )

    if api_keys[MS_Voice.id]["enabled"]:
        api_key = api_keys[MS_Voice.id]["key"]
        location_region = api_keys[MS_Voice.id]["location_region"]
        ms_voice = MS_Voice( api_key=api_key, location_region=location_region)


    ################
    # Speech to Text - Listening

    # Test DeepSpeech Listening
    predicted_text = deepspeech.listen()
    print(predicted_text)

    # Test MS Listening
    user_speech = ms_voice.listen()
    print("You said...\n", user_speech)


    ################
    # Text to Speech - Saying

    # Test Google voice
    google_tts.say("This voice is from Google.")

    # Test IBM voice
    ibm_tts.say("This is IBM talking. Still speaking.")
    
    # Test MS voice
    ms_voice.say("This is a voice from Microsoft.")


    #################
    # Loading the voice into AlfredUtils

    # AlfredUtils test
    alfred_utils = AlfredUtils(tts=ms_voice, stt=deepspeech)
    alfred_utils.say("This is alfred testing your ears. Can you hear me?")
    user_speech = alfred_utils.listen()
    print('You said, "', user_speech, '"')

    # If we don't wait, the program dies too fast and it cuts the last audio short
    import time
    time.sleep(1)
