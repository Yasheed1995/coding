
# coding: utf-8

# In[ ]:

import turtle

def squarePlus(a,b):
    size = a
    length = b
    time = 4
    wn.setup(a,a) #==turtle.setup(size,size) wn.setup(size,size)
    #t.shape("turtle")
    #t.setpos(0,0)
    t.seth(90)
    move(time, length)
    wn.exitonclick()
def move(time, length):    
    if time > 0:
        t.fd(length/2)
        if time >1:
            t.setpos(0,0)
            t.lt(90)
            time -=1
            move(time, length)
        else:
            return 
    else:
        return


    
wn = turtle.Screen()   
t = turtle.Turtle()    
t.color("red")
t.pensize(5)


squarePlus(1000,500)


# In[ ]:




# In[ ]:



