from visual import *
from visual.graph import *
import math
print "Final project: Simulate pendulum waves"
print "\n"
from PIL import ImageGrab   # PIL
from subprocess import call # for issuing commands
bob_num = int(raw_input("Enter number of bobs: "))
longest_length = float(raw_input("Enter longest string length: "))
cycle = float(raw_input("Enter number of cycles: "))

#Define a function that determines the all the string lengths
#based on the longest string length and number of cycles
def find_all_length(bob_num, longest_length, cycle):
    len_list = []
    for times in range(bob_num):
        len_list.append(longest_length*((cycle/(cycle+times))**2))
    return sorted(len_list, reverse = False)

#Define some basic values
g = 9.8
"""A list containing all string length"""
L = find_all_length(bob_num, longest_length, cycle)
r = [x + 0.000196 for x in L]
mass= 1.0
scene = display(title='15 bobs, 2 meters, 12 cycles',width = 800,height =800,center = (0,-1,0),background=(1,1,0.5))
ceiling= box(length= 2,height=0.03,width=2,color=color.blue)

#Define the initial angle
theta = math.pi/6

#Define all balls and its position and velocity
"""Make a list of all balls"""
balls = []
for times in range(len(r)):
    balls.append(sphere(radius=0.06,color=color.green, material = materials.shiny))
"""Define all ball position"""
for times in range(len(r)):
    balls[times].pos = vector(r[times]*sin(theta), -r[times]*cos(theta), 0.75 + times * -0.05)
"""Define all ball initial velocity"""
for ball in balls:
    ball.v = vector(0, 0, 0)

#Define all string and its position
"""Make a list of all strings"""
strings = []
for times in  range(len(r)):
    strings.append(cylinder(radius=0.006))
for times in range(len(r)):
    strings[times].pos = vector(0, 0, balls[times].pos.z)
"""Define all string axis"""
for times in range(len(r)):
    strings[times].axis = balls[times].pos - strings[times].pos

#Define a list containing all curves
curves = []
for curve in range(len(r)):
    if curve % 2 == 0:
        curves.append(gcurve(color = color.white))
    else:
        curves.append(gcurve(color = color.blue))

#Define a function that determines the vector of the string force
def force(x, times):
    string_force = - (1E5) * (mag(x) - L[times]) * (x / mag(x))
    return string_force

#Run the simulation at 1.15 times faster than real time
scene.waitfor("click")
dt = 0.001
time = 0
count = cycle
ic, fnum = 0, 0     # counter, and file number
while True:
    rate(1150)
    time += dt
    for times in range(len(balls)):
        balls[times].a = vector(0,-g,0) + (force(strings[times].axis, times)/mass)
        balls[times].v += balls[times].a * dt
        balls[times].pos += balls[times].v * dt
        strings[times].axis = balls[times].pos - strings[times].pos
        for times in range(len(balls)):
            curves[times].plot(title='15 bobs, 2 meters, 11 cycles',pos = (time, sin(arctan(balls[times].pos.x/balls[times].pos.y))))
    count -= 1
    # capture images, for 200 frames
    if (fnum >= 1000):
        break
    elif (ic%41 == 0):      # grab every 20 iterations, may need adjustment
        im = ImageGrab.grab((0,0,1600,800))
        num = '00'+repr(fnum)           # sequence num 000-00999, trunc. below
        im.save('img-'+num[-3:]+'.png') # save to png file, 000-999, 3 digits
        fnum += 1
    ic += 1

# if the program cannot find "ffmpeg", check its path. can also replace it with "movie.bat"
call("ffmpeg -r 20 -i img-%3d.png -vcodec libx264 -vf format=yuv420p,scale=412:206 -y movie.mp4".split())
print ("\n Movie made: movie-graph12cycles.mp4")

    
    
