from visual import *
g=9.8 
size = 0.25 
height = 15.0

scene = display(width=800, height=800, center = (0,height/2,0), background=(0.5,0.5,0)) 
floor = box(length=30, height=0.01, width=10, color=color.blue)
ball = sphere(radius = size, color=color.red)
a1=arrow(shaftwidth=0.1)

ball.pos = vector( -15, 2, 0)
ball.v = vector( 8, 8, 0)
a1.color=color.green

dt = 0.001
t=0.000
while ball.pos.y >= size: 
 rate(1000) 

 ball.pos += ball.v*dt
 ball.v.y += - g*dt
 a1.pos=(ball.pos.x+0.5,ball.pos.y,0)
 a1.axis=(ball.v.x,ball.v.y,0)
 t=t+0.001
 
print t 
