from swampy.TurtleWorld import *
import math

def square(tur,len):
    for i in range(4):
        fd(tur, len)
        lt(tur)

def polygon(tur,len,n):
    angle = 360.0/n;
    for i in range(n):
        fd(tur, len)
        lt(tur,angle)

def polygonarc(tur,len,n,arc):
    angle = 360.0/n;
    step = int(n*arc/360.0)
    for i in range(step):
        fd(tur, len)
        lt(tur,angle)

def circle(tur,rad,arc):
    n = int(math.pi*rad)
    len = 2.0*math.pi*rad/n
    polygon(tur,len,n)

def arc(tur,rad,arc):
    n = int(math.pi*rad)
    len = 2.0*math.pi*rad/n
    polygonarc(tur,len,n,arc)

world = TurtleWorld()

# bob = Turtle()
# print bob
# square(bob, 100)
#
# charlie = Turtle()
# print charlie
# polygon(charlie,100,5)

# daphine = Turtle()
# daphine.delay = 0.01
# print daphine
# circle(daphine,100,180)

ellie = Turtle()
ellie.delay = 0.01
print ellie
arc(ellie,100,250)

wait_for_user()