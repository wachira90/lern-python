#!python
# -*- coding: utf-8 -*-
import os

N = 2
with open("readdemo.txt","r") as file:
    head = [next(file) for x in range(N)]
print(head)

'''
['First Line\n', 'Second Line\n']
'''
