__author__ = "Nikhil Krishnan"
# problem 4.2

from swampy.TurtleWorld import *
from polygon import *
import math

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle)



def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        lt(t, 360.0/n)



world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
print bob

# flower(bob, 7, 60.0, 60.0)
# flower(bob, 10, 40.0, 80.0)
flower(bob, 20, 140.0, 20.0)

wait_for_user()