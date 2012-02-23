import math

def sum_digits(value):
	sum =0
	while value !=0:
		sum +=value%10
		value /=10
	return sum

def fact(value):
	mul =1
	for i in range(value,0,-1):
		mul *=i
	return mul
	
if __name__ == "__main__":
	num = 0
	i = 786 #0
	while num!=8001:
		num = list(map(sum_digits, list (map(fact, range(0,i+1)))))[-1]
		print num, i
		i+=1
	
print i-1		

