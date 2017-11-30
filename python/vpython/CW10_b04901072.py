from visual import *
from random import random
from visual.graph import *

N=50
L=((24.4E-3/(6E23))*N)**(1/3.0)/2
m,size=4E-3/6E23,310E-12
L_size=L-size
k,T=1.38E-23,298.0
t,dt=0,0.5E-13
vrms=(3*k*T/m)**0.5
atoms=[]

deltav=100.
vdist=gdisplay(x=800,y=0,ymax=N*deltav/1000.,width=500,height=300,xtitle="v",ytitle="dN")
theory=gcurve(color=color.cyan)
dv=10.
for v in arange(0.,3001.+dv,dv):
    theory.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(2.*pi*k*T))**1.5)*exp((-0.5*m*v**2)/(k*T))*v**2*dv))
observation=ghistogram(bins=arange(0.,3000.,deltav),accumulate=1,average=1,color=color.red)

scene=display(width=800,height=800,background=(0.2,0.2,0))
container=box(length=2*L,height=2*L,width=2*L,opacity=0.2,color=color.yellow)

for i in range(N):
    position=vector(-L_size+2*L_size*random(),-L_size+2*L_size*random(),-L_size+2*L_size*random())
    if i==N-1:
        atom=sphere(pos=position,radius=size,color=color.yellow,make_trail=True,retain=600)
    else:
        atom=sphere(pos=position,radius=size,color=(random(),random(),random()))
    ra,rb=pi*random(),2*pi*random()
    atom.m,atom.v=m,vector(vrms*sin(ra)*cos(rb),vrms*sin(ra)*sin(rb),vrms*cos(ra))
    atoms.append(atom)

def vcollision(a1,a2):
    v1prime=a1.v-2*a2.m/(a1.m+a2.m)*(a1.pos-a2.pos)*dot(a1.v-a2.v,a1.pos-a2.pos)/abs(a1.pos-a2.pos)**2
    v2prime=a2.v-2*a1.m/(a1.m+a2.m)*(a2.pos-a1.pos)*dot(a2.v-a1.v,a2.pos-a1.pos)/abs(a2.pos-a1.pos)**2
    return v1prime,v2prime

average_free_path=(2*L)**3/((2**0.5)*pi*N*(2*size)**2)
print "Theoretical mean free path : {}\n".format(average_free_path)

mom=0
free_path=[0 for i in range(N)]
col_count=[0 for i in range(N)]
C=0
mean=0


while True:
    rate(1000)
    t+=dt

    v=[]
    for i in range(N):
        atoms[i].pos+=atoms[i].v*dt
        v.append(mag(atoms[i].v))
    observation.plot(data=v)

    for i in range(N-1):
        for j in range(i,N):
            if abs(atoms[i].pos-atoms[j].pos)<=2*size and dot(atoms[i].pos-atoms[j].pos,atoms[i].v-atoms[j].v)<0:
                atoms[i].v,atoms[j].v=vcollision(atoms[i],atoms[j])
                col_count[i]+=1
                col_count[j]+=1
    for atom in atoms:      
        for i in range(3):      
            if abs(atom.pos[i])+size>=L and atom.pos[i]*atom.v[i]>0 :     
                atom.v[i]=-atom.v[i]
                mom+=2*m*abs(atom.v[i])
                
    for i in range(N):
        if col_count[i]==1:
            free_path[i]+=abs(atoms[i].v)*dt
       
        if col_count[i]==2:
            mean+=free_path[i]
            free_path[i]=0
            col_count[i]=1
            C+=1
       
    if int(t/dt)%1000==0:
        print "Pressure : %6.0f Pa"%(mom/(6*(2*L)**2*t))
        print "Mean free path : {}\n".format(mean/C)
        
        
                   










    
    
