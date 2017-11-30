from visual import *
import math
import ruler

g=9.8 
size = 0.25 
height = 15.0
drag_coef = 0.3
drag_power = 1.0
v_initial = 5
ball_mass = 3
theta = math.pi/6
maxdes = 0
maxang = 0

scene = display(width=800, height=800, center = (0,height/2,0), background=(0.5,0.5,0)) 
floor = box(length=30, height=0.01, width=10, color=color.blue)
ruler1 = ruler.ruler(vector(-15, 0, 1), vector(1,0,0), unit = 2.0, length = 30.0, thickness = 0.2) 
ruler2 = ruler.ruler(vector(-15, 0, 1), vector(0,1,0), unit = 1.0, length = 10.0, thickness = 0.2) 
ball = sphere(radius = size, color=color.red, make_trail=True)
ball.pos = vector( -7, size, 0)
t = 0
dt = 0.001

while maxdes <= ball.pos.x +7:
    ball.pos = vector( -7, size, 0)
    ball.v = v_initial * vector(math.cos(theta), math.sin(theta), 0)
    n = 0
    
    while n<3 :
        rate(1000) 

        ball.pos += ball.v*dt
        a=drag_coef*v_initial**drag_power/ball_mass*(ball.v/v_initial)
        ball.v=ball.v-(a+(0.0,g,0.0))*dt
 
        if ball.pos.y <= size and ball.v.y < 0:
            ball.v.y = - ball.v.y
            n += 1
        t += 0.001
        
    if maxdes <= ball.pos.x +7:
        maxdes = ball.pos.x +7
        maxang = theta
        
    theta += 0.01
    
         
print "distance="+str(maxdes)
print "angle="+str(maxang)
print "runtime="+str(t)

