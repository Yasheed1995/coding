from visual import *

g = 9.8 
size = [0.05, 0.04]
m = [0.2, 0.15] 
r, k = 0.5, 15  
balls = []

scene = display(width=800, height=800, center=(0, -0.2, 0), background=(0.5,0.5,0)) 
balls.append(sphere(radius = size[0], color=color.red))
balls.append(sphere(radius = size[1], color=color.blue))
spring = helix(radius=0.02, thickness =0.01) 
balls[0].pos = vector(-r/2, 0, 0) 
balls[1].pos = vector(r/2, 0, 0)
balls[0].v = vector(0.6, 0, 0) 
balls[1].v = vector(-0.8, 0, 0)


dt = 0.001
n = 0
p = 0
t = 0
G = vector(0, 0, 0)
tv = 0
while True:
	rate(1000)
 	spring.pos = balls[0].pos
 	spring.axis = balls[1].pos - balls[0].pos 
 	spring_force = - k * (mag(spring.axis) - r) * spring.axis / mag(spring.axis) 
 	balls[1].a = spring_force / m[1] 
 	balls[0].a = -spring_force / m[0]
	
 	balls[1].v += balls[1].a*dt
 	balls[1].pos += balls[1].v*dt
	
 	balls[0].v += balls[0].a*dt
 	balls[0].pos += balls[0].v*dt

 	 
 	G += (balls[1].pos*m[1] + balls[0].pos*m[0])/(m[1]+m[0])
 	t += dt
 	p += 1

	if (balls[0].v.x) * tv <= 0:
 		n += 1

 	if n == 2:
 		print "Time: %f" %(t)
		print G/p
		n = 0
		p = 0
		t = 0
	tv = balls[0].v.x
 		







