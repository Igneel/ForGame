
import socket

def mysend(sock, msg):
  sock.send(msg.encode("utf-8"))
  #sock.send(msg)

def myreceive(sock):
  data = b""
  data = sock.recv(10)
  #while tmp:
  #    data += tmp
  #    tmp = sock.recv(1)
  return data.decode("utf-8")
  
# https://docs.python.org/3/howto/sockets.html
# create an INET, STREAMing socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port port
sock = socket.socket()
port=11081
judgeIP="109.233.56.90"
sock.connect( (judgeIP, port))
print("connected")
data=myreceive(sock)
print(data)
testdata="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
exploit="admin\n"
mysend(sock,exploit)
data=myreceive(sock)
print(data)
