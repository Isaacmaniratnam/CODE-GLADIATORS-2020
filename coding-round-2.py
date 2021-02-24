# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:06:41 2020

@author: Isaac
"""

def condi(a1,a2):
  return set(a1).union(set(a2))
def main():
	ntc = 0
	sot=0
	a1=[]
	b1=[]
	while(ntc < 1 or ntc > 100000):
		ntc = int(input("ntc")) #enter 1 for input
		#print(ntc)
		for x in range(ntc):
			while (sot<1 or sot>100000 or min(condi(a1,b1))<0 or max(condi(a1,b1))> 2**63-1):
				sot = int(input("sot")) #enter size of team 11
				a1=input("team1").split() # enter 28427 19877 30709 18527 17409 14758 20873 18458 28587 17751 21672
				a1 = sorted(list(map(int,a1)),reverse=True)
				b1=input("team2").split() # enter 21865 26619 20213 26217 407 30558 15430 17994 31674 2019 10539
				b1 = sorted(list(map(int,b1)),reverse=True)
				c1 = []  
			for x in a1:
				for y in b1:
					if x>y:
						c1.append([x,y])
						b1.remove(y)
						break
					else:
						continue
			print(len(c1))
			sot = 0
			#print(c1)
main()