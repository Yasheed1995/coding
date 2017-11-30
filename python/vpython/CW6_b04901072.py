from visual import *


G=6.67E-11
mass={"earth":5.9742E24,"sun":1.989E30 ,"mars":6.4185E23,"comet halley":2.2E14}
d_at_perihelion={"earth":1.471E11,"mars":2.066E11,"comet halley":8.7664E10}
v_at_perihelion={"earth":3.029E4,"mars":2.65E4,"comet halley":5.4554E4}

def G_force(m,pos):
    G=6.67E-11
    r=mag(pos)
    M=1.989E30
    f=G*M*m/r**2
    return -f*pos/mag(pos)

class as_object(sphere):
    
    def potential_energy(self):
        return -G*mass["sun"]*self.m/mag(self.pos)
    def kinetic_energy(self):
        return 0.5*self.m*mag(self.v)**2
    

scene=display(width=1000,height=1000,background=(0,0,0))
scene.forward=vector(0,-1,0)

sun=sphere(radius=30*6.955E8,color=color.yellow,pos=vector(0,0,0),material=materials.emissive)
earth=as_object(radius=3000*6.372E6,material=materials.BlueMarble,make_trail=True)
earth.pos=vector(d_at_perihelion["earth"],0,0)
earth.m=mass["earth"]
earth.v=vector(0,0,-v_at_perihelion["earth"])

mars=as_object(radius=3000*3.389E6,material=materials.rough,color=color.red,make_trail=True)
mars.pos=vector(d_at_perihelion["mars"],0,0)
mars.m=mass["mars"]
mars.v=vector(0,0,-v_at_perihelion["mars"])

comet_halley=as_object(radius=3E5*11E3,color=color.white,make_trail=True)
comet_halley.pos=vector(d_at_perihelion["comet halley"],0,0)
comet_halley.m=mass["comet halley"]
comet_halley.v=vector(0,0,v_at_perihelion["comet halley"])

#orbit1=curve(radius=1E9,pos=earth.pos,color = color.blue)
#orbit2=curve(radius=1E9,pos=mars.pos,color=color.red)
#orbit3=curve(radius=1E9,pos=comet_halley.pos,color=color.white)

dt=86400.0
dy=1.0/365
t_earth=0
t_mars=0
t_comet=0
t_check=0
m=0
n=0
f=0
k=0
k2=0
k3=0
pos_c=vector(0,0,0)
t_area=-100000000
d_at_aphelion_earth=vector(0,0,0)
d_at_aphelion_mars=vector(0,0,0)


print "Kinetic energy at perihelion:",comet_halley.kinetic_energy(),"J"
print "Potential energy at perihelion:",comet_halley.potential_energy(),"J"
print "Total energy at perihelion:",comet_halley.potential_energy()+comet_halley.kinetic_energy(),"J\n"
while True:
    rate(1000)
    m=earth.pos.z
    n=mars.pos.z
    f=comet_halley.pos.z
    for i in [earth,mars,comet_halley]:
        i.v+=G_force(i.m,i.pos)/i.m*dt
        i.pos+=i.v*dt
        
    #orbit1.append(earth.pos)
    #orbit2.append(mars.pos)
    #orbit3.append(comet_halley.pos)

    t_area+=1
    
    if t_area==1:
        angle=diff_angle(pos_c,comet_halley.pos)
        area=0.5*mag(pos_c)*mag(comet_halley.pos)*sin(angle)
        print "Swept area:",area,"\n"
        t_area=-10000000
        pos_c=vector(0,0,0)
        

    t_earth+=dy
    t_mars+=dy
    t_comet+=dt
    
    
    if (earth.pos.z)*m<0:
        k+=1
        if k==1:
            d_at_aphelion_earth+=earth.pos
        if k==2:
            print "Earth(T**2/r**3):",(t_earth)**2/((mag(d_at_aphelion_earth)+d_at_perihelion["earth"])/2)**3,"\n"
    if (mars.pos.z)*n<0:
        k2+=1
        if k2==1:
            d_at_aphelion_mars+=mars.pos
        if k2==2:
            print "Mars(T**2/r**3):",(t_mars)**2/((mag(d_at_aphelion_mars)+d_at_perihelion["mars"])/2)**3,"\n"

    if (comet_halley.pos.z)*f<0:
        k3+=1
        if k3%2==1:
            pos_c+=comet_halley.pos
            t_area=0
            print "Kinetic energy at aphelion:",comet_halley.kinetic_energy(),"J"
            print "Potential energy at aphelion:",comet_halley.potential_energy(),"J"
            print "Total energy at aphelion:",comet_halley.potential_energy()+comet_halley.kinetic_energy(),"J"
        if k3%2==0:
            pos_c+=comet_halley.pos
            t_area=0
            print "Kinetic energy at perihelion:",comet_halley.kinetic_energy(),"J"
            print "Potential energy at perihelion:",comet_halley.potential_energy(),"J"
            print "Total energy at perihelion:",comet_halley.potential_energy()+comet_halley.kinetic_energy(),"J"
            
           
    if round(comet_halley.v.z)==0:
        if t_comet-t_check>86400*5:
            pos_c+=comet_halley.pos
            t_area=0
            print "Kinetic energy at half_way point:",comet_halley.kinetic_energy(),"J"
            print "Potential energy at half_way point:",comet_halley.potential_energy(),"J"
            print "Total energy at half_way point:",comet_halley.potential_energy()+comet_halley.kinetic_energy(),"J"
           
            t_check=t_comet

    
    
     
















    

    
    
