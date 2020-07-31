#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    AtheleteSort.py
# @Author:      manunellutla
# @Time:        6/9/20 11:48 AM

N, M = map(int, input("N M: ").split())

if not (1 <= N <= 1000 and  1 <= M < 1000):
    print("numbers out of range")
    quit()

rows = []
for _ in range(N):
    rows.append(input("row: "))

K = int(input("K: "))

if not 0  <= K <= M:
    print("sorting column not in range")
    quit()

rows = sorted(rows, key=lambda row: int(row.split()[K]))

for row in rows:
    print(row)








#### Awesome solution ##########
# N, M = map(int, input("N, M :").split())
# rows = [input("R: ") for _ in range(N)]
# K = int(input("K: "))
#
# for row in sorted(rows, key=lambda row: int(row.split()[K])):
#     print(row)
