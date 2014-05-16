import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)

delay = (10 / 1000.0)

class Stepper:
    def __init__(self, pinA, pinB, pinC, pinD):
        self.coil_A_1_pin = pinA
        self.coil_A_2_pin = pinB
        self.coil_B_1_pin = pinC
        self.coil_B_2_pin = pinD

        GPIO.setup(self.coil_A_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_A_2_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_1_pin, GPIO.OUT)
        GPIO.setup(self.coil_B_2_pin, GPIO.OUT)

    def rotate(self, steps):  
        for i in range(0, steps):
            self.setStep(1, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 1, 0, 1)
            time.sleep(delay)
            self.setStep(0, 1, 1, 0)
            time.sleep(delay)
            self.setStep(1, 0, 1, 0)
            time.sleep(delay)
    
    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.coil_A_1_pin, w1)
        GPIO.output(self.coil_A_2_pin, w2)
        GPIO.output(self.coil_B_1_pin, w3)
        GPIO.output(self.coil_B_2_pin, w4)
