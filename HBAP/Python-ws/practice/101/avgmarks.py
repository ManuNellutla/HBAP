#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    avgmarks.py
# @Author:      manunellutla
# @Time:        6/11/20 11:28 PM

# students = {a: (float(b) + float(c) + float(d)) / 3 for a, b, c, d in (input().split() for _ in range(int(input())))}
# print(format(students.get(input()), '.2f'))

# Named Tuples
import re
from collections import namedtuple
import inspect

if __name__ == '__main__':
      n = int(input())
      Student = namedtuple('Student', input().split())
      students = sum([int(Student(*input().split()).MARKS) for _ in range(n)])
      print(students/n)
    #  print(stu)

    # print([[a / b] for a, b in [(sum(a), len(a)) for a in
    #                             [[int(Student(*input().split()).MARKS) for _ in range(n)] for n, Student in
    #                              [(int(input()), __import__('collections').namedtuple('Student', input().split()))]]]][
    #           0][0])
