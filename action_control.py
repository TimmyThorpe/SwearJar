#include <stdio.h>
#include <stdlib.h>
#include <math.h>
from pygame import mixer

mixer.init()
songs = ["money.mp3","edcomisdeep.mp3", "edcomdisappointed.mp3"]


import RPi.GPIO as GPIO
from swearJar import jar
from pygame import mixer
import time

def action(i):
    servoPIN = 8
    
    GPIO.setup(servoPIN, GPIO.OUT)

    p = GPIO.PWM(servoPIN, 50)
    p.start(2.5)
    
    while jar() == False:
        try:
            if mixer.music.get_busy() == 0:
                mixer.music.load(songs[i])
                mixer.music.play()
            p.ChangeDutyCycle(5)
            time.sleep(0.5)
            p.ChangeDutyCycle(12.5)
            time.sleep(0.5)
        except:
            print("error")
    
    mixer.music.stop()
    
      
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)  
#action()
