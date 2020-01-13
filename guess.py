import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

rec = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if(ask):
            speak(ask)
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, ny speech service is down')
        return voice_data

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    rand = random.randint(1, 10000000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)