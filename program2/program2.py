#!/usr/bin/python
""" Minesweeper
"""
from array import array
file = open('siminesweepertest.txt', 'r')

#print file.read()

#for line in open('siminesweepertest.txt').xreadlines( ):
while 1: 
	row = file.read(1)          # read by character
   	if not row: 
		break
    	else:
		if row.isdigit():
			col = file.read(3)
			x = []
			for i in xrange(int(row)):
				x.append([])
				for j in xrange(int(col)+1):
					char = file.read(1)
					if char == '*' or char == '.':
						x[i].append(char)
			print x	 	
file.close()
