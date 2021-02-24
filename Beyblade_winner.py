# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 12:32:51 2020

@author: Personal
"""
N = -1
sot=0
a1=[]
b1=[]
condi= (set(a1).union(set(a2))
#while (N <= 1 or N >= 10000000):
ntc = 10
for x in range(ntc):
  while (sot<1 or sot>100000 or min(condi)<0 or max(condi)> 2**63-1):
    sot = int(input("sot"))
    a1=input("t1").split()
    a1 = sorted(list(map(int,a1)),reverse=True)
    b1=input("t2;").split()
    b1 = sorted(list(map(int,b1)),reverse=True)  
    c1=[]


    for x in a1:
      for y in b1:
        if (x>y):
          c1.append([x,y])
          b1.remove(y)
          break
        else:
          continue

    print(len(c1))
    print(c1)
