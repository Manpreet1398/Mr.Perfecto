# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 13:11:54 2019

@author: manpr
"""

import os
import sys
print(os.getcwd())
#current working directory
#os.chdir("directory path") change directory
file=sys.argv[0]
#reads currrent file
print(os.path.abspath(file))
#absolute path
print(os.listdir(os.getcwd()))
print(os.path.isabs(file))
print(os.path.isabs("python\filesys.py"))
print(os.path.realpath(file))
#relative path
print(os.path.relpath("filesys.py","e:\\"))
print(os.path.relpath("e:\\filesys.py","office"))
print(os.path.dirname(file))
#complete path
print(os.path.basename(file))
#file name
print(os.path.exists(file))
#file exists or not
print(os.path.isdir(os.getcwd()))
print(os.path.isfile(file))
print(os.path.getsize(file))
print(dir(os))
#name
print(help(os))
#complete definition
#os.mkdir("test")
#creates new folder
#os.removedirs("test")
#removes folder
#os.rename("E:\python\fac.py","E:\python\factorial.py")
#renames the directory that is only in current working directory
print(os.stat(file).st_size)
print(os.stat(file).st_mtime)
import datetime
print(datetime.datetime.fromtimestamp(os.stat(file).st_mtime))
print(os.environ.get("Path"))

print(os.walk(os.getcwd()))
for dirpath, dirnames, filenames in os.walk("e:\\python"):
    print("the dirpath are" +str(dirpath))
    print("the dirnames are" +str(dirnames))
    print("the filenames are" +str(filenames))