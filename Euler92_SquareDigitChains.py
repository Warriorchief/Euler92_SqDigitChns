#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 22:48:56 2017

@author: christophergreen

Square digit chains
Problem 92
A number chain is created by continuously adding the square of the digits in a number to form a
 new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most
 amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?




"""

#import math

def process(x):
    count=0
    output=0
    for i in str(x):
        output+=int(i)**2
    count+=1
    return output
        

def untilHits(m):
    x=m
    counter=0
    while x!=1:
        x=process(x)
        counter+=1
        if x==89:
            #print(m,"became 89 after",counter,"loops")
            return m
    #print(m,"became 1 after",counter,"loops")

def main(maximum):
    outcount=0
    j=1
    while j<maximum:
        if j%100000==0:
            print("passing through j being",j,"so there's another hundred thousand")
        if untilHits(j)==j:
            outcount+=1
        j+=1
    print("number of ints below",maximum,"that work out to 89 is",outcount)
    return outcount
    
main(10**7) #--> 8581146 CORRECT