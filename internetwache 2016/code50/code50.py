#188.166.133.53:11027
import socket

def get_x(equa):
	equa = equa.replace('=','==')
	for i in range(-10000,10000):
		out = eval(equa.replace('x',str(i)))
		if out != False:
			print equa
			print 'x = ' + str(i)
			return i

if __name__ == "__main__":
	s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
	#now connect to the web server on port 80
	# - the normal http port
	s.connect(("188.166.133.53", 11027))
	while True:
		data = s.recv(1024)
		while data.find(':') == -1:
			print data
			data = s.recv(1024)
		start = data.find(':') + 2
		print data
		num = get_x(data[start:])
		print num
		s.send(str(num) + "\n")
		#print s.recv(1024)
