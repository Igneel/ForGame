import PIL

from PIL import Image, ImageDraw

print "hi"

image= Image.open("/root/300-0-0-0-0.png")




for x in xrange(1,2000):
	image.crop(0,0+x*100,2000,100+x*100).save(str(i)+"wow.png","PNG")
