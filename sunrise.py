# test to debug sparkle class in pure python before moving to matrix
import random
import time
import atexit
import math
import numpy
from PIL import Image
from PIL import ImageDraw
from rgbmatrix import Adafruit_RGBmatrix

fps            = 8  # Scrolling speed (ish)
prevTime    = time.time()
width          = 32  # Matrix size (pixels) -- change for different matrix
height         = 32  # types (incl. tiling).  Other code may need tweaks.
image       = Image.new('RGB', (32, 32))
draw        = ImageDraw.Draw(image)
matrix = Adafruit_RGBmatrix(32, 1)

def clearOnExit():
	matrix.Clear()

atexit.register(clearOnExit)

class sun:
	def __init__(self,panelno):#when creating a new star, pass panel number to it so it knows which panel the sun should spawn in
		self.color = [0,0,0]
		self.panel = panelno
		self.location = [0,0,0,0]
		#this bit is basically a conviluted way to 
		if self.panel == 0:
			self.location = [0,0,32,32]
		elif == 1:
			self.location = [0,33,64,64]
		else
			self.location = [0,0,0,0]
	
	def draw(self):
		.color




#OH SHIT START DRAWING STUFF FOR REAL
	# Clear background
	draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0))

	#call draw for all the shit
	for x in starlist: 
		x.draw()
		pass

#Timing 
	print "First Half:",1.0/fps,"second half:",(currentTime - prevTime)
	timeDelta   = (1.0 / fps) - (currentTime - prevTime)
	print "timeDelta"
	print timeDelta
	if(timeDelta > 0.00):
		time.sleep(timeDelta)
		print "sleeping"
		prevTime = time.time()


	# Offscreen buffer is copied to screen
	matrix.SetImage(image.im.id, 0, 0)