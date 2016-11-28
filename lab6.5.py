def convert_n_to_m(x, n, m):
	
	if int(n) < 1 or int(m) > 36:
		return False
	
	x = str(x).upper()
	
	if x.find("-") > -1:
		return False
	
	convertString = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	def convert_n_to_10(x, n):
		decNum = 0
		try:
			for i in range(len(x)):
				if convertString.index(x[i]) < n:
					decNum = decNum + convertString.index(x[i]) * n ** (len(x) - 1 - i)
				else:
					return False
			return decNum
		except ValueError:
			return False
	
	def convert_10_to_m(x, m):
		if not x:
			return False
		x = long(x)
		if x < m:
			return convertString[x]
		else:
			if m == 1:
				result = ''
				for i in range(x):
					result = '0' + result
				return result
			
			try:
				return convert_10_to_m(x//m, m) + convertString[x%m]
			except:
				return False
	if n == 10:
		if m == 10:
			#print "Return x as n==10 and m==10"
			return x
		else:
			#print "Return convert_10_to_m(x, m) as n==10 and not m==10"
			return convert_10_to_m(x, m)
	else:
		if m == 10:
			#print "Return convert_n_to_10(x, n) as not n==10 and m==10"
			return convert_n_to_10(x, n)
		else:
			#print "Return convert_10_to_m(convert_n_to_10(x, n), m) as not (n==10 | m==10)"
			return convert_10_to_m(convert_n_to_10(x, n), m)

print "-777 with base 10 converting to base 2 => " + str(convert_n_to_m(-777, 10, 2))
print "FALSE"

print "4DAD5 with base 13 converting to base 10 => " + str(convert_n_to_m("4dad5", 13, 10))
print "318165"

print "1AB3 with base 12 converting to base 10 => " + str(convert_n_to_m("1AB3", 12, 10))
print "3303"

print "769 with base 10 converting to base 2 => " + str(convert_n_to_m("769", 10, 2))
print "1100000001"

print "[123] with base 4 converting to base 3 => " + str(convert_n_to_m([123], 4, 3))
print "False"

print "0123 with base 5 converting to base 6 => " + str(convert_n_to_m("0123", 5, 6))
print "102"

print "123 with base 3 converting to base 5 => " + str(convert_n_to_m("123", 3, 5))
print "False"

print "123 with base 4 converting to base 1 => " + str(convert_n_to_m(123, 4, 1))
print "000000000000000000000000000"

print "-123.0 with base 11 converting to base 16 => " + str(convert_n_to_m(-123.0, 11, 16))
print "False"

print "A1Z with base 36 converting to base 16 => " + str(convert_n_to_m("A1Z", 36, 16))
print "32E7"

exit()