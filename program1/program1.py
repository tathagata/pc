#!/usr/bin/python
""" The 3n+1 Problem
Problem description: Collatz Sequence
"""

def cycleLength(term):
	cycleLen = 0
	while term != 1:
		cycleLen = cycleLen +1
		if term%2 == 0:
			term = term/2
		else:
			term = 3*term + 1
	return cycleLen + 1

import sys
filename = sys.argv[1]
for line in open(filename).xreadlines(  ):
	low, high = line.split(' ')
	low = int(low)
	high = int(high)
	cycleLens = map(cycleLength, range(low, high))
	cycleLens.sort()
	print low, high, cycleLens.pop()
