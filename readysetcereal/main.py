import MySQLdb
import time

db = MySQLdb.connect(host="leaflr.com",
                     user="rsc",
                     passwd="g00dbyeworld!",
                     db="rsc")

cur = db.cursor()

from temp import Temperature
from light import LightSensor
from valve import Valve
from servo import Servo

temp = Temperature()
l1 = LightSensor(17)
val = Valve(22)
val.close()
s1 = Servo()

def bowlPresent():
  x = 0
  while(x < 20):
    if(l1.visible()):
      return False
    x = x+1

  return True

def status():
  tC = temp.readTempC()
  print "Celcius " + str(tC)
  tF = temp.readTempF()
  print "Farenheight " + str(tF)
  milkTemp = tF
  cur.execute("UPDATE current_status SET milk_temp=%s" % (milkTemp))
  db.commit()
  #print "Light: " + str( l1.visible() )
    

while True:

  print "Checking Status..."
  status()
  time.sleep(2)

  print "Checking for Bowl..."
  if( bowlPresent() ):
    print "Bowl Present."
    #turn on Big Red LED
    
    #get most recent pending order
    cur.execute("SELECT * FROM pending_orders WHERE status='Pending' ORDER BY time_ordered ASC LIMIT 1;")
    for row in cur.fetchall():
      orderId = row[0]
      timeOrdered = row[1]
      c1 = row[2]
      c2 = row[3]
      c3 = row[4]
      
      milk = row[5]
      spoon = row[6]

      print "Now Serving Order #" + str(orderId)
      #print c1
      #print c2
      #print c3

      #print milk
      #print spoon

      cur.execute("UPDATE pending_orders SET status='serving' WHERE order_id=%s" % (orderId))
      db.commit()
      #print "Updated Mysql Table"

      #dispense spoon
      if( spoon == 1):
        print "Here come's a spoon..."
        s1.releaseSpoon()
        time.sleep(1)

      #dispense cereal 1
      if( c1 > 0 ):
        print str(c1) + "% Cereal 1"
        time.sleep(1)
        #motor1.turn( delay, int(500 * (c1/100.0)))
      #dispense cereal 2
      if( c2 > 0 ):
        print str(c2) + "% Cereal 2"
        time.sleep(1)
        #motor2.turn( delay, int(500 * (c2/100.0)))
      #dispense cereal 3
      if( c3 > 0 ):
        print str(c3) + "% Cereal 3"
        time.sleep(1)
        #motor3.turn( delay, int(500 * (c3/100.0)))

      #dispense milk
      if( milk > 0):
        val.open( milk )
        print "Milk goodness :) [" + str(milk) + " oz]"
        time.sleep(2)
    
    #Turn on Big Green LED
      cur.execute("INSERT INTO completed_orders VALUES (%s, NOW(), NOW(), %s, %s, %s, %s, %s)" % (orderId, c1, c2, c3, milk, spoon))
      cur.execute("UPDATE pending_orders SET status='Complete' WHERE order_id=%s" % (orderId))
      cur.execute("DELETE FROM pending_orders WHERE order_id=%s" % (orderId))
      db.commit()
    #wait for bowl to be picked up
      print "Please Pick Up Bowl"
      while( l1.visible() == False ):
        time.sleep(1)
  else:
    print "No Bowl."
    time.sleep(2)
