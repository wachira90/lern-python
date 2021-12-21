#!python
# -*- coding: utf-8 -*-
import os

with open("read_demo.txt", "r") as file:
    # reading the first line
    first_line = file.readline()
    print(first_line)
    for last_line in file:
        pass
    # printing the last line
    print(last_line)
    
'''
First Line 
Fifth Line
'''
