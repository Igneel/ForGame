import socket
import math
def read(d,stop):
  res=b""
  while 1:
    temp=d.recv(1)
    if temp==stop:
      return res
    else:
      res=res+temp

s=socket.socket()
s.connect(("195.154.53.62", 1337))

data=read(s,b':')

def calcit(a,op,b):
  a=int(a)
  b=int(b)
  if op == "*":
   return a*b
  if op =="/":
   return math.floor(a/b)
  if op =="+":
   return a+b
  if op =="-":
   return a-b
  if op =="%":
   return a%b
  return 0

while 1:
  data=read(s,b'\n')
  data=read(s,b'\n')
  data=data.decode("UTF-8")
  print(data)
  m=str.split(data)
  if data[0]=="C":
   print(read(s,b'\n'))
   print(read(s,b'\n'))
   print(s.recv(1024))
   
  ans = calcit(m[0],m[1],m[2])
  print(ans)
  ans=str(ans)+"\n"
  s.send(ans.encode("UTF-8"))
