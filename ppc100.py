import PIL
from PIL import Image, ImageDraw
from operator import itemgetter
print "hi"
step=100
xparts=25
yparts=1000//xparts
image= Image.new('RGB',(xparts*100,yparts*100))
test= Image.new('RGB',(xparts*100,yparts*100))
row=0
column=0
forsorting=[]
for i in xrange(0,999):
	timage=Image.open("/root/ppc100/"+str(i)+".png")
	pix=timage.load()
	imarray=[]
	imarray.append(pix[0,0][0])
	imarray.append(pix[0,0][1])
	imarray.append(pix[0,0][2])
	imarray.append(pix[0,0][2]+pix[0,0][1]+pix[0,0][0])
	imarray.append(i)
	forsorting.append(imarray)
	print forsorting[i]
	row=row+step #i//xparts*step

	if i%xparts==0:
		column=column+step
		row=0
	#image.paste(timage,(row,column))
#forsorting.sort()
ready=sorted(forsorting, key=itemgetter(3))
#ready=sorted(ready, key=itemgetter(0))
#ready=sorted(ready, key=itemgetter(4))
imageName=0
row=0
column=0
res=[]
for i in xrange(0,999):
	print ready[i]
	res.append(forsorting[i][3])
	#print forsorting[i][3]

for i in xrange(0,999):	
	timage=Image.open("/root/ppc100/"+str(ready[i][4])+".png")
	row=row+step #i//xparts*step

	if i%xparts==0:
		column=column+step
		row=0
	image.paste(timage,(row,column))

print "end"

image.save("1000.png","PNG")
