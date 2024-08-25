# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 10:27:31 2022

@author: eghorbanioskalaei
"""
import random , math

berlin52= [[565.0 ,575.0],[25.0, 185.0],[345.0 ,750.0],[945.0, 685.0],[845.0, 655.0],
           [880.0 ,660.0],[25.0, 230.0],[525.0 ,1000.0],[580.0, 1175.0],[650.0, 1130.0],
           [1605.0, 620.0],[1220.0, 580.0],[1465.0 ,200.0],[1530.0, 5.0],[845.0, 680.0],
           [725.0 ,370.0],[145.0 ,665.0],[415.0 ,635.0],[510.0, 875.0],[560.0, 365.0],
           [300.0 ,465.0],[520.0, 585.0],[480.0 ,415.0],[835.0, 625.0],[975.0, 580.0],
           [1215.0 ,245.0],[1320.0 ,315.0],[1250.0 ,400.0],[660.0, 180.0],[410.0 ,250.0],
           [420.0 ,555.0],[575.0, 665.0],[1150.0, 1160.0],[700.0, 580.0],[685.0, 595.0],
           [685.0 ,610.0],[770.0 ,610.0],[795.0 ,645.0],[720.0 ,635.0],[760.0, 650.0],
           [475.0, 960.0],[95.0, 260.0],[875.0, 920.0],[700.0, 500.0],[555.0, 815.0],
           [830.0, 485.0],[1170.0 ,65.0],[830.0, 610.0],[605.0 ,625.0],[595.0, 360.0],
           [1340.0, 725.0],[1740.0, 245.0]]

def stochasticTwoOpt(perm):
    result= perm[:]
    size= len(result)
    
    p1, p2 = random.randrange(0,size), random.randrange(0,size)
    exclude = set([p1])
    if p1==0:
        exclude.add(size-1)
    else:
        exclude.add(p1-1)
        
        
    if p1==size-1:
        exclude.add(0)
    else:
        exclude.add(p1+1)
    
    while p2 in exclude:
        p2= random.randrange(0, size)
        
    if p2 < p1:
        p1, p2 = p2 , p1
    
    result[p1:p2] = reversed(result[p1:p2])
    return result

def tourCost(perm):
    totalDistance = 0.0
    size = len(perm)
    for index in range(size):
        startNode = perm[index]
        
        if index== size-1:
            endNode = perm[0]
        else:
            endNode = perm[index+1]
            
        totalDistance +=euclideanDistance(startNode, endNode)
    return totalDistance

def euclideanDistance(xNode, yNode):
    sum = 0.0
    for xi, yi in zip (xNode, yNode):
        sum+=pow((xi-yi),2)
    return math.sqrt(sum)