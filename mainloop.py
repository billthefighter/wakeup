#Alarm clock thing
import time
import Image
import ImageDraw
from rgbmatrix import Adafruit_RGBmatrix
#init variables
width = 32
height = 32
image = Image.new("1", (width, height)) # Can be larger than matrix if wanted!!
draw  = ImageDraw.Draw(image)    # Declare Draw instance before prims
# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)
image       = Image.new('L', (width, height))
draw        = ImageDraw.Draw(image)
currentTime = 0.0
prevTime    = 0.0
#init classes
class star:
	def __init__(self, x, y, sp):
		self.x = x
		self.y = y
		self.sp = sp #sparkle value

	def sparkle(self):
		if self.sp == 0:
			self.sp += 1
			pass
		if self.sp > 0 and self.sp < 8:
			self.sp += 1
			pass



# Flash screen red, green, blue (packed color values)
matrix.Fill(0xFF0000)
time.sleep(1.0)
matrix.Fill(0x00FF00)
time.sleep(1.0)
matrix.Fill(0x0000FF)
time.sleep(1.0)
matrix.Clear()

draw.point(xy, options)
draw.ellipse(xy, options)

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

	# Initialization done; loop forever ------------------------------------------
while True:

	# Clear background
	draw.rectangle((0, 0, width, height), fill=(0, 0, 0))

	for t in tileList:
		if t.x < width:        # Draw tile if onscreen
			t.draw()
		t.x -= 1               # Move left 1 pixel
		if(t.x <= -tileWidth): # Off left edge?
			t.x += tileWidth * tilesAcross     # Move off right &
			t.p  = predictList[nextPrediction] # assign prediction
			nextPrediction += 1                # Cycle predictions
			if nextPrediction >= len(predictList):
				nextPrediction = 0

	# Try to keep timing uniform-ish; rather than sleeping a fixed time,
	# interval since last frame is calculated, the gap time between this
	# and desired frames/sec determines sleep time...occasionally if busy
	# (e.g. polling server) there'll be no sleep at all.
	currentTime = time.time()
	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
	if(timeDelta > 0.0):
		time.sleep(timeDelta)
	prevTime = currentTime

	# Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)
#state 3: Sexytime
	#ends with timeout
	#ends with button, back to state 0
#State 4: Wake Up Time
	#create circles of increasingly brighter light until wakeup time, then 
	#exits on button press to stocktick
	#exits on timeout
#state5: Stocktick
#State6: Time Display
#state7: Reading light 
	#
