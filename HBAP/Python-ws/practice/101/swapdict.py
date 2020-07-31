#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    swapdict.py
# @Author:      manunellutla
# @Time:        6/7/20 9:17 PM


"""
Take a disctionary and aggregate by repeated values example

input ;
  {'in.text' : 'sam',
    'fanto' : 'nam',
    'out.text : 'sam'}

output :
   {'sam':['in.text', 'out.text'],
    'nam':['fanto']'}

"""
from collections import defaultdict


def swap(indict: {}) -> {}:
    result = defaultdict(list)
    for key, value in indict.items():
        # result[value] = (lambda x: x <- result.get(value).append(key)) if value in result.keys() else [key]
        # print(value, result[value])
        if value in result:
            tmp = []
            tmp = result[value]
            tmp.append(key)
            result[value] = tmp
        else:
            result[value] = [key]
    return result


input = {'in.text': 'sam',
         'fanto': 'nam',
         'out.text': 'sam',
         'tingo': 'disco',
         'lingo': 'nam',
         'singo': 'sam'}

print(swap(input))
