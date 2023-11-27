import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def check_grade():
    input_state = GPIO.input(2)
    if input_state == False:
        return "uncontracted"
    else:
        return "contracted"