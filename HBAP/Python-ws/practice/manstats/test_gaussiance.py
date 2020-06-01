#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    test_gaussiance.py
# @Author:      manunellutla
# @Time:        6/1/20 4:20 PM
from unittest import TestCase
from gaussiance import Gaussiance
import random
import types as ty

class TestGaussiance(TestCase):
    g = Gaussiance(0, 1)

    def setUp(self) -> None:
        data = random.sample(range(10, 200),50) * random.randint(1,10)
        #g = Gaussiance(0, 1)
        self.g.set_data(data)

    def test_calculate_mean(self):
        self.setUp()
        mean = self.g.calculate_mean()
        print(f"Mean  {mean}")
        assert isinstance(mean, (int,float)), "mean is not a float %r" % mean

    def test_calculate_stddev(self):
        self.setUp()
        self.g.mean = self.g.calculate_mean()
        stddev = self.g.calculate_stddev(True)
        print(f"StandardDeviation {stddev}")
        assert isinstance(stddev, (int,float)), "Standard deviation is not a float %r" % stddev
        stddev = self.g.calculate_stddev(False)
        print(f"StandardDeviation {stddev}")
        assert isinstance(stddev, (int, float)), "Standard deviation is not a float %r" % stddev

    def test_plot_hist(self):
        self.setUp()
        self.g.plot_hist()
        assert True
