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

fps            = 8  # Scrolling speed (ish)
prevTime       = time.time()
width          = 32  # Matrix size (pixels) -- change for different matrix
height         = 32  # types (incl. tiling).  Other code may need tweaks.

# ------------Image Block---------------------
image       = Image.new('RGB', (32, 32))
draw        = ImageDraw.Draw(image)
matrix      = Adafruit_RGBmatrix(32, 2)
atexit.register(clearOnExit)

def clearOnExit():
	matrix.Clear()
# ------------Image Block---------------------

def ratecalcsin(step,scale):
	int(round(255*math.sin(math.radians(90*(step/scale)))))



class sun:
	def __init__(self,panelno):
		self.color = [0,0,0]
		self.panel = panelno
		self.location = [0,0,0,0]
		self.step = 0 #so each sun can track its own state
		self.maxstep = 255
		#this bit is basically a conviluted way to initialize where the sun is (if it's sun 0 spawn in panel 0, ect)
		if self.panel == 0:
			self.location = [0,0,32,32]
		elif self.panel == 1:
			self.location = [0,33,64,64]
		else:
			self.location = [0,0,0,0]
	def colorinc(self):
		if self.step == self.maxstep:
			pass
		elif self.step <= 0 and self.step > 255:
			self.step += 1
			#this whole line is basically to try to make a non-linear scale of light
			#intent is to go from a steeper change value at the beginning to a more gradual one later
			#super conviluted but it's the best I could think of at the time
			#colorval = int(round(255*math.sin(math.radians((90*(self.step/self.maxstep))))))
			# this is a shitty hack to make it get gradually more yellow
			colorvalr = ratecalcsin(self.step,self.maxstep)
			colorvalg = self.step/self.maxstep*255
			self.color = [colorvalr,colorvalb,0]
	def draw(self):
		draw.rectangle((self.location), fill=(self.color))


#---------------Start Program--------------------------------------------------------------------



sunrise_lw = sun(0)
sunrise_es = sun(1)

state = 4
while state == 4:
# ------------Image Block---------------------
	# Clear background
	draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0))
# ------------Image Block---------------------
	sunrise_lw.colorinc()
	sunrise_lw.draw()


	sunrise_es.colorinc()
	sunrise_es.draw()

	

#Timing 
	print "First Half:",1.0/fps,"second half:",(currentTime - prevTime)
	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
	print "timeDelta"
	print timeDelta
	if(timeDelta > 0.00):
		time.sleep(timeDelta)
		print "sleeping"
		prevTime = time.time()

# ------------Image Block---------------------
	# Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)
# ------------Image Block---------------------