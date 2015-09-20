# test to debug sparkle class in pure python before moving to matrix
import random

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
			self.toggle == 1
			self.sp -= 1
		elif self.toggle == 1 and self.sp > 0:
			self.sp -= 1
	def joggle():
		self.x = random.randint(0, 32)
		self.y = random.randint(0, 32)
		self.sp = random.randint(0,8)
		self.toggle = random.randint(0,1)



#generate initial list of stars
starlist = [] 
for i in xrange(0,10):
	starlist.append(star())
	print starlist[i].x,starlist[i].y,starlist[i].sp,starlist[i].toggle
	pass


# #loop through stars
# for i in xrange(starlist):
#  	if starlist[i].sp = 0 and fartarray[i].toggle = 1: #if it's in the list and has completed sparkling, this condition will be true
#  			fartarray.pop(i)
#  			pass
#  	if fartarray[i].sp != 0 :
#  			fartarray.sparkle()
#  			pass	
#  	pass
# #check how many stars there are in the list, if there's less than 10 then make a new star
# if len(starlist) < 10:



#