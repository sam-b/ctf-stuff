import socket

def get_prime(num):
	next = num + 1
	while True:
		if is_prime(next):
			return next
		next = next + 1

from math import sqrt; from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

if __name__ == "__main__":
	s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
	#now connect to the web server on port 80
	# - the normal http port
	s.connect(("188.166.133.53", 11059))
	while True:
		data = s.recv(2048)
		print data
		start = data.find("after") + 6
		num = data[start:]
		num = int(num[:-2])
		print num
		s.send(str(get_prime(num)) + "\n")
		print s.recv(2048)
