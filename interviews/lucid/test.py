splitstring = []
def printsplits(string):
	if len(string) == 2:
		 for i in ' '.join(string)

	else:
		if (len(string[1:])>1):
			global splitstring
			splitstring.append([string[:1], printsplits(string[1:])])


if __name__ == "__main__":
	printsplits('abcdef')
	print splitstring
