import math

x = 45
pickles = math.radians((90-x))
poop = int(round(255*math.sin(math.radians((90-x)))))
print pickles 
print poop

farts =[]

for x in xrange(1,90):
	farts.append(int(round(255*math.cos(math.radians((90-x))))))
	pass

print farts

