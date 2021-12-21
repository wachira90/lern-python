#!python
# -*- coding: utf-8 -*-
import os

with open('read_demo.txt', 'r') as file:
    # read first 3 lines
    for i in range(3):
        print(file.readline().strip())

        
'''
First line
Second line
Third line
'''
