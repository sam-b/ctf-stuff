def xor(a,b):
    return a ^ b

def encode(eq):
    print eq
    out = []
    for c in eq:
        q = bin(xor(ord(c),(2<<4))).lstrip("0b")
        print q
        q = "0" * ((2<<2)-len(q)) + q
        out.append(q)
    b = ''.join(out)
    print b
    pr = []
    for x in range(0,len(b),2):
        c = chr(int(b[x:x+2],2)+51)
        pr.append(c)
    s = '.'.join(pr)
    print s
    return s

def decode(eq):
    out = ''
    pr = eq.split('.')
    tmp = []
    for i in pr:
        b = bin(ord(i) - 51).lstrip("0b")
        tmp.append(("0" * (2 - len(b))) + str(b))
    tmp = ''.join(tmp)
    chars = [tmp[i:i+8] for i in range(0, len(tmp), 8)]
    for i in chars:
        out += chr(int(i,2) ^ 2<<4)
    return out
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
    s.connect(("188.166.133.53", 11071))
    while True:
        data = s.recv(1024)
        print data
        if data != '':
            line = data.split('\n')
            for l in line:
                if l.find(':') != -1:
                    parsed = l[l.find(':') + 2:]
                    print parsed
                    eq = decode(parsed)
                    print eq
                    x = get_x(eq)
                    print x
                    s.send(encode(str(x)) + '\n')