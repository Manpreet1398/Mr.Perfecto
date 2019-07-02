# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:51:49 2019

@author: manpr
"""

d={}
l=[1,2,3]
d["name:"]="manpreet"
print(d['name:'])
d["list"]=l
print(d)
print(d.get("address","not found"))
d.setdefault("address","janakpuri")
print(d)
print(d.setdefault("name:","python"))
d1=d.copy()
print(d1)
d2=dict.fromkeys(d)
print(d2)
d3=dict([(1,2),(3,4)])
print(d3)
#4 functions max 2 values to be returned using those values print dictionary
d.pop("name:")
print(d)
print(d.pop("roll","not found"))
d.update({"name ":"ankit"})
print(d)
print(d.values())
print(d.items())
print(d.keys())
for n in d.keys():
    print(n)
for t in d.items() :
    print(t)
for t in d :
    print(t)
l3=[0,1,2,3,0]
print(any(l3))
print(all(l3))
l4=[0,0,0,0,0]
print(any(l4))
print(all(l4))
l5=[1,2,3]
print(any(l5))
print(all(l5))
    