#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    miniongame.py
# @Author:      manunellutla
# @Time:        6/10/20 8:40

s = input("Enter a string: ")

vowels = list('AEIOUaeiou')
print(vowels)

# #stuart = [(lambda a: a + a) (a) for a in list(s) if a in vowels]
# stuart = [s[:i] for i in range(1, len(s)+1)]
# print(stuart)
#
 kevin = sum([a for a in list(s) if a not in vowels])
# print(kevin)

# Stuart,Kevin = {}
# kevin_list, stuart_list  =[]
stusc = 0
kevsc = 0

for i in range(len(s)):
    if s[i] in vowels:
        print(s[:len(s)-i])
        kevsc += (len(s)-i)
        print(kevsc)
    else:
        stusc += (len(s) - i)
        print(stusc)

