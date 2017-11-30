#!/usr/bin/python

import turtle

t = turtle.Turtle()
wn = turtle.Screen()

wn.bgcolor('lightgreen')

def poly(sz, n, N):
	if n < 1:
		return
	else:
		t.dot( 10, 'red' )
		t.forward(sz)
		t.right(360.0/N)
		poly(sz, n-1, N)
		
t.shape('turtle')
t.color('red')
t.width(5)

poly(90, 7, 7)

wn.exitonclick()
