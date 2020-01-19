import sys
sys.path.append("/home/pi/.local/lib/python2.7/site-packages")

import speech_recognition as sr

r = sr.Recognizer()
    
def speechToText():
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source, phrase_time_limit = 2)
        
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))