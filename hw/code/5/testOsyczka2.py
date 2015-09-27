__author__ = 'nkrishn'

import random
import math

class Osyczka2:
    def __init__(self):
        self.probability = 0.5
        self.retries = 10
        self.changes = 100
        self.maximization = True
        self.minEnergy = -350
        self.maxEnergy = 150

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

def Osyczka2constraintCheck(x):
    if (0 <= x[0]+x[1]-2) and (0 <= 6-x[0]-x[1])\
        and (0 <= 2-x[1]+x[0]) and (0 <= 2-x[0]+3*x[1])\
            and (0 <= 4 - (x[2]-3)**2-x[3]) and (0 <= (x[4]-3)**3+x[5]-4):
        return True
    else:
        return False

def randomValidInput():
    ConstraintOk = False
    while not ConstraintOk:
        candidate = [random.uniform(0,10), random.uniform(0,10), random.uniform(1,5), random.uniform(0,6), random.uniform(1,5), random.uniform(0,10)]
        ConstraintOk = Osyczka2constraintCheck(candidate)
    return candidate

def maxminOsyczka2(nE):
    # find the empirical minimum and maximum of Osyczka2 model

    min = energy(randomValidInput())
    max = min

    for i in range(nE*10):
        newEnergy = energy(randomValidInput())
        if (min > newEnergy):
            min = newEnergy
        elif (newEnergy> max):
            max = newEnergy

    return (min,max)

def MaxWalkSat():
    # we are assuming maximization

    #parameters
    probability = 0.5
    numberRetries = 10
    numberChanges = 100




    # for i in range(numberChanges):






    candidate = randomValidInput()
    return candidate, energy(candidate)


# [minEn,maxEn] = maxminOsyczka2(10000) # to test for minimum and maximum values
# print minEn
# print maxEn

(solution, minimum_energy) = MaxWalkSat()
print "Solution, x = ", solution
print "Solution energy = %g" %minimum_energy