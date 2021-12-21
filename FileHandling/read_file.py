#!python
# -*- coding: utf-8 -*-

# read file with absolute path
try:
    fp = open(r"E:\demos\files\read_demo.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("Please check the path")
 
