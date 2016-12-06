def find_fraction(summ):
	a, b = 0, 0
	if summ <= 2:
		return False
	elif summ%2 != 0:
		a, b = (summ - 1)/2, (summ + 1)/2
	else:
		a, b = summ/2 - 1, summ/2 + 1
		while a % 2 == 0 and b % 2 == 0 and b % a != 0:
			a, b = a - 1, summ - a + 1
	return a, b


print "=== TEST START ==="

print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)

print "==== TEST END ===="

print find_fraction(100) # (49, 51)
print find_fraction(102) # (49, 53)
print find_fraction(1000) # (499, 501)
print find_fraction(0) # (499, 501)
print find_fraction(-2) # (499, 501)

print "=== NEW TEST START ==="
print find_fraction(0)
print find_fraction(1)
print "==== NEW TEST END ===="


exit(0)