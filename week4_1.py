import sys

def text_prompt(msg):
	try:
		return raw_input(msg)
	except NameError:
		return input(msg)

print 'Quadratic equation solving'
print '--------------------------'

a = float(text_prompt('input a : '))
b = float(text_prompt('input b : '))
c = float(text_prompt('input c : '))

d = b**2 - 4 * a * c
print 'D : ' + str(d)

print 'First way of code'
if d < 0:
	print 'the roots are complex'
else:
	if d == 0:
		print 'the answer is : ' + str(-b / (2 * a))
	else:
		print 'the answers are : ' + str((-b + d**0.5) / (2 * a)) + ' and ' + str((-b - d**0.5) / (2 * a))

print 'Second way of code'
if d < 0:
	print 'the roots are complex'
elif d == 0:
	print 'the answer is : ' + str(-b / (2 * a))
else:
	print 'the answers are : ' + str((-b + d**0.5) / (2 * a)) + ' and ' + str((-b - d**0.5) / (2 * a))
exit()