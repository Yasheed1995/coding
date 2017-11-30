from visual import *
from random import random
from visual.graph import *

N=100
L=((24.4E-3/(6E23))*N)**(1/3.0)/2
m,size=4E-3/6E23,93E-12
k,T=1.38E-23,298.0
t,dt=0,1E-13
momentum,vrms=0,(2*k*T/m)**0.5
v_W,move_L=0,L
stage=0
atoms=[]

deltav=50
vdist=gdisplay(x=800,y=0,ymax=N*deltav/1000,width=500,height=300,xtitle="v",ytitle="dN")
theory_low_T=gcurve(color=color.cyan)
theory_new_T=gcurve(color=color.blue)
dv=10
for v in arange(0.,4201.+dv,dv):
    theory_low_T.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(4.*pi*k*T))**1)*exp((-0.5*m*v**2)/(k*T))*v*dv))
observation=ghistogram(bins=arange(0.,4200.,deltav),accumulate=1,average=1,color=color.red)
observation2=ghistogram(bins=arange(0.,4200.,deltav),accumulate=1,average=1,color=color.green)

scene=display(width=800,height=800,background=(0.2,0.2,0))
container=box(length=2*L,height=2*L,width=2*size,opacity=0.2,color=color.yellow)

pos_array,v_array=zeros((N,3)),zeros((N,3))
for i in range(N):
    pos_array[i]=[-(L-size)+2*(L-size)*random(),-(L-size)+2*(L-size)*random(),0]
    if i==N-1:
        atom=sphere(pos=pos_array[i],radius=size,color=color.yellow,make_trail=True,retain=600)
    else:
        atom=sphere(pos=pos_array[i],radius=size,color=(random(),random(),random()))
    rb=2*pi*random()
    v_array[i]=[vrms*cos(rb),vrms*sin(rb),0]
    atoms.append(atom)

def vcollision(a1p,a2p,a1v,a2v):
    v1prime=a1v-(a1p-a2p)*sum((a1v-a2v)*(a1p-a2p))/sum((a1p-a2p)**2)
    v2prime=a2v-(a2p-a1p)*sum((a2v-a1v)*(a2p-a1p))/sum((a2p-a1p)**2)
    return v1prime,v2prime
def keyinput(evt):
    global stage
    if evt.key==" ":
        stage+=1
scene.bind("keydown",keyinput)

T_count=0
count_time=0
T_stage3=0

while True:
    t+=dt
    rate(5000)

    pos_array+=v_array*dt
    for i in range(N):
        atoms[i].pos=pos_array[i]
        
    if stage==0 or stage>2:
        observation.plot(data=mag(v_array))
    if stage==2:
        observation2.plot(data=mag(v_array))
        if count_time==0:
            for i in range(N):
                T_stage3+=0.5*m*sum(square(v_array[i]))
            T=T_stage3/(N*k)
            for v in arange(0.,4201.+dv,dv):
                theory_new_T.plot(pos=(v,(deltav/dv)*N*4.*pi*((m/(4.*pi*k*T))**1)*exp((-0.5*m*v**2)/(k*T))*v*dv))
            count_time=1
    if stage==3:
        container.length=2*L
        move_L=L
        
    if stage==1:
        v_W=L/(50000.0*dt)
        container.length+=-2*v_W*dt
        move_L=container.length/2
        if container.length<=L:
            stage+=1

    r_array=pos_array-pos_array[:,newaxis]
    rmag=sqrt(sum(square(r_array),-1))
    hit=less_equal(rmag,2*size)-identity(N)
    hitlist=sort(nonzero(hit.flat)[0]).tolist()
    for ij in hitlist:
        i,j=divmod(ij,N)
        hitlist.remove(j*N+i)
        if sum((pos_array[i]-pos_array[j])*(v_array[i]-v_array[j]))<0:
            v_array[i],v_array[j]=vcollision(pos_array[i],pos_array[j],v_array[i],v_array[j])
    if stage!=1:
        for i in range(N):
            if abs(pos_array[i][0])>move_L-size and pos_array[i][0]*v_array[i][0]>0:
                v_array[i][0]=-v_array[i][0]
                momentum+=2*m*abs(v_array[i][0])
            if abs(pos_array[i][1])>L-size and pos_array[i][1]*v_array[i][1]>0:
                v_array[i][1]=-v_array[i][1]
                momentum+=2*m*abs(v_array[i][0])
    if stage==1:
        for i in range(N):
            if abs(pos_array[i][0])>move_L-size and pos_array[i][0]*v_array[i][0]>0:
                if v_array[i][0]>0:
                    v_array[i][0]=-v_array[i][0]-2*v_W
                    momentum+=m*(abs(2*v_array[i][0])+2*v_W)
                else:
                    v_array[i][0]=-v_array[i][0]+2*v_W
                    momentum+=m*(abs(2*v_array[i][0])+2*v_W)
            if abs(pos_array[i][1])>L-size and pos_array[i][1]*v_array[i][1]>0:
                if v_array[i][1]>0:
                    v_array[i][1]=-v_array[i][1]-2*v_W
                    momentum+=m*(abs(2*v_array[i][1])+2*v_W)
                else:
                    v_array[i][1]=-v_array[i][1]+2*v_W
                    momentum+=m*(abs(2*v_array[i][1])+2*v_W)
                    
    if int(t/dt)%2000==0:
        for i in range(N):
            T_count+=0.5*m*sum(square(v_array[i]))
        print "T = {} K".format(T_count/(N*k))
        T=T_count/(N*k)
        T_count=0
        vol=container.length*container.width*container.height
        print "Volume = {} m^3".format(vol)
        P=momentum/(2*(container.length*container.width+container.height*container.width)*t)
        count=P*(vol)**2
        print "Pressure*volume^gamma = {}\n".format(count)
        momentum=0
        t=0
        
        
        


                                         






    







