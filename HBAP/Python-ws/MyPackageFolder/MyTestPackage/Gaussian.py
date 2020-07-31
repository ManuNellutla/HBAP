#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Gaussian.py
# @Author:      manunellutla
# @Time:        6/8/20 10:36 PM

import math
import matplotlib.pyplot as plt
import seaborn as sns
import ppretty
from .GeneralInterface import Distribution

class Gaussian(Distribution):

    def __init__(self, mu, sigma):
        """"""
        Distribution.__init__(self, mu, sigma)
