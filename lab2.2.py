import sys

x = 0
y = 0
z = 0

try:
	x = int(sys.argv[1])
	if x < 1:
		print "First argument shall be greater than 0."
		exit()
except:
	print "First argument is not a number"

try:
	y = int(sys.argv[2])
	if y < 0:
		print "Second argument shall be greater or equal 0."
		exit()
except:
	print "Second argument is not a number"

try:
	z = int(sys.argv[3])
	if z < 0 or z > 1:
		print "Third argument shall be greater or equal 0 and lesser or equal 1."
		exit()
except:
	print "Third argument is not a number"

song = ''
for i in range(y):
	if (i < y):
		song = song + ' '
	for j in range(x):
		song = song + 'la'
		if (j < (x - 1)):
			song = song + '-'

#if y > 0:
if z == 0:
	song = song + '.'
elif z == 1:
	song = song + '!'

print "Everybody sing a song:" + song

exit()