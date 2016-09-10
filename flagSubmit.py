
import socket

def mysend(sock, msg):
  sock.send(msg.encode("utf-8"))

def myreceive(sock):
  data = b""
  tmp = conn.recv(1024)
  while tmp:
      data += tmp
      tmp = conn.recv(1024)
  return data.decode("utf-8")
  
# https://docs.python.org/3/howto/sockets.html
# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port port

sock = socket.socket()
port=80
judgeIP="192.168.2.69"
sock.connect( (judgeIP, port))

mysend(sock,flag)
data=myreceive(sock)

