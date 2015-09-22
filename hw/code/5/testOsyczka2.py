__author__ = 'nkrishn'

import random
import math

def Osyczka2(x):
    """
    x is a list
    :rtype : (f1, f2)
    """
    if (len(x)==6):
        f1 = -(25*(x[0]-2)**2 + (x[1]-2)**2 + (x[2]-1)**2*(x[3]-4)**2 + (x[4]-1)**2)
        f2 = sum([xi**2 for xi in x])
        return (f1,f2)
    else:
        print "Error in number of arguments"

def energy(state,Max=100,Min=-100):
    # return (sum(Schaffer(state))-Min)/(Max-Min)
    return (sum(Osyczka2(state)))

def test():
    x =[2,3,1,4,5,6]
    return x, energy(x)

(solution, minimum_energy) = test()
print "Solution, x = ", solution
print "Solution energy = %g" %minimum_energy