#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    GeneralInterface.py
# @Author:      manunellutla
# @Time:        6/8/20 10:27 PM

"""
 This is a general interface that will be carried across
"""
class Distribution:

    def __init__(self, mu=1, sigma=0):
        """
        Constructor for gaussiance
        :param mu:
        :param sigma:
        """
        self.stdev = sigma
        self.mean = mu

    def calculate_mean(self):
        return self.mean

    def calculate_stdev(self):
        return self.stdev