# Servo Control
import time

class Servo(object):

   def __init__(self):
        self.set("delayed", "0")
	self.set("mode", "servo")
	self.set("servo_max", "180")
	self.set("active", "1")

	self.delay_period = 0.01

   def set(self, property, value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
		f.write(value)
		f.close()	
	except:
		print("Error writing to: " + property + " value: " + value)
 
   def setServo(self, angle):
	self.set("servo", str(angle))
	

   def releaseSpoon(self):

        self.set("active","1")

	for angle in range(0, 180):
           self.setServo(angle)
	   time.sleep(self.delay_period)

	for angle in range(0, 180):
           self.setServo(180-angle)
	   time.sleep(self.delay_period)

	self.set("active","0")

#while True:
   #s1 = Servo()
   #s1.releaseSpoon()
   #print "Spoon!"
   #time.sleep(1)
