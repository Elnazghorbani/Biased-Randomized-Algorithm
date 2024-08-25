# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 20:51:15 2022

@author: eghorbanioskalaei
Greedy Randomized Adaptive Search or GRASP metaheuristics
"""

from shared import berlin52, stochasticTwoOpt, tourCost, euclideanDistance
import random, time
import math




'''Aux func to apply a local search'''
def localSearch(aSol, aCost, maxIter):
    count = 0
    while count < maxIter:
        newSol = stochasticTwoOpt(aSol)
        newCost = tourCost(newSol)
        if newCost < aCost:
            aSol = newSol
            aCost = newCost
            count = 0
        else:
            count +=1
    return aSol, aCost

def constructGreedySolution(perm, beta):
    emergingSol =[]
    problemSize = len(perm)
    emergingSol = [perm[random.randrange(0, problemSize)]]
    
    while len(emergingSol)< problemSize:
        notInSolNodes = [node for node in perm if node not in emergingSol]
        costs=[]
        emergingSolSize = len(emergingSol)
        for node in notInSolNodes:
            
            costs.append(euclideanDistance(emergingSol[emergingSolSize-1] , node))
    
        cl= []
        for index, cost in enumerate(costs):
                index= int(math.log(random.random())/ math.log(1-beta))
                index= index %  len(notInSolNodes) 
                cl.append(notInSolNodes[index])
                notInSolNodes.pop(index)
        emergingSol.append(cl[random.randrange(0, len(cl))])
        
    newCost = tourCost(emergingSol)
    return emergingSol, newCost
    



algorithmName="BRA"
print("best solution by "+ algorithmName+ "...")

#problem configuration
inputsTSP= berlin52
maxIteration = 100
maxNoImprove = 50
greedinessFactor = 0.7 #In the range[0,1], o is more greedy 1 is less
start= time.time()

#main loop
bestCost = float("inf") #infinity
while maxIteration > 0:
    maxIteration -=1
    #construct a greedy solution
    newSol, newCost = constructGreedySolution(inputsTSP, greedinessFactor)
    #refine it using a local search heuristic
    newSol, newCost = localSearch(newSol, newCost, maxNoImprove)
    if newCost < bestCost:
        bestSol = newSol
        bestCost = newCost
        print("cost= %.2f; Iter = %d" % (bestCost, maxIteration))
 
#stop clock and return output
stop= time.time()
print("bestCost = %.2f ; Elapsed = %.2fs" % (bestCost, stop-start))
print("bestSol= %s" % bestSol)

