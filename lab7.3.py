class SuperStr(str):
	
	def __new__(cls, value):
		return str.__new__(cls, value)
	
	def is_repeatance(self, base):
		if isinstance(base, str) and base != "" and self != "":
			testStr = self
			while testStr.find(base) > -1:
				testStr = testStr.replace(base, "")
			if len(testStr) == 0:
				return True
		return False
	
	def is_palindrom(self):
		part_a = ""
		part_b = ""
		testStr = self.lower()
		if len(testStr) % 2 == 0:
			part_a = testStr[:len(testStr)/2:1]
			part_b = testStr[len(testStr)/2::1]
		else:
			middle = ((len(testStr) + 1) / 2) - 1
			part_a = testStr[:middle:1]
			part_b = testStr[middle + 1::1]
		if part_a[::1] == part_b[::-1]:
			return True
		return False
	
	def is_repeatance_test(self, base):
		if not isinstance(base, str):
			return False
		testStr = self
		while testStr.find(base) > -1:
			testStr = testStr.replace(base, "")
		if len(testStr) == 0:
			return True
		return False

	def is_palindrom_test(self):
		midChars = "+-_|.,! "
		midchar = ""
		part_a = ""
		part_b = ""
		testStr = self.lower()
		if len(testStr) % 2 == 0:
			part_a = testStr[:len(testStr)/2:1]
			part_b = testStr[len(testStr)/2::1]
		else:
			middle = ((len(testStr) + 1) / 2) - 1
			part_a = testStr[:middle:1]
			part_b = testStr[middle + 1::1]
			midchar = testStr[middle]
		if part_a[::1] == part_b[::-1] and midchar in midChars:
			return True
		return False


print "\n"

print "TESTING REPEATANCE"
s = SuperStr('')
print s, s.is_repeatance('a') # True


exit()