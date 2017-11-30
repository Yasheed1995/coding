from visual import *
from visual.graph import *


A,N=0.10,50
size,m,k,d=0.06,0.1,10.0,0.4

scene1=gdisplay(width=800,height=300,xtitle='wavevector',ytitle='angular frequency',background=(0.4,0.4,0))


L=[]
Unit_K=2*pi/(N*d)
t,dt=0,0.0001
T,K,p_c=0,0,0
T_c=0
print "Please wait for a while~"
for n in range(1,N/2):
    Wavevector=n*Unit_K
    phase=Wavevector*arange(N)*d
    ball_pos,ball_orig,ball_v,spring_len=arange(N)*d+A*sin(phase),arange(N)*d,zeros(N),ones(N)*d

    
    while True:
        #rate(10000)
        t+=dt
        T+=dt
    
        spring_len[0:-1]=ball_pos[1:]-ball_pos[0:-1]
        spring_len[N-1]=ball_pos[0]+N*d-ball_pos[N-1]
        ball_v[1:]+=((spring_len[1:]-ones(N-1)*d)*k-(spring_len[0:-1]-ones(N-1)*d)*k)/m*dt
        ball_pos+=ball_v*dt
        ball_v[0]+=k*(spring_len[0]-d)/m*dt

        if (ball_pos[0]-ball_orig[0])*(p_c-ball_orig[0])<0:
            K+=1
        if K==2:
            if T_c==4:
                L.append((Wavevector,2*pi/T))
                T,T_c,K,p_c=0,0,0,0
                break
            else:
                T_c+=1
                T,K,p_c=0,0,0
    
        p_c=ball_pos[0]

p=gdots(color=color.cyan,gdisplay=scene1)
p.plot(pos=L)
print "Thanks for your patience."