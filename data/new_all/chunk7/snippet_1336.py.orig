#Source: https://stackoverflow.com/questions/39652480/pillow-image-typeerror-an-integer-is-required-got-type-tuple
from PIL import Image, ImageChops,ImageDraw,ImageFilter
import math
import glob
import os.path
from os import  listdir;
import numpy


image_list = []

redPixels = []
greenPixels = []
bluePixels = []

for filename in glob.glob(r"C:\Users\Elias\Desktop\Proj1\images\*.png"):
    im = Image.open(filename)
    image_list.append(im)
im = Image.open(open(r"C:\Users\Elias\Desktop\Proj1\images\1.png",'rb'))
width, height = im.size
print(height)
print (width)

result = Image.new('RGB', (width,height))
newpix = result.load()
for x in range (width):
    for y in range (height):
        for z in (image_list):
            red  = z.getpixel((x,y))
            blue = z.getpixel((x,y))
            green = z.getpixel((x,y))

            redPixels.append(red)
            greenPixels.append(green)
            bluePixels.append(blue)
        red = sorted(redPixels)
        blue = sorted(bluePixels)
        green = sorted(greenPixels)

        mid = int( (len(image_list)+1)/2)-1

        newRed = redPixels[mid]
        newBlue = bluePixels[mid]
        newGreen = greenPixels[mid]
        newpix[x,y] = (newRed,newGreen,newBlue)

result.save("Stacked.png")