import sys

n = int(sys.argv[1])
a = 0
b = 1
x = 0
for i in range(0, n):
	x = a + b
	if(i > 0):
		a = b
	b = x
print x

exit()