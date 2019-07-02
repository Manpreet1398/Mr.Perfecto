# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:25:21 2019

@author: manpr
"""

def sum():
    a=8+4
    b=10+5
    return a,b
s=sum()    
print(s)


def sub():
    c=8-4
    d=10-5
    return c,d
s1=sub()
print(s1)

def mul():
    e=8*4
    f=10*5
    return e,f
s2=mul()
print(s2)

def div():
    g=8/4
    h=10/5
    return g,h
s3=div()
print(s3)

d={}
#d["sum:"]=sum()
#print(d["sum:"])
#print(d)
#print(d.setdefault("sub:",sub()))
#print(d)
#print(d.setdefault("mul:",mul()))
#print(d)
#print(d.setdefault("div:",div()))
#print(d)
d=dict([sum(),sub(),mul(),div()])
print(d)
