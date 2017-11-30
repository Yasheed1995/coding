from visual import *
r=0.3
k=25.0
size=[0.05,0.04,0.03]
mass=[0.3,0.4,0.3]
colors=[color.yellow,color.green,color.blue]
position=[vector(0,0,0),vector(0,-r,0),vector(0.25,-0.45,0)]
velocity=[vector(0,0,0),vector(0,0,0),vector(-0.2,0.42,0)]

def af_col_v(v1,v2,x1,x2,m1,m2):
    v1_prime=v1+2*m2/(m1+m2)*dot((v2-v1),(x1-x2))*(x1-x2)/mag(x1-x2)**2
    v2_prime=v2+2*m1/(m1+m2)*dot((v1-v2),(x2-x1))*(x2-x1)/mag(x2-x1)**2
    return (v1_prime,v2_prime)

def potential(x):
    a=0.5*25*(mag(x)-0.3)**2
    return a

def Ek_line(v1,v2,m1,m2,s):
    v11=abs(dot(v1,s)/mag(s))
    a=0.5*m1*v11**2
    
    v22=abs(dot(v2,s)/mag(s))
    b=0.5*m2*v22**2
    
    v_m=(v1*m1+v2*m2)/(m1+m2)
    v3=abs(dot(v_m,s)/mag(s))
    c=0.5*(m1+m2)*v3**2
    
    return a+b-c

def Ek_rot(v1,v2,m1,m2,s):
    v11=abs(dot(v1,s)/mag(s))
    v111=(mag(v1)**2-v11**2)**(0.5)
    a=0.5*m1*v111**2
    
    v22=abs(dot(v2,s)/mag(s))
    v222=(mag(v2)**2-v22**2)**(0.5)
    b=0.5*m2*v222**2
    
    v_m=(v1*m1+v2*m2)/(m1+m2)
    v3=abs(dot(v_m,s)/mag(s))
    v33=(mag(v_m)**2-v3**2)**(0.5)
    c=0.5*(m1+m2)*v33**2
    
    return a+b-c

def Ek_mass(v1,v2,m1,m2):
    v_m=(v1*m1+v2*m2)/(m1+m2)
    c=0.5*(m1+m2)*mag(v_m)**2
    return c

scene=display(width=1000,height=1000,x=600,y=100,background=(0.3,0.3,0))
ball_reference=sphere(pos=(0,0,0),radius=0.01,color=color.red)
balls=[sphere(pos=position[0],radius=size[0],color=colors[0]),sphere(pos=position[1],radius=size[1],color=colors[1]),sphere(pos=position[2],radius=size[2],color=colors[2])]
balls[0].v=velocity[0]
balls[1].v=velocity[1]
balls[2].v=velocity[2]


string=helix(radius=0.02,thickness=0.01)
string.pos=balls[0].pos
string.axis=balls[1].pos-string.pos

Ek=0.5*mass[2]*mag(balls[2].v)**2
momentum=mass[2]*balls[2].v

print "Initial kinetic energy = %f J"%Ek
print "Initial momentum =",momentum,"\n"

dt=0.001
t=0
t2=0
count=0
q1=0
q2=0
q3=0
q4=0
while True:
    rate(1000)
    
    string.pos=balls[0].pos
    string.axis=balls[1].pos-string.pos
    string.force=-k*(mag(string.axis)-r)*string.axis/mag(string.axis)

    
    balls[0].a=-string.force/mass[0]
    balls[0].v+=balls[0].a*dt
    
    balls[1].a=string.force/mass[1]
    balls[1].v+=balls[1].a*dt

    for ball in balls:
        ball.pos+=ball.v*dt
    
    if (abs(balls[0].pos-balls[2].pos)<=size[0]+size[2] and dot(balls[0].pos-balls[2].pos,balls[0].v-balls[2].v)<=0):
        (balls[0].v,balls[2].v)=af_col_v(balls[0].v,balls[2].v,balls[0].pos,balls[2].pos,mass[0],mass[2])
    
    
    if balls[2].v!=velocity[2]:#after collision
        t+=dt
        q1+=potential(string.axis)*dt
        q2+=Ek_line(balls[0].v,balls[1].v,mass[0],mass[1],string.axis)*dt
        q3+=Ek_rot(balls[0].v,balls[1].v,mass[0],mass[1],string.axis)*dt
        q4=Ek_mass(balls[0].v,balls[1].v,mass[0],mass[1])
        q5=0.5*mass[2]*mag(balls[2].v)**2
        q6=q1/t+q2/t+q3/t+q4+q5
        q7=mass[0]*balls[0].v+mass[1]*balls[1].v
        q8=mass[2]*balls[2].v
        q9=q7+q8
        if round(mag(string.axis),3)==0.3 and t-t2>0.01:
            count+=1
            t2=t
            if count==2:#a period of oscillation
                
                print "Internal vibrational potetial energy average =",q1/t,"J"
                q1=0
                print "Internal vibrational kinetic energy average =",q2/t,"J"
                q2=0
                print "Internal rotational kinetic energy average =",q3/t,"J"
                q3=0
                print "Center of mass kinetic energy =",q4,"J"
                print "Kinetic energy of balls[2] =",q5,"J"
                print "Total energy =",q6,"J"
                print "Linear momentum of spring-ball system =",q7
                print "Linear momentum of balls[2] =",q8
                print "Total linear momentum =",q9,"\n"
                

                
                t=0
                count=0
                t2=0
                
            
        



















    
