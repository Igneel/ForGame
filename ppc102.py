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

for i in xrange(0,1000):
	timage.append(Image.open("/root/ppc100/"+str(i)+".png"))
	pix=timage[i].load()
	imarray=[]
	imarray.append(pix[0,0][0]) #0
	imarray.append(pix[0,0][1]) # 1
	imarray.append(pix[0,0][2]) # 2
	imarray.append(pix[99,99][0]) # 3
	imarray.append(pix[99,99][1]) # 4
	imarray.append(pix[99,99][2]) # 5
	imarray.append(pix[0,99][0]) # 6
	imarray.append(pix[0,99][1]) # 7
	imarray.append(pix[0,99][2]) # 8
	imarray.append(pix[99,0][0]) # 9
	imarray.append(pix[99,0][1]) # 10
	imarray.append(pix[99,0][2]) # 11

	# 0,0  99,0
	# 99,99 0,99 
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
for i in xrange(0,1000):
	used.append(lastindex)
	image.paste(timage[lastindex],(row,column))
	mind=1000
	index=0
	print i


	for j in xrange(0,1000):
		if isIn(used,j):
			continue
		d=distance(forsorting[lastindex][9],forsorting[lastindex][10],forsorting[lastindex][11],forsorting[j][0],forsorting[j][1],forsorting[j][2])
		d=d+distance(forsorting[lastindex][3],forsorting[lastindex][4],forsorting[lastindex][5],forsorting[j][6],forsorting[j][7],forsorting[j][8])
		if d<mind:
			mind=d
			index=j
	lastindex=index
	print mind
	row=row+step
	if i%xparts==0 and i!=0:
		column=column+step
		row=0


print "end"

image.save("1003.png","PNG")