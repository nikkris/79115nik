__author__ = 'nkrishn'

import random
import math
import copy

# Multi-objective problem
class Osyczka2:
    def __init__(self):
        """

        :rtype : object
        """
        self.probability = 0.5
        self.retries = 10
        self.changes = 1000
        self.maximization = True
        self.minEnergy = -400
        self.maxEnergy = 150
        self.num_decision = 6
        self.min_decision = [0,0,1,0,1,0]
        self.max_decision = [10,10,5,6,5,10]
        self.stepsize = 10
        self.timeout = 1000

    def eval_Osyczka2(self,x):
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

    def norm_energy(self,state):
        # return (sum(Osyczka2(state))-Min)/(Max-Min)
        return (sum(self.eval_Osyczka2(state))-self.minEnergy)/(self.maxEnergy - self.minEnergy)

    def energy(self,state):
        # return sum(Osyczka2(state))
        return (sum(self.eval_Osyczka2(state)))

    def Osyczka2constraintCheck(self,x):
        if (0 <= x[0]+x[1]-2) and (0 <= 6-x[0]-x[1])\
            and (0 <= 2-x[1]+x[0]) and (0 <= 2-x[0]+3*x[1])\
                and (0 <= 4 - (x[2]-3)**2-x[3]) and (0 <= (x[4]-3)**3+x[5]-4):
            return True
        else:
            return False

    def randomValidInput(self):
        ConstraintOk = False
        time_out = 0
        while (not ConstraintOk) and (time_out < self.timeout):
            candidate = [random.uniform(self.min_decision[0],self.max_decision[0]),
                         random.uniform(self.min_decision[1],self.max_decision[1]),
                         random.uniform(self.min_decision[2],self.max_decision[2]),
                         random.uniform(self.min_decision[3],self.max_decision[3]),
                         random.uniform(self.min_decision[4],self.max_decision[4]),
                         random.uniform(self.min_decision[5],self.max_decision[5])]
            ConstraintOk = self.Osyczka2constraintCheck(candidate)
            time_out+= 1
        if ConstraintOk:
            return candidate
        else:
            print "error in generating valid input"
            return [0,0,0,0,0,0]

    def indexValidInput(self,old_candidate,index):
        ConstraintOk = False
        candidate = copy.copy(old_candidate)
        time_out = 0
        while (not ConstraintOk) and (time_out <self.timeout):
            candidate[index] = random.uniform(self.min_decision[index],self.max_decision[index])
            ConstraintOk = self.Osyczka2constraintCheck(candidate)
            time_out+= 1
        if ConstraintOk:
            return candidate
        else:
            return old_candidate

    def bestValidInput(self,old_candidate,index):
        candidate = copy.copy(old_candidate)
        best_candidate = copy.copy(old_candidate)
        for iLoop in range(self.stepsize):
            candidate[index] = self.min_decision[index]+(iLoop/float(self.stepsize))*(self.max_decision[index]-self.min_decision[index])
            if self.Osyczka2constraintCheck(candidate):
                if self.norm_energy(candidate)> self.norm_energy(best_candidate):
                    best_candidate = copy.copy(candidate)
        return best_candidate

    def maxminOsyczka2(self, nE):
        # find the empirical minimum and maximum of Osyczka2 model

        min = self.energy(self.randomValidInput())
        max = min

        for i in range(nE*10):
            newEnergy = self.energy(self.randomValidInput())
            if (min > newEnergy):
                min = newEnergy
            elif (newEnergy> max):
                max = newEnergy
        return (min,max)


# Multi-objective optimizer
def MaxWalkSat(problem):
    # we are assuming maximization

    #best_candidate initialization
    best_candidate = problem.randomValidInput()
    best_energy = problem.norm_energy(best_candidate)

    for iRetry in range(problem.retries):
        candidate = problem.randomValidInput()

        old_score = problem.norm_energy(candidate) # for printout only

        op_str = ", {dig:04},  :{en:1.4}, ".format(dig=0,en=best_energy)
        for iChng in range(problem.changes):
            # print "before change"
            # print "Normalized energy = %f" %problem.norm_energy(candidate)
            if problem.norm_energy(candidate)> 1.5:
                return candidate, problem.energy(candidate)
            else:
                index = random.randint(0,problem.num_decision-1)
                if problem.probability < random.random():
                    #change random setting in index
                    # print "random index"
                    candidate = problem.indexValidInput(candidate,index)
                    # print "Normalized energy = %f" %problem.norm_energy(candidate)

                else:
                    # print "optimize index"
                    candidate = problem.bestValidInput(candidate,index)
                    # print "Normalized energy = %f" %problem.norm_energy(candidate)


                #for printout only
                if old_score>problem.energy(candidate):
                    op_str+='?.' #jump
                else:
                    op_str+='+.'

            if ((iChng+1) % 25) == 0:
                op_str+="\n"
                print op_str
                op_str = ", {dig:04},  :{en:1.4}, ".format(dig=iChng,en=problem.norm_energy(candidate))

        energy = problem.norm_energy(candidate)
        if energy > best_energy:
            best_candidate = copy.copy(candidate)
            best_energy = energy
            op_str='!' #new best in retries
            print op_str



    return best_candidate, best_energy

#testing
prob1 = Osyczka2()

print "Experiment to determine the minimum and maximum energies"
[minEn,maxEn] = prob1.maxminOsyczka2(1000)
print "Minimum Energy = %f" %minEn
print "Maximum Energy = %f \n" %maxEn


(solution, maximum_energy) = MaxWalkSat(prob1)
print "Solution, x = ", solution
print "Solution energy = %g" %maximum_energy


