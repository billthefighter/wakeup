# test to debug sparkle class in pure python before moving to matrix
import random
import time
import atexit
import Image
import ImageDraw
from rgbmatrix import Adafruit_RGBmatrix

#global inits
fps            = 2  # Scrolling speed (ish)
prevTime    = 0.0
image       = Image.new('L', (width, height))
draw        = ImageDraw.Draw(image)

def clearOnExit():
	matrix.Clear()

atexit.register(clearOnExit)

class star:
	def __init__(self):
		self.x = random.randint(0, 32)
		self.y = random.randint(0, 32)
		self.sp = random.randint(0,8)
		self.toggle = random.randint(0,1)

	def sparkle(self):
		if self.sp >= 0 and self.sp < 8 and self.toggle == 0:
			self.sp += 1
			pass
		elif self.sp == 8:
			self.toggle = 1
			self.sp -= 1
		elif self.toggle == 1 and self.sp > 0:
			self.sp -= 1
	def newstar():
		self.x = random.randint(0, 32)
		self.y = random.randint(0, 32)
		self.sp = 0
		self.toggle = 0



#generate initial list of stars
starlist = [] 
for i in xrange(0,10):
	starlist.append(star())
	#print starlist[i].x,starlist[i].y,starlist[i].sp,starlist[i].toggle
	pass

poop = 0
while poop < 10:
	#print poop
	#print 'starting starloop'
	#loop through stars
	for i in xrange(len(starlist)):
	 	if starlist[i].sp == 0 and starlist[i].toggle == 1: #if it's in the list and has completed sparkling, this condition will be true
	 			starlist.pop(i)
	 			starlist.append(star()) #since we might have popped a star off the list, the loop can fail if the list suddenly becomes smaller
	 			#NOTE NOTE NOTE Need to make sure to newstar the newly appended star or it will just pop on at some random value
	 			pass
	 	else:
	 			starlist[i].sparkle()
	 			pass	
	 	pass
	#check how many stars there are in the list, if there's less than 10 then make a new star
	if len(starlist) < 10:
		starlist.append(star())
		#NOTE NOTE NOTE Need to make sure to newstar the newly appended star or it will just pop on at some random value
	print starlist[0].x,starlist[0].y,starlist[0].sp,starlist[0].toggle
	#for i in xrange(1,10):
	#	print starlist[i].x,starlist[i].y,starlist[i].sp,starlist[i].toggle
	#	pass
	poop += 1	
	currentTime = time.time()
	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
	if(timeDelta > 0.0):
		time.sleep(timeDelta)
	prevTime = currentTime

	# Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)
	pass



#