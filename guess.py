import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

rec = sr.Recognizer()
random_number = 100
max_number = 100
eves_guess = 0
users_guess = 1


def listen(ask = False):
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

def ask_to_play():
    time.sleep(1)
    speak("do you want to play?")
    game_response = listen()
    if 'yes' in game_response:
        speak("do you want to guess?")
        guess_response = listen()
        if 'yes' in guess_response:
            random_number = random.randint(1, 100)
            start_game(random_number)
        else:
            speak("Okay, think of a number between 1 and 100")
            time.sleep(3)
            speak("Ready?")

    else:
        exit()

# def make_guesses:

def start_game(num):
    users_guess = 0
    random_number = num
    speak("Okay, I am thinking of a number between 1 and 100. Guess what it is.")
    while users_guess != random_number:
        users_guess = listen()
        users_guess = int(users_guess)
        if users_guess > random_number:
            speak("It is smaller")
        if users_guess < random_number:
            speak("It is bigger")
    speak("Great Job! you guessed it!")


ask_to_play()
