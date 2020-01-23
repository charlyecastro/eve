import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

# The user is able to ask eve questions such as their name, the time, find location for a place, and search something

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

def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Eve')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'x' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak ('Here is the location of ' + location)
    if 'exit' in voice_data:
        speak('Goodbye!')
        exit()

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    rand = random.randint(1, 10000000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)
speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)