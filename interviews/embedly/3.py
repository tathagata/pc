from __future__ import division
sum = 0
for i in range(1,900): sum+=1/i

new_sum =0
for i in range(1,450):
	new_sum += 1/i
	print i, sum, sum/2, sum/2-new_sum
	if (sum/2-new_sum)<0.0000:
		break
		


