import PIL

from PIL import Image, ImageDraw

from operator import itemgetter

print "hi"


def distance(r1,g1,b1,r2,g2,b2):
    return abs(r1-r2)+abs(g1-g2)+abs(b1-b2)

def isIn(a,b):
	for x in xrange(0,len(a)):
		if a[x]==b:
			return True

	return False
step=100


xparts=25
yparts=1000//xparts


firstImageName="38.png"

image= Image.new('RGB',(xparts*100,yparts*100))


test= Image.new('RGB',(xparts*100,yparts*100))
row=0
column=0

forsorting=[]
timage=[]

for i in xrange(0,999):
	timage.append(Image.open("/root/ppc100/"+str(i)+".png"))
	pix=timage[i].load()
	imarray=[]
	imarray.append(pix[0,0][0])
	imarray.append(pix[0,0][1])
	imarray.append(pix[0,0][2])
	imarray.append(pix[99,99][0]) # 3
	imarray.append(pix[99,99][1]) # 4
	imarray.append(pix[99,99][2]) # 5
	imarray.append(i)


	forsorting.append(imarray)
	#print forsorting[i]
	row=row+step #i//xparts*step

	if i%xparts==0:
		column=column+step
		row=0
	
	#image.paste(timage,(row,column))
row=0
column=0
lastindex=38
used=[]
for i in xrange(0,999):
	used.append(lastindex)
	image.paste(timage[lastindex],(row,column))
	mind=1000
	index=0
	print i


	for j in xrange(0,999):
		if isIn(used,j):
			continue
		d=distance(forsorting[lastindex][3],forsorting[lastindex][4],forsorting[lastindex][5],forsorting[j][0],forsorting[j][1],forsorting[j][2])
		if d<mind:
			mind=d
			index=j
	lastindex=index
	print mind
	row=row+step
	if i%xparts==0:
		column=column+step
		row=0


print "end"

image.save("1001.png","PNG")