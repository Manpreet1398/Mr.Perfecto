# -*- coding: utf-8 -*-
"""
Created on Sat May  4 17:20:00 2019

@author: manpr
"""

class sam:
    "this is sample class"
    d={"name":"ank"}
    def display(self):
        pass
c=sam()
print(c.__doc__)
#c is isntance of a class sam (default constructor)
print(sam.__dict__)
print(c.display.__name__)
print(sam.__module__)
     
class second:
    pass
d=second()
d.x=11
