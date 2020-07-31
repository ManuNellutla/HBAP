#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    makeDatainCSV.py
# @Author:      manunellutla
# @Time:        6/24/20 8:49 AM
import csv
import random

import pandas as pd

rows = int(input())
columns = input().split()
filename = input()

with open(filename, mode='w') as efile:
    e_writer = csv.writer(efile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    e_writer.writerow(columns)
    for i in range(rows):
        e_writer.writerow([random.randint(190,300) for _ in range(len(columns))])
