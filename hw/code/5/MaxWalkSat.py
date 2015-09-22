__author__ = 'nkrishn'

import random
import math

# compute normalization values
def MaxMinEnergy(r):
    minimum = sum(Schaffer(random.uniform(r[0],r[1])))
    maximum = minimum

    for i in range(100):
        test = sum(Schaffer(random.uniform(r[0],r[1])))
        if test< minimum:
            minimum = test
        if test> maximum:
            maximum = test
        # minimum = 0 # to avoid problem with minimization

    return (maximum,minimum)

# multi-objective model: Schaffer
def Osyczka2(x):
    """
    :rtype : (f1, f2)
    """

    return (x**2,(x-2)**2)

def energy(state,Max,Min):
    # return (sum(Schaffer(state))-Min)/(Max-Min)
    return (sum(Schaffer(state)))

def jump(ce,ne,t):
    prob = math.exp((ce-ne)*t)
    assert prob <= 1
    return (prob > random.random())

def test():

    mutation_variance = 10
    Max,Min = MaxMinEnergy((-10**2,10**2))


    # Initial parameters
    curr_state = random.gauss(10.0,10.0)
    curr_energy = energy(curr_state,Max,Min)
    K_temp = 1
    K_max = 1000

    # Solution buffer
    best_state = curr_state
    best_energy = curr_energy

    op_str = ", {dig:04},  :{en:1.4}, ".format(dig=K_temp,en=best_energy)
    while K_temp< K_max and curr_energy < Max:

        #mutation
        neigh_state = curr_state + random.gauss(0.0,mutation_variance)
        neigh_energy = energy(neigh_state,Max,Min)

        if neigh_energy < best_energy: # new best
            best_state = neigh_state
            best_energy = neigh_energy
            op_str+='!'

        if neigh_energy < curr_energy: # jump to better
            curr_state = neigh_state
            curr_energy = neigh_energy
            op_str+='+'
        elif jump(curr_energy,neigh_energy,float(K_temp)/K_max):
            curr_state = neigh_state
            curr_energy = neigh_energy
            op_str+='?'

        op_str+= '.'
        K_temp+= 1
        if (K_temp % 25) == 0:
            op_str+="\n"
            print op_str
            op_str = ", {dig:04},  :{en:1.4}, ".format(dig=K_temp,en=best_energy)

    return (best_state,best_energy)

(solution, minimum_energy) = test()
print "Solution, x = %g" %solution
print "Solution energy = %g" %minimum_energy

