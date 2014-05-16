#!/usr/bin/env python
 
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
 
import RPi.GPIO as GPIO, time, os

GPIO.setmode(GPIO.BCM)

class LightSensor(object):

   def __init__(self, pin):
      self.RCpin = pin
 
   def visible(self):
        reading = 0
	GPIO.setup(self.RCpin, GPIO.OUT)
        GPIO.output(self.RCpin, GPIO.LOW)
        time.sleep(0.1)

	GPIO.setup(self.RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while(GPIO.input(self.RCpin) == GPIO.LOW):
                reading += 1
                print reading
        if reading < 10:
           return True
        else:
           return False
 
#lightsensor = LightSensor(17)
#while True:
   #print lightsensor.visible()
