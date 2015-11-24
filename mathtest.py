import math

x = 45
pickles = math.radians((90-x))
poop = int(round(255*math.sin(math.radians((90-x)))))
#print pickles 
#print poop

# farts =[]

# for x in xrange(1,90):
# 	farts.append(int(round(255*math.cos(math.radians((90-x))))))
# 	pass

# print farts


def ratecalcsin(step,scale):
	return int(round(255*math.sin(math.radians(90*(step/scale)))))

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
		elif self.step >= 0 and self.step < 255:
			self.step += 1
			#this whole line is basically to try to make a non-linear scale of light
			#intent is to go from a steeper change value at the beginning to a more gradual one later
			#super conviluted but it's the best I could think of at the time
			#colorval = int(round(255*math.sin(math.radians((90*(self.step/self.maxstep))))))
			# this is a shitty hack to make it get gradually more yellow
			colorvalr = ratecalcsin(self.step,self.maxstep)
			print colorvalr
			colorvalg = self.step/self.maxstep*255
			self.color = [colorvalr,colorvalg,0]
			print self.color

print ratecalcsin(3,25.0)

sunrise_lw = sun(0)
sunrise_es = sun(1)

print sunrise_es.location
