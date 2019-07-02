# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:40:35 2019

@author: manpr
"""

#tuple
x=2,3,4
print(x)
print(len(x))
print(min(x))
print(max(x))
print(tuple("hello"))
print(x.count(4))
print(x.index(2))

def sum():
    c=4+5
    b=6+10
    return c,b
y=sum()
print(y)    
#multiple return values more than 2
l=[1,2,3]
l1=[4,5,'hello']
tup=[l,l1]
print(tup)


