#!/usr/bin/python

class some:
	def __init__(self, e, r, hh, g):
		self.param1 = 1
		self.param2 = 2
		self.param3 = hh
		self.t = g
	def get_1(self):
		self.param1 = 55555
		return self.param1
	def set_2(self):
		self.param2 = 444444
		print self.param2
		
s = some(8, 5, 18, 222)


a = s.get_1()
print a

print s.set_2()

class many(some):
	
	

