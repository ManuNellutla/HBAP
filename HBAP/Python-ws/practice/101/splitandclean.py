#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    splitandclean.py
# @Author:      manunellutla
# @Time:        6/13/20 9:44 PM

def merge_the_tools(string, k):
    # your code goes here
    for i in range(len(string) // k):
        tmp = [str(a) for a in set(list(string[k * i:(k * i) + k]))]
        print("".join(tmp))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
