#!/usr/bin/python
__author__ = 'b04901025'
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.pen(speed=0)

def draw_sierpinski(length,depth):
	if depth==0:
		# draw a small triangle
		for i in range(0,3):
			t.fd(length)
			t.left(120)
	else:
		draw_sierpinski(length/2,depth-1)
		t.fd(length/2)
		draw_sierpinski(length/2,depth-1)
		t.bk(length/2)
		t.left(60)
		t.fd(length/2)
		t.right(60)
		draw_sierpinski(length/2,depth-1)
		t.left(60)
		t.bk(length/2)
		t.right(60)

if __name__ == '__main__':
	t.penup()
	t.goto(-100, 0)
	t.pendown()
	draw_sierpinski(200, 5)
	wn.exitonclick()