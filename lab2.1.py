import sys
import math

x = 0
mu = 0
sigma = 0

try:
	x = float(sys.argv[1])
except:
	print "First argument is not a number"

try:
	mu = float(sys.argv[2])
except:
	print "Second argument is not a number"

try:
	sigma = float(sys.argv[3])
except:
	print "Third argument is not a number"

calc = (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(- math.pow((x - mu), 2) / (2 * math.pow(sigma, 2)))

print calc

exit()