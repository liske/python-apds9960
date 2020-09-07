from apds9960.const import *
from apds9960 import APDS9960
import RPi.GPIO as GPIO
import smbus
from time import sleep

port = 1
bus = smbus.SMBus(port)

apds = APDS9960(bus)

def intH(channel):
    print("INTERRUPT")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)
try:
    # Interrupt-Event hinzufuegen, steigende Flanke
    GPIO.add_event_detect(7, GPIO.FALLING, callback = intH)

    print("Light Sensor Test")
    print("=================")
    apds.enableLightSensor()
    oval = -1
    while True:
        sleep(0.25)
        val = apds.readAmbientLight()
        r = apds.readRedLight()
        g = apds.readGreenLight()
        b = apds.readBlueLight()
        if val != oval:
            print("AmbientLight={} (R: {}, G: {}, B: {})".format(val, r, g, b))
            oval = val

finally:
    GPIO.cleanup()
    print("Bye")
