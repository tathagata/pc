#!/usr/bin/python
#file_object = open('sampleinput.txt')
#all_the_text = file_object.read()
#lines = file_object.readlines()
#lines = file_object.read().split('\n')
#lines = file_object.read().splitlines(1)
#lines = file_object.read().splitlines(       )


for line in open('sampleinput.txt').xreadlines(  ):
	for word in line.split( ):
		low, high = line.split(' ')
		print low, high

