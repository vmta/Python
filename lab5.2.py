import sys
import math
import random

def counter(a, b):
	_a = str(a)
	_b = list(set(str(b)))
	counter = 0
	
	i = 0
	while i < len(_b):
		if _a.find(_b[i]) > -1:
			counter = counter + 1
		#j = 0
		#while j < len(_a):
		#	if _b[i] == _a[j]:
		#		counter = counter + 1
		#	j = j + 1
		i = i + 1
	return counter

def test():
	a = int(math.floor(random.random() * 10000))
	b = int(math.floor(random.random() * 1000))
	print "a: " + str(a) + "; b: " + str(b) + "; result: " + str(counter(a, b))

for i in range(0,5):
	test()

a = 12345
b = 567
print "a: " + str(a) + "; b: " + str(b) + "; result: " + str(counter(a, b))

a = 1233211
b = 12128
print "a: " + str(a) + "; b: " + str(b) + "; result: " + str(counter(a, b))

a = 123
b = 45
print "a: " + str(a) + "; b: " + str(b) + "; result: " + str(counter(a, b))

exit()
