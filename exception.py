# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:13:37 2019

@author: manpr
"""

def divide(n):
    try:
        f=n/0
        print(f)
    except ZeroDivisionError :
        print("error found")
    finally:
        print("this has to print for any issue")
    
divide(6)    
#the code in finally will run definitely
#Exception