from visual import *



scene=display(width=800,height=800,center=(0,-0.5,0),background=(0.5,0.5,0))
ceiling=box(length=1,height=0.005,width=1,color=color.blue)
string=cylinder(radius=0.003)
string.pos=vector(0,0,0)
L=1.0
g=9.8
m=1
theta=pi/180*15

ball=sphere(radius=0.03,color=color.red,make_trail=True)
ball.pos=vector(L*sin(theta),-L*cos(theta),0)
v=sin(theta)*(g/(cos(theta)))**0.5
ball.v=vector(0,0,v)
string.axis=ball.pos-string.pos
theorical_T=2*pi*(L*cos(theta)/g)**0.5

def force(r):
    m=1
    g=9.8
    L=1.0
    f=1E5*(mag(r)-L)
    return -f*r/mag(r)
    
    
dt=0.001
t=0

while True:
    rate(1000)
    string.axis=ball.pos-string.pos
    string_force=force(ball.pos)
    ball.a=string_force/m+vector(0,-g,0)
    ball.v+=ball.a*dt
    ball.pos+=ball.v*dt
   
    t+=dt
    
    if round(ball.v.z,2)==round(sin(theta)*(g/cos(theta))**0.5,2):
        if t>0.1:
            print "T=",t,"seconds"
            t=0
            print "Theorical T=",theorical_T,"seconds\n"
    







    
