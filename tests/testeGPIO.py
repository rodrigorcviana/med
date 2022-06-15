import os, sys

if not os.getegid() == 0:
    sys.ext('start script as root')

from pyGPIO.gpio import gpio, port
from time import sleep

gpio.init()
gpio.setcfg(port.GPIO4, 1)

n = 0

while n < 50:
    gpio.output(port.GPIO4, 1)
    sleep(1)
    gpio.output(port.GPIO4, 0)
    sleep(1)
    n += 1

sys.exit('finished')