import math
class Sphere(object):
	r = None
	x = None
	y = None
	z = None
	
	def __init__(self, userR = 1.0, userX = 0.0, userY = 0.0, userZ = 0.0):
		self.r = float(userR)
		self.x = float(userX)
		self.y = float(userY)
		self.z = float(userZ)
	
	def get_volume(self):
		return (4 * math.pi * self.r**3) / 3
	
	def get_square(self):
		return 4 * math.pi * self.r**2
	
	def get_radius(self):
		return self.r
	
	def set_radius(self, userR):
		self.r = float(userR)
	
	def get_center(self):
		return (self.x, self.y, self.z)
	
	def set_center(self, userX, userY, userZ):
		self.x = float(userX)
		self.y = float(userY)
		self.z = float(userZ)
	
	def is_point_inside(self, userX, userY, userZ):
		distance = math.sqrt((self.x - userX)**2 + (self.y - userY)**2 + (self.z - userZ)**2)
		if distance <= self.r:
			return True
		return False

s1 = Sphere()
s1.set_radius(1.1)
s1.set_center(0.5, 1, 0)
print "s1 Center has coordinates: ", s1.get_center()
print "s1 Radius: ", s1.get_radius()
print "(0.99, 0, 0) is inside s1: ", s1.is_point_inside(0.99, 0, 0) # False

# Create test sphere with radius and default center
s0 = Sphere(0.5)

print "s0 Center has coordinates: ", s0.get_center()	# (0.0, 0.0, 0.0)
print "Volume is: ", s0.get_volume()			# 0.523598775598
print "Square is: ", s0.get_square()			# 3,141592653589
print "(0, -1.5, 0) is inside:", s0.is_point_inside(0, -1.5, 0)	# False

# Change sphere radius
s0.set_radius(1.6)
print "(0, -1.5, 0) is inside:", s0.is_point_inside(0, -1.5, 0)	# True
print "Radius is:", s0.get_radius()			# 1.6

# Change sphere center
s0.set_center(1.1, 1.2, 1.3)
print "Center has coordinates: ", s0.get_center()	# (1.1, 1.2, 1.3)

exit()