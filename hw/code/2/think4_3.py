__author__ = "Nikhil Krishnan"
# problem 4.3

from swampy.TurtleWorld import *
from polygon import *
import math

def isotriangle(tur,isoside,isoangle):
    otherside = 2*isoside*math.sin((isoangle/2.0)/360.0*2*math.pi)
    fd(tur,isoside)
    lt(tur,90+isoangle/2.0)
    fd(tur,otherside)
    lt(tur,90+isoangle/2.0)
    fd(tur,isoside)

def pie(tur,r,n):
    isoangle = float(360.0/n)
    rt(tur,isoangle/2)
    for lp in range(n):
        isotriangle(tur,r,isoangle)
        rt(tur,180)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0
print bob

# pie(bob,100,5) # first figure
# pie(bob,100,6) # second figure
pie(bob,100,7) # third figure

die(bob)

wait_for_user()