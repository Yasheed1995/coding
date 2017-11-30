#!/usr/bin/python

def fab4(N):
	n, a, b = 0, 0, 1
	while n < N:
		yield b
		a, b = b, a + b
		n = n + 1
		
def fab(N):
	n, a, b = 0, 0, 1
	while n < N:
		print b
		a, b = b, a + b
		n = n + 1
		
if __name__ == '__main__':
	for n in fab4(10000):
		print n
		
	#fab(10000)