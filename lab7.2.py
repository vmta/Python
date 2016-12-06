class Student():
	name = None
	mark = None
	conf = None
	
	def __init__(self, name, conf):
		self.name = name
		self.conf = conf
		self.mark = [0 for i in range(conf['lab_num'] + 1)]
	
	def make_lab(self, m, n = None):
		if m > self.conf['lab_max']:
			m = self.conf['lab_max']
		if n is None:
			n = 0
			while self.mark[n] != 0 and n < self.conf['lab_num']:
				n = n + 1
		if n >= 0 and n < self.conf['lab_num']:
			self.mark[n] = m
		return self
	
	def make_exam(self, m):
		if m > self.conf['exam_max']:
			m = self.conf['exam_max']
		self.mark[len(self.mark) - 1] = m
		return self
	
	def is_certified(self):
		max = self.conf['lab_max'] * self.conf['lab_num'] + self.conf['exam_max']
		result = sum(self.mark)
		canCertify = False
		if result >= self.conf['k'] * max:
			canCertify = True
		return result, canCertify








# TESTING SEQUENCE
conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 20,
'k': 0.61,
}

igor = Student("Igor Gunia", conf)

igor.make_lab(5) \
.make_lab(4.75) \
.make_lab(4.5) \
.make_lab(4.25) \
.make_lab(4) \
.make_lab(3.75) \
.make_lab(3.5) \
.make_lab(3.25) \
.make_lab(2.75) \
.make_lab(1) \
.make_exam(1)

print "{0}'s marks:\n{1}\n{0}'s total points allow to certify? {2}\n".format(igor.name, igor.mark, igor.is_certified())

igor.make_lab(8, 19) \
.make_exam(31)

print "{0}'s marks:\n{1}\n{0}'s total points allow to certify? {2}\n".format(igor.name, igor.mark, igor.is_certified())



conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print o3.is_certified()
o3.make_lab(20,1).make_lab(20,0)
print o3.is_certified()
o3.make_lab(50,2)
print o3.is_certified()
o3.make_lab(40,1)
print o3.is_certified(), o3.mark, o3.conf

exit()