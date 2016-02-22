from z3 import *
import sys

if __name__ == "__main__":
	x = BitVec('x', 32)
	s = Solver()
	s.add(x | 0x1337 == 0)
	if s.check():
		print hex(int(str(s.model()[x])))
	else:
		print "unsat :("