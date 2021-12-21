#!python
# -*- coding: utf-8 -*-
import os

with open('read_demo.txt', 'r') as fp:
    # Read the first line
    line = fp.readline()
    # Iterate the file till it reached the EOF
    while line != '':
        print(line, end='')
        line = fp.readline()
        
'''
First line
Second line
Third line
Fourth line
Fifth line
'''
