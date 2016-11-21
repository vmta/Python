def count_holes(n):
	dHoles = {'0': 1, '1': 0, '2': 0, '3': 0, '4': 1, '5': 0, '6': 1, '7': 0, '8': 2, '9': 1}
	sHoles = 0
	
	# If not a string, then convert argument into a string
	if not isinstance(n, str):
		n = str(n)
	
	# If a string argument has leading zeros, strip them off
	while True:
		if len(n) > 1 and (n[0] == '0' or n[0] == '-'):
			n = n[1:]
		else:
			break
	
	# If string contains anything but numbers, return ERROR
	if not n.isdigit():
		return "ERROR"
	
	# Check each argument's number and get corresponding value from dict
	# to sum them up
	for i in range(0, len(n)):
		sHoles = sHoles + dHoles[n[i]]
	
	# Finally, return the sum
	return sHoles

print '-888888888888888888888' + ': ' + str(count_holes(-888888888888888888888))
print '888888888888888888888' + ': ' + str(count_holes(888888888888888888888))
print '0' + ': ' +  str(count_holes(0))
print '-88' + ': ' +  str(count_holes('-88'))
print '[1]' + ': ' +  str(count_holes([1]))
print '88.0' + ': ' +  str(count_holes(88.0))
print '""' + ': ' + str(count_holes(''))
print 'None' + ': ' + str(count_holes(None))
print '69L' + ': ' + str(count_holes(69L))

exit()