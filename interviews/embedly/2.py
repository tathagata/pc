from __future__ import division
import math
def sum(vals):
	for i in vals: sum +=i

import urllib, urllib2, urlparse, re
url = 'http://apply.embed.ly/static/data/2.html'
depth =1
do = re.compile(r'<div>')
dc = re.compile(r'</div>')
po = re.compile(r'<p>.*</p>')
vals = []
for i in urllib2.urlopen(url).readlines():
	r=do.search(i)
	if r: 
		print ' '*depth, 'div -', depth
		depth +=1
	r=dc.search(i)
	if r:
		print ' '*depth, 'div -', depth
		depth -=1

	r=po.search(i)
	if r:
		print ' '*depth, 'p -', depth
		vals.append(depth)

sum=0
for i in vals:sum  += i
mean = sum/len(vals) 

sum=0
for i in vals:sum +=math.pow((mean-i),2)
print  math.sqrt(sum/len(vals))
