import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if (a > 0 and b > 0 and c > 0):
	if (a < (b + c) and b < (a + c) and c < (a + b)):
		print "triangle"
	else:
		print "not triangle"
else:
	print "not triangle"

alpha = 0
alpha_rad = (pow(b, 2) + pow(c, 2) - pow(a, 2)) / (2 * b * c)
if(alpha_rad >= -1 and alpha_rad <= 1):
	alpha = math.acos(alpha_rad) * 180 / math.pi
	print "alpha: %f" % alpha

beta = 0
beta_rad = (pow(a, 2) + pow(c, 2) - pow(b, 2)) / (2 * a * c)
if(beta_rad >= -1 and beta_rad <= 1):
	beta = math.acos(beta_rad) * 180 / math.pi
	print "beta: %f" % beta

if(alpha > 0 and beta > 0):
	zeta = 180 - alpha - beta
	print "zeta: %f" % zeta

exit()
