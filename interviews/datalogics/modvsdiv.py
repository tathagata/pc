from __future__ import division
import math

def bydiv0():

	for i in range(100, 1, -1):
		if math.floor(i/7)==math.ceil(i/7):
			print i,

def bydiv1():
	for i in range(100, 1, -1):
		s=str(i/7)
		if len(s[s.index('.'):])==2:
			print i,

def bydiv2():
	div = 0
	for i in range(100, 1, -1):
		if math.floor(i/7)==math.ceil(i/7):
			div = i
			print div,
			break
	for i in range(div,1,-7):
		print i,




def bymod():
	for i in range(100,1,-1):
		if (i%7==0):
			print i,

def bymod1():
	div=0
	for i in range(100,1,-1):
		if (i%7==0):
			div=i
			print i,
			break

	for i in range(div,1,-7):
		print i,



if __name__=="__main__":
	print "MOD"
	from timeit import Timer
	t = Timer("bymod()","from __main__ import bymod")
	print t.timeit(1)*1000000

	print "MOD-1"
	t = Timer("bymod1()","from __main__ import bymod1")
	print t.timeit(1)*1000000
	
	print "DIV-0"
	from timeit import Timer
	t = Timer("bydiv0()","from __main__ import bydiv0")
	print t.timeit(1)*1000000


	print "DIV-1"
	t = Timer("bydiv1()","from __main__ import bydiv1")
	print t.timeit(1)*1000000


	print "DIV-2"
	t = Timer("bydiv2()","from __main__ import bydiv2")
	print t.timeit(1)*1000000



