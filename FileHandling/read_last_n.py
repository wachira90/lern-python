#!python
# -*- coding: utf-8 -*-
import os

n = 2
with open('readdemo.txt', 'r') as f:
    lines = f.readlines()[n:]
print(lines)

'''
['Third Line\n', 'Fourth Line\n', 'Fifth Line']
'''
