from stepper3 import Stepper

motorA = Stepper(14,15,18,23)
motorB = Stepper(24,25,8,7)
motorC = Stepper(11,9,10,22)

while True:
  steps = raw_input("How many steps for Motor A? ")
  motorA.rotate(int(steps))

  steps = raw_input("How many steps for Motor B? ")
  motorB.rotate(int(steps))

  steps = raw_input("How many steps for Motor C? ")
  motorC.rotate(int(steps))


  
