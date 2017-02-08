import socket

def readUntil(s,stop):
  res=""
  temp=s.recv(1)
  while temp!=stop:
  	res=res+temp
  	temp=s.recv(1)

  return res


s=socket.socket()

s.connect(("195.154.53.62", 7412))

#s.send(b'1')

while 1:
	data=readUntil(s,b'\n')
	#print(data.decode("UTF-8"))
	data=readUntil(s,b'\n')
	#print(data.decode("UTF-8"))
	data=readUntil(s,b'\n')
	#print(data.decode("UTF-8"))
	s.send(b'2\n')
	data=readUntil(s,b'\n')
	print(data.decode("UTF-8"))


