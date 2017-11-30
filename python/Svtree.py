#!/usr/bin/python
__author__ = 'b04901025'
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

def svtree(trunklength, levels):
	''' 
	svtree: draws a side-view tree
	trunklength = the length of the first line drawn ("the trunk")
	levels = the depth of recursion to which it continues branching
	'''
	if levels == 0:
		return
	else:
		t.forward(trunklength)
		t.right(30)
		svtree(trunklength/2, levels-1)
		t.left(60)
		svtree(trunklength/2, levels-1)
		t.back(trunklength)

if __name__ == '__main__':
	t.penup()
	t.goto(-15, -50)
	t.left(90)
	t.pendown()
	svtree(128, 6)
	wn.exitonclick()