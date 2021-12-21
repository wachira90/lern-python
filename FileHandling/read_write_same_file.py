#!python
# -*- coding: utf-8 -*-
import os

with open('read_demo.txt', 'r+') as f:
    # read from start
    print(f.read())

    # Writing into file
    # write at current position
    f.write("\nSixth Line")
    # this will read from current file pointer position
    print(f.read())

    # write at current position
    f.write("\nSeventh Line")
    # this will read from current position
    print(f.read())
