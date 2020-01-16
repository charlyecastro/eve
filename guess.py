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
MAX_NUMBER = 100
eves_guess = 0

# Using the microphone, Eve listens to the user and returns a String Representations of what the user said. If eve can understand it will return 'Sorry, I did not get that'. If the speech service fails it will say 'Sorry, my speech service is down'
def listen(ask = False):
    with sr.Microphone() as source:
        audio = rec.listen(source)
        voice_data = ''
        try:
            voice_data = rec.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data

# Using Googles Text To Seech, the function takes in a String as a parameter which is then used to Speak in an english voice.
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    rand = random.randint(1, 10000000)
    audio_file = 'audio-' + str(rand) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# Eve introduces herslef and invites the user to play the guessing game. If the user answers yes, eve will then ask if the user wants to be the guesser or not, Otherwise Eve will say goodbye. 
def game_intro():
    time.sleep(1)
    speak("Hi my name is Eve. Do you want to play?")
    game_response = listen()
    if 'yes' in game_response:
        speak("do you want to guess?")
        guess_response = listen()
        if 'yes' in guess_response:
            user_guesses()
        else:
            speak("Okay, think of a number between 1 and 100.")
            time.sleep(3)
            speak("Ready?")
            #eve_guesses()
    else:
        speak("Okay, maybe next time.")
        exit()

# Eve picks a random number and listens to the users guesses until the user guesses the right number. Eve also keeps track of the number of guesses. Depending on the users guess, Eve will let the user know if their guess is too high or too low.
def user_guesses():
    users_guess = 0
    random_number = random.randint(1, MAX_NUMBER)
    speak("Okay, I am thinking of a number between 1 and 100. Guess what it is.")
    while users_guess != random_number:
        users_guess = listen()
        users_guess = int(users_guess)
        if users_guess > random_number:
            speak("The number I am thinking is less than " + users_guess)
        if users_guess < random_number:
            speak("The number I am thinking is greater than " + users_guess)
    speak("Great Job! you guessed it!")

# The user picks a random number and listens to Eve's guesses until the Eve guesses the right number. Eve also keeps track of the number of guesses. Depending on the Eve's guess, the user will let Eve know if their guess is too high or too low.
#def eve_guesses()
