# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:35:12 2019

@author: manpr
"""
class A : #const(object) construct is the parents class of all the objects
    def sum(self,a,b):
        s=a+b
        print(s)
a=A()
a.sum(4,5)        
#print(a.__name__)method name
#print(a.__module__)python.py
#new file import sample (sample.txt) will provide SUM() as name and METHOD as module as inherited 
#else importing in same file will give main
def sum() : 
    pass
#to pass the abstract method(no definition)
class B(A) :
    pass
#multiple inheritance     
@staticmethod
def sum(a,b):
#no need to write self
def __init__(self a,b) :
#constructor
    self.a=a
    self.b=b
def sum(self) :
    c=self.a+self.b
    print(c)
    
c=const(4,5)
c.sum()

#Q class with const and 2 values as a parameters 4 methods (arithmetic operators)     