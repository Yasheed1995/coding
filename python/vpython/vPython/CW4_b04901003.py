from visual import *
import math
g = 9.8
k = 1E5
L = 1.0
mass = 1.0
theta = 0.2
scene = display(width=800, height=1000, center=(0, -0.3, 0), background=(0.5,0.5,0)) 
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue) 
ball = sphere(radius = 0.03, color=color.red)
ball.pos = L*vector(math.sin(theta),-math.cos(theta),0)
ball.v = vector(0, 0, math.sqrt(g*L*math.sin(theta)*math.tan(theta)))
string = cylinder(radius=0.003)
string.pos = vector(0, 0, 0)
string.axis = ball.pos


dt = 0.001
tv = 0
t = 0
n = 0
while True:
	rate(1000)
	string_force = -k * (mag(ball.pos)-L) * string.axis / mag(string.axis)
	ball.a = vector(0, -g, 0) + string_force/mass
	ball.v += ball.a * dt
	ball.pos +=ball.v * dt
	string.axis = ball.pos
	string_force = -k * (mag(ball.pos)-L) * string.axis / mag(string.axis)
	t += dt
	
	if tv * ball.v.x < 0:
		n += 1
	if n == 2:
		print "Time: %f" %(t)
		n = 0 
		t = 0
	tv = ball.v.x











