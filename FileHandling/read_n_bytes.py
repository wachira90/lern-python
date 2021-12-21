#!python
# -*- coding: utf-8 -*-
import os

# read file with absolute path
try:
    fp = open(r"E:\demos\files_demos\read_demo.txt", "r")
    print(fp.read(30))
    fp.close()
except FileNotFoundError:
    print("Please check the path.")
    
'''
First line
Second line
Third l
'''
