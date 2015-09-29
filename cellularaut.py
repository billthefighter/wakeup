from PIL import Image
from PIL import ImageOps
import random
#from rgbmatrix import Adafruit_RGBmatrix
import atexit
#define inputs
#runrule = 3

def step(a, rule, k=2, r=1):
    nbrs = [a[c:] + a[:c] for c in range(-r, r+1, 1)]
    l = []
    for t in apply(zip, nbrs):
        result = 0
        for i in t:
            result = (result * k) + i
        l.append(result)
    return [((rule / (k ** v)) % k) for v in l]

def basicRun(rule, steps, stepper, seed=[1], k=2, r=1):
    print steps
    seed=[1]
    for x in xrange(0,steps):
        seed.append(random.randint(0,1))
        pass
    #seed = ([0] * steps) + seed + ([0] * steps)
    #print seed
    result = seed[:]
    for i in range(steps):
        seed = stepper(seed, rule, k=k, r=r)
        result += seed[:]
    return result, (len(seed), steps + 1)

def showResult(result, dims, k=2):
    i = Image.new("RGB", dims)
    i.putdata(result, (255 / (k - 1)))
    i = i.crop(i.getbbox())
    i = ImageOps.invert(i)
    i.load()
    i.show()
    matrix.SetImage(image.im.id, 0, 0)

def runTest(runrule,lines):
    result, dims = basicRun(runrule, lines, step)
    showResult(result, dims)

if __name__ == "__main__":
    runTest(90,32)
    #for x in [30,90,54,110]:
        #runTest(x,32)
        #pass
    