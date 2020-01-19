import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def jar():
    GPIO.setup(21,GPIO.IN)

    if(GPIO.input(21)==GPIO.HIGH):
        return True
    
    return False

