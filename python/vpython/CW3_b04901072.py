from visual import *

g=9.8
sizes=[0.05,0.04]
ms=[0.2,0.15]
r,k=0.5,15


scene=display(width=800,height=800,center=(-0.3,-0.2,0),background=(0.5,0.5,0))

balls=[sphere(radius=sizes[0],color=color.red),sphere(radius=sizes[1],color=color.red)]
spring=helix(radius=0.02,thickness=0.01)

balls[0].pos=vector(0,0,0)
balls[1].pos=vector(-r-0.2,0,0)
balls[0].v=vector(0,0,0)
balls[1].v=vector(0,0,0)
spring.pos=vector(-r-0.2,0,0)

dt=0.001
t=0
z=0
while True:
    rate(1000)
    spring.axis=balls[0].pos-balls[1].pos
    
    spring.force=-k*(mag(spring.axis)-r)*spring.axis/mag(spring.axis)
    balls[0].a=spring.force/ms[0]
    balls[1].a=-spring.force/ms[1]
    
        
    

    balls[0].v+=balls[0].a*dt
    balls[1].v+=balls[1].a*dt
    balls[0].pos+=balls[0].v*dt
    balls[1].pos+=balls[1].v*dt
    spring.pos=balls[1].pos

    t+=dt
    
    if round (balls[1].pos[0],5)==-0.7 and t>0.001:
        print "T=",t,"seconds"
        print "the averaged center of mass:",(balls[0].pos*ms[0]+balls[1].pos*ms[1])/(ms[0]+ms[1])
        t=0
            
    
        
    














    
