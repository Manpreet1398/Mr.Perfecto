# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:09:01 2019

@author: manpr
"""

l=['bob','alis','andrew','Bob','Alis','Andrew']
l1=[1,2,3,4]
l.sort()
print(l)
l.sort(key=str.lower)

print(l)
l.extend(l1)
print(l)
l.extend([1,5,6])
print(l)
l2=l[:5]
print(l2)
l2=l[: : -1]
print(l2)
print(list('hello'))
print(list(range(2,20,2)))
print(l.count('andrew'))
l.reverse()
print(l)
print("h" not in l)
for n in l:
    print(n)
for n in range(len(l)):
    print(n) 
l.pop()
print(l)
l.clear()
print(l)
l=[1,2]
a,b=l
print(a)    