#!/usr/bin/python
""" Minesweeper
"""
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
			print col
			if not col:
				break
			else:
				a = []
				for i in xrange(int(row)):
					a.append([])
					for j in xrange(int(col)+1):
						char = file.read(1)
						#print char
						if char == '*' or char =='.':
							a[i].append(char)
			#b = [[] for i in range(col)]
				

file.close()
