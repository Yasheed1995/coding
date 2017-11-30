#!/usr/bin/python
__author__ = 'b04901025'
import turtle
import random
wn = turtle.Screen()
t = turtle.Turtle()
t.pen(speed=0)

def appletree(trunklength, levels):
	''' 
	svtree: draws a side-view tree
	trunklength = the length of the first line drawn ("the trunk")
	levels = the depth of recursion to which it continues branching
	'''
	t.shape('classic')
	if levels > 3:
		t.color('brown')
	else:
		
		t.color('darkgreen')
	t.width(levels)
	random.seed(trunklength)
	l = random.uniform(0.7, 3)
	ang = random.uniform(30, 60)
	h = random.randint(0, 9)
	print h
	if levels == 0:
		t.dot(3,'red')
		return
	else:
		t.forward(trunklength)
		t.right(ang)
		appletree(trunklength/l, levels-1)
		t.left(ang)
		appletree(trunklength/l, levels-1)
		t.left(ang)
		appletree(trunklength/l, levels-1)
		t.right(ang)
		t.back(trunklength)
		
if __name__ == '__main__':
	t.penup()
	t.goto(-15, -200)
	t.left(90)
	t.pendown()
	appletree(256, 6)
	wn.exitonclick()