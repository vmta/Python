import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

x = math.sqrt(a * b) / (math.pow(math.e, a) * b) + a * math.pow(math.e, (2 * a / b))

print x

exit()
