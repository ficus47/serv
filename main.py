import socket as sk

x = sk.gethostbyname(sk.gethostname())
print(x)

sock = sk.socket()
sock.bind((x,8080))

sock.listen(5)

while True:
  
