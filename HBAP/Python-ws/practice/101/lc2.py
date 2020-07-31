#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    lc2.py
# @Author:      manunellutla
# @Time:        6/9/20 10:04 PM

"""
list  comprehension

input :
    x
    y
    z
    N
output:
 [[0,0,0],[0,0,1].......[1,1,1]]
"""
from click._compat import raw_input

if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    x,y,z,n = [int(raw_input()) for _ in range(4)]
    print ([ [ i, j,k] for i in range( x + 1) for j in range( y + 1) for k in range(z + 1) if ( ( i + j + k) != n )])