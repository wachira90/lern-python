#!python
# -*- coding: utf-8 -*-
import os

with open('read_demo.txt', 'r') as fp:
    # Read file into list
    lines = fp.readlines()
    print(lines)
    
'''
['First line\n', 'Second line\n', 'Third line\n', 'Fourth line\n', 'Fifth line']
'''
