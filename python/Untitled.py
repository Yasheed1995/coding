#!/usr/bin/python
__author__ = 'b04901025'
import turtle
import math
wn = turtle.Screen()
t = turtle.Turtle()
t.pen(speed=5)

def draw_hax(length,depth):
	if depth==0:
		# draw a small hax
		for i in range(0,6):
			t.fd(length)
			t.left(60)
	else:
		draw_hax(length/2,depth-1)
		t.left(30)
		t.penup()
		t.fd(length * math.sqrt(3))
		t.pendown()
		t.left(90)
		draw_hax(length/2,depth-1)
		t.left(30)
		t.penup()
		t.fd(length * math.sqrt(3))
		t.pendown()
		t.left(90)
		draw_hax(length/2,depth-1)
		t.left(30)

if __name__ == '__main__':
	t.penup()
	t.goto(-100, 0)
	t.pendown()
	draw_hax(200, 2)
	wn.exitonclick()