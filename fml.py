import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)

p = GPIO.PWM(2, 50)
p.start(2.5)

p.ChangeDutyCycle(5)
time.sleep(0.5)
p.ChangeDutyCycle(12.5)
time.sleep(0.5)
