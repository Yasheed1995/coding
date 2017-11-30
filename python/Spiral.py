#!/usr/bin/python
__author__ = 'b04901025'
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

def spiral(initialLength, angle, multiplier):
	if initialLength <= 1:
		return
	else:
		t.forward(initialLength)
		t.right(angle)
		spiral(initialLength*multiplier, angle, multiplier)

if __name__ == '__main__':
	t.penup()
	t.goto(-200, 200)
	t.pendown()

	#spiral(100, 90, 0.9)
	
	spiral(100, 170, 0.95)
	'''

	spiral(400, 120, 0.8)
	'''
	#spiral(2, 1, 0.999)
	wn.exitonclick()