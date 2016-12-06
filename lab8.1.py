class CombStr():
	userString = None
	
	def __init__(self, userString):
		if not isinstance(userString, str):
			userString = str(userString)
		self.userString = userString
	
	def count_substrings(self, length):
		tStr = self.userString
		sStr = set()
		if length < 1 or length > len(tStr):
			return 0
		while len(tStr) >= length:
			sStr.add(tStr[:length])
			tStr = tStr[1:]
		return len(sStr)

print "=== TESTING START ==="

s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0), "? 0"
print s0.count_substrings(1), "? 4"
print s0.count_substrings(2), "? 5"
print s0.count_substrings(5), "? 7"
print s0.count_substrings(15), "? 0"

s1 = CombStr('igor')
print s1.count_substrings(1), "? 4"

s4  = CombStr('29389efj s9fbsyaedg dBD QYDUEHWFUHB&*#(@)(#!')
print s4.count_substrings(2), "? 43"
print "==== TESTING END ===="

exit()