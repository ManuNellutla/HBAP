#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    listy.py
# @Author:      manunellutla
# @Time:        6/18/20 9:06 PM

if __name__ == '__main__':
        l =[]
        commands = [input() for _ in range(int(input()))]
        for c in commands:
            s = c.split()
            if s[0] != "print":
                eval("l."+s[0]+"("+",".join(s[1:])+")")
            else:
                print(l)