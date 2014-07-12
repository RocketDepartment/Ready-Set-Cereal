import time

from light import LightSensor
from stepper3 import Stepper

l1 = LightSensor(17)
motorA = Stepper(14,15,18,23)

def bowlPresent():
  x = 0
  while(x < 20):
    if(l1.visible()):
      return False
    x = x+1

  return True

while True:

  print "Checking for Bowl..."
  #if( bowlPresent() ):
  print "Bowl Present."

  print "Cereal 1"
  time.sleep(1)
  motorA.rotate( 25 )
  time.sleep(60)    
  print "Please Pick Up Bowl"
  #while( l1.visible() == False ):
        #time.sleep(1)
  #else:
    #print "No Bowl."
    #time.sleep(2)
