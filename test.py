import RPi.GPIO as GPIO
from action_control import action
import Speechtest
from pygame import mixer

mixer.init()

#engine = pt.init()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def button_callback(channel):
    print("pressed")

   
k = 1
while (True):
    text = Speechtest.speechToText()
    print(text)
    try:
        if "f*** this" in text:
            action(1)
        elif "quadratic" in text:
            action(2)
        elif "*" in text:
            action(0)
        elif "water water water" in text:
            mixer.music.load('loolooloo.mp3')
            mixer.music.play()
            print("### LOO! LOO! LOO!")
        #water water water loo loo loo
    except Exception as e:
        #print(e)
        pass
