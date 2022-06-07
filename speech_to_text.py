#!/usr/bin/env python3
#requires PyAudio and SpeechRecognition libraries
#pip install PyAudio
#pip install SpeechRecognition


import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Talk into the microphone.")
    audio = r.listen(source)

try:
    output = r.recognize_google(audio)
    print("You said " + output)
except sr.UnknownValueError:
    print("Could not understand what you said.")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
