import RPi.GPIO as GPIO, time, os
import time

GPIO.setmode(GPIO.BCM)

class Valve(object):
    
    def __init__(self, pin):
        self.valvePin = pin
        GPIO.setup(self.valvePin, GPIO.OUT)
        GPIO.setup(self.valvePin, GPIO.LOW)

    def close(self):
        GPIO.setup(self.valvePin, GPIO.LOW)

    def open(self, sec):
        GPIO.output(self.valvePin, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(self.valvePin, GPIO.LOW)

#val = Valve(22)
#while True:
    #print "Open"
    #val.open(5)
    #print "Close"
    #time.sleep(5)
