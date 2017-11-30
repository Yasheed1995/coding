from PIL import Image
import numpy as np
def read(place):
    global w,h
    pic=Image.open(place)
    w,h=pic.size       
    data=np.matrix(pic.getdata()).reshape(h,w)
    #print data
    return data
def readc(place):
    global w,h
    pic=Image.open(place)
    w,h=pic.size       
    data=pic.getdata()
    datal=[[],[],[]]   
    for i in xrange(w*h):
        for j in xrange(3):
            datal[j].append(data[i][j])        
    for i in xrange(3):
        datal[i]=np.matrix(datal[i]).reshape(h,w)
    return datal
def sv(data):
    (u,s,v)=np.linalg.svd(data)
    #print u.shape,s.shape,v.shape
    return (u,s,v)
def cut((u,s,v),k):
    u=u[:,:k]
    s=s[:k]
    v=v[:k,:]
    #print u
    return u*np.diag(s)*v
def demo(data,place):
    pic=Image.new("RGB",(w,h))
    for i in xrange(w):
        for j in xrange(h):
            pi=int(round(data[j,i]))
            pic.putpixel((i,j),(pi,pi,pi))
    pic.save(place)
def democ(datal,place):
    pic=Image.new("RGB",(w,h))
    for i in xrange(w):
        for j in xrange(h):
            pi1=int(round(datal[0][j, i]))
            pi2=int(round(datal[1][j, i]))
            pi3=int(round(datal[2][j, i]))
            pic.putpixel((i,j),(pi1,pi2,pi3))
    pic.save(place)
k=40
datal=readc('2.png')

for i in xrange(3):
    (u,s,v)=sv(datal[i])
    datal[i]=cut((u,s,v),k)
    #print datal[i]
print datal[0]
democ(datal,'test3.png')
#print float(k*(w+h)+k)/(w*h)

'''
k=128
data=read('Lena.png')
(u,s,v)=sv(data)
data=cut((u,s,v),k)
demo(data,'test2.png')
print float(k*(w+h)+k)/(w*h)


print float(k*(w+h)+k)/(w*h)'''


