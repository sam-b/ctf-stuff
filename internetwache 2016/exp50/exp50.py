import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("188.166.133.53", 12037))
print s.recv(1024)
s.send("aaaaaaaaaa\nAAAAAAAAAA")
print s.recv(1024)