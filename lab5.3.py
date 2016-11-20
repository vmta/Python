import sys
import math

def super_fibonacci(n, m):
	if n < 0: n = 1
	if m > 35: m = 35
	fib = list()
	for i in range(0, m):
		fib.append

n = 2
m = 1
print "n: " + str(n) + "; m: " + str(m) + "; " + super_fibonacci(n, m)

n = 3
m = 5
print "n: " + str(n) + "; m: " + str(m) + "; " + super_fibonacci(n, m)

n = 8
m = 2
print "n: " + str(n) + "; m: " + str(m) + "; " + super_fibonacci(n, m)

n = 9
m = 3
print "n: " + str(n) + "; m: " + str(m) + "; " + super_fibonacci(n, m)
exit()
