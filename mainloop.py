#Alarm clock thing

#init variables

#init classes
import time
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

# Flash screen red, green, blue (packed color values)
matrix.Fill(0xFF0000)
time.sleep(1.0)
matrix.Fill(0x00FF00)
time.sleep(1.0)
matrix.Fill(0x0000FF)
time.sleep(1.0)

#init current time

#state 0: off, wait for input
	#check for if alarm is supposed to go off
	#check if button has been pressed
		#check mode state
		#go to alarm set
		#go to nighttime
		#go to sexytime
		#go to stocktick
#state 1: Alarm Set
	#exits after time for alarm is set, goes to off state
	#also exits after timeout
#state 2: Nighttime star sparkle mode
	#ends with timeout
	#ends with button, back to state 0
#state 3: Sexytime
	#ends with timeout
	#ends with button, back to state 0
#State 4: Wake Up Time
	#create circles of increasingly brighter light until wakeup time, then 
	#exits on button press to stocktick
	#exits on timeout
#state5: Stocktick
	#
