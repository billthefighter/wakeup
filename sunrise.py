# test to debug sparkle class in pure python before moving to matrix
import random
import time
import atexit
import math
import numpy
from PIL import Image
from PIL import ImageDraw

# ------------Image Block---------------------
from rgbmatrix import Adafruit_RGBmatrix
# ------------Image Block---------------------

fps            = 8 # Scrolling speed (ish)
prevTime       = time.time()
width          = 32  # Matrix size (pixels) -- change for different matrix
height         = 32  # types (incl. tiling).  Other code may need tweaks.

# ------------Image Block---------------------
image       = Image.new('RGB', (64, 32))
draw        = ImageDraw.Draw(image)
matrix      = Adafruit_RGBmatrix(32, 2)


def clearOnExit():
	matrix.Clear()
atexit.register(clearOnExit)
# ------------Image Block---------------------

def ratecalcsin(step,scale):
	return int(round(255*math.sin(math.radians(90*(step/scale)))))



class sun:
	def __init__(self,panelno):
		self.color = (0,0,0)
		self.panel = panelno
		self.location = [0,0,0,0]
		self.step = 0 #so each sun can track its own state
		self.maxstep = 255
		#this bit is basically a conviluted way to initialize where the sun is (if it's sun 0 spawn in panel 0, ect)
		if self.panel == 0:
			self.location = [0,0,31,31]
		elif self.panel == 1:
			self.location = [32,0,64,32]
		else:
			self.location = [0,0,0,0]
	def colorinc(self):
		if self.step == self.maxstep:
			pass
		elif self.step >= 0 and self.step < self.maxstep:
			self.step += 1
			#this whole line is basically to try to make a non-linear scale of light
			#intent is to go from a steeper change value at the beginning to a more gradual one later
			#super conviluted but it's the best I could think of at the time
			#colorval = int(round(255*math.sin(math.radians((90*(self.step/self.maxstep))))))
			# this is a shitty hack to make it get gradually more yellow
			colorvalr = ratecalcsin(float(self.step),self.maxstep)
			#print colorvalr
			colorvalg = int(float(self.step)/self.maxstep*255)
			if self.step > int(float(self.maxstep)/2):
				colorvalb = 2*int(float(self.step-int(float(self.maxstep)/2))/self.maxstep*255)
			else: 
				colorvalb = 0
			self.color = (colorvalr,colorvalg,colorvalb)
			#print self.color
	def draw(self):
		draw.rectangle((self.location), fill=self.color)


#---------------Start Program--------------------------------------------------------------------



sunrise_lw = sun(0)
sunrise_es = sun(1)

#state = 4
#while state == 4:
poop = 0
while poop < 300:
# ------------Image Block---------------------
	# Clear background
	#draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0))
# ------------Image Block---------------------
	
	poop += 1
	#print poop
	sunrise_lw.colorinc()
	sunrise_lw.draw()
	#print sunrise_lw.color

	sunrise_es.colorinc()
	sunrise_es.draw()

	

#Timing 
	currentTime = time.time()
	#print "First Half:",1.0/fps,"second half:",(currentTime - prevTime)
	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
	#print "timeDelta"
	#print timeDelta
	if(timeDelta > 0.00):
		time.sleep(timeDelta)
		#print "sleeping"
		prevTime = time.time()

# ------------Image Block---------------------
	## Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)
# ------------Image Block---------------------