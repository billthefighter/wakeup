# test to debug sparkle class in pure python before moving to matrix
import random
import time
import atexit
from PIL import Image
from PIL import ImageDraw
#from rgbmatrix import Adafruit_RGBmatrix

#global inits
starno			=10 #number of stars
fps            = 4  # Scrolling speed (ish)
prevTime    = time.time()
width          = 32  # Matrix size (pixels) -- change for different matrix
height         = 32  # types (incl. tiling).  Other code may need tweaks.
image       = Image.new('RGB', (32, 32))
draw        = ImageDraw.Draw(image)
#matrix = Adafruit_RGBmatrix(32, 1)

def clearOnExit():
	matrix.Clear()

atexit.register(clearOnExit)

class star:
	def __init__(self):
		self.x = random.randint(0, 32)
		self.y = random.randint(0, 32)
		self.sp = random.randint(0,16)
		self.toggle = random.randint(0,1)

	def sparkle(self):
		if self.sp >= 0 and self.sp < 16 and self.toggle == 0:
			self.sp += 1
			pass
		elif self.sp == 16:
			self.toggle = 1
			self.sp -= 1
		elif self.toggle == 1 and self.sp > 0:
			self.sp -= 1
	def newstar(self):
		self.x = random.randint(0, 32)
		self.y = random.randint(0, 32)
		self.sp = 0
		self.toggle = 0
	def draw(self):
		x = self.x
		y = self.y
		sp = self.sp
		draw.point([x,y], fill = (15*sp, 15*sp, 15*sp))




#generate initial list of stars
starlist = [] 
for i in xrange(0,starno):
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
	 			starlist[i].newstar()
	 			#NOTE NOTE NOTE Need to make sure to newstar the newly appended star or it will just pop on at some random value
	 			pass
	 	else:
	 			starlist[i].sparkle()
	 			pass	
	 	pass
	#check how many stars there are in the list, if there's less than 10 then make a new star
	if len(starlist) < starno:
		starlist.append(star())
		starlist[i].newstar()
		print starlist
		#NOTE NOTE NOTE Need to make sure to newstar the newly appended star or it will just pop on at some random value
	#print starlist[0].x,starlist[0].y,starlist[0].sp,starlist[0].toggle
	#for i in xrange(1,10):
	#	print starlist[i].x,starlist[i].y,starlist[i].sp,starlist[i].toggle
	#	pass

	#OH SHIT START DRAWING STUFF FOR REAL
	# Clear background
	draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0))

	#call draw for all the shit
	for x in starlist: 
		x.draw()
		pass



	#timer
	currentTime = time.time()
	#print "current time"
	#print currentTime
	#print "current - prev"
	#print currentTime - prevTime
	#print prevTime
	print "First Half:",1.0/fps,"second half:",(currentTime - prevTime)
	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
	print "timeDelta"
	print timeDelta
	if(timeDelta > 0.00):
		time.sleep(timeDelta)
		print "sleeping"
		prevTime = time.time()
	#prevTime = currentTime

	# Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)
	
	poop += 1	#increment poop
	#print 'length of newstar is:'
	#print len(starlist)
	pass

matrix.Clear()


#