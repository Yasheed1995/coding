#!/usr/bin/python
__author__ = 'b04901025'
import turtle
wn = turtle.Screen()
t = turtle.Turtle()
t.pen(speed=0)

def flakeside(sidelength, levels):
	
	if levels == 0:
		t.forward(sidelength/3.0)
		return
	else:
		flakeside(sidelength/3, levels-1)
		t.right(60)
		flakeside(sidelength/3, levels-1)
		t.left(120)
		flakeside(sidelength/3, levels-1)
		t.right(60)
		flakeside(sidelength/3, levels-1)
		

def snowflake(sidelength, levels):
	flakeside(sidelength, levels)
	t.left(120)
	flakeside(sidelength, levels)
	t.left(120)
	flakeside(sidelength, levels)
	t.left(120)
	
if __name__ == '__main__':
	t.penup()
	t.goto(-100, 0)
	t.pendown()
	snowflake(400, 2)
	wn.exitonclick()
	'''
	koch_flake = "FRFRF"
	iterations = 5
	
	for i in range(iterations):
		koch_flake = koch_flake.replace("F","FLFRFLF")

	t.down()

	for move in koch_flake:
		if move == "F":
			t.forward(100.0 / (3 ** (iterations - 1)))
		elif move == "L":
			t.left(60)
		elif move == "R":
			t.right(120)
	'''