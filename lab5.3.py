import sys
import math

def super_fibonacci(n, m):
	if n < 0: n = 1
	if m > 35: m = 35
	fib = list()
	i = 0
	while i <= n:
		if i < m:
			fib.append(1)
		else:
			num = 0
			for j in range (len(fib) - m, len(fib)):
				num = num + fib[j]
			fib.append(num)
		i = i + 1
	#print fib
	return fib[n - 1]

n = 2
m = 1
print "n: " + str(n) + "; m: " + str(m) + "; res: " + str(super_fibonacci(n, m))

n = 3
m = 5
print "n: " + str(n) + "; m: " + str(m) + "; res: " + str(super_fibonacci(n, m))

n = 8
m = 2
print "n: " + str(n) + "; m: " + str(m) + "; res: " + str(super_fibonacci(n, m))

n = 9
m = 3
print "n: " + str(n) + "; m: " + str(m) + "; res: " + str(super_fibonacci(n, m))

n = 10
m = 5
print "n: " + str(n) + "; m: " + str(m) + "; res: " + str(super_fibonacci(n, m))

exit()
