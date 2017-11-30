#!/usr/bin/python
__author__ = 'b04901025'
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

def chai(size):
	''' chai function! '''
	if size < 5:
		return
	else:
		t.forward(size)
		t.left(90)
		t.forward(size / 2.0)
		t.right(90)
		chai(size / 2.0)
		t.right(90)
		t.forward(size)
		t.left(90)
		chai(size / 2.0)
		t.left(90)
		t.forward(size / 2.0)
		t.right(90)
		t.back(size)
		return

if __name__ == '__main__':
	t.penup()
	t.goto(-150, 150)
	t.pendown()
	chai(100)
	wn.exitonclick()	
			