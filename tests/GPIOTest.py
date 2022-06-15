import os, sys
import RPi.GPIO as GPIO
from time import sleep

if not os.getegid() == 0:
    sys.ext('start script as root')

GPIO.setmode(GPIO.RAW)
GPIO.setup(GPIO.PB+20, GPIO.OUT)

n = 0

while n < 50:
    GPIO.output(GPIO.PB+20, 0)
    sleep(1)
    GPIO.output(GPIO.PB+20, 1)
    sleep(1)
    n += 1

sys.exit('finished')
