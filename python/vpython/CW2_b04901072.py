from visual import*
import ruler
from math import pi

g=9.8
size=0.25
v_initial=10
theta=pi/4
drag_coe=0.3
drag_power=1.0



scene=display(title='bouncing projectile',center=(0,5,0),width=1200,height=800,background=(0.5,0.5,0))
floor=box(length=30,height=0.01,width=4,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=True)
ruler1=ruler.ruler(vector(-15,0,1),vector(1,0,0),unit=2.0,length=30.0,thickness=0.2)
ruler2=ruler.ruler(vector(-15,0,1),vector(0,1,0),unit=1.0,length=10.0,thickness=0.2)

ball.pos=vector(-15.0,0.0,0.0)
ball.v=v_initial*vector(cos(theta),sin(theta),0)
dt=0.001
x=0.0
k=0
while ball.pos.x<15.0:
    rate(1000)
    ball.pos+=ball.v*dt
    x+=ball.v.x*dt
    ball.v+=vector(0,-g*dt,0)-drag_coe*ball.v*dt
    if ball.y<=size and ball.v.y<0:
        ball.v.y=-ball.v.y
        k+=1
    if k==3:
        break
print '%f m '%x


