#!/usr/bin/python
__author__= 'b04901025'
from turtle import *
from random import *

def tri(n):
	# shape('turtle')
	# clr = choice(['darkgreen', 'red', 'blue'])
	# color(clr)
	# color('darkgreen')
	# width(2 * n + 1)
	if n == 0:
		return
	else:
		# dot(10, 'red')
		forward(100)
		left(120)
		tri(n-1)

if __name__ == '__main__':
	# width(10)
	tri(5)
	done()