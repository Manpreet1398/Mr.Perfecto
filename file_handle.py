# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:01:07 2019

@author: manpr
"""

#file=open("E:\python\sample.txt",'r')
#print(file.readline())
#for line in file.readline() :
 #   print(line,end=" ")
#file.close()    
file=open("E:\python\sample.txt",'w')
file.write("heLLO")
#file.writelines(["this","is","hi"])
#list of strings
#file.close()
file.writeline(["this","is","hi"])
file.close()