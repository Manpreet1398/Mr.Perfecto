# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:53:10 2019

@author: manpr
"""

l=[]
l.append(25)
l.append(10)
l.insert(0,36)
l.insert(2,"hello")
print(l)
l1=[1,2,3,4]
l2=['a','b','c','d']
l3=[l1,l2,l]
print(l3)
print(l3[0][3])
print(l*2)
l4=l+l1
print(l4)
l.remove('hello')
print(l)
del l[0]
print(l)
l.sort()
print(l)
l.sort(reverse=True)
print(l)