#!python
# -*- coding: utf-8 -*-
import os

with open('readdemo.txt', 'r') as f:
  lines = f.readlines()
  for line in reversed(lines):
    print(line)
    
'''
Fifth Line 
Fourth Line 
Third Line 
Second Line 
First Line
'''
    
    
