#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    nestedlists.py
# @Author:      manunellutla
# @Time:        6/11/20 10:25 PM

# N = int(input())

#create a 2D list from input
students = [[input(), float(input())] for _ in range(int(input()))]

# loop through to find second lowest grade
second_min_grade = (sorted(set([student[1] for student in students]), reverse=False))[1]

#students in lowest score alphabetically
stu_low_score = sorted([student[0] for student in students if student[1] == second_min_grade])
#print names
for name in stu_low_score:
    print(name)

