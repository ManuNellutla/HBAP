#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    test_gaussiance.py
# @Author:      manunellutla
# @Time:        6/1/20 4:20 PM
from unittest import TestCase
from gaussiance import Gaussiance
import random
import matplotlib.pyplot as plt

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
        print(self.g)

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

    def test_add(self):
        self.setUp()
        self.g.calculate_mean()
        self.g.calculate_stddev(True)
        data2 = random.sample(range(50, 100),30) * random.randint(1,5)
        g2 = Gaussiance(3,2)
        g2.set_data(data2)
        g2.calculate_mean()
        g2.calculate_stddev(False)
        print(self.g)
        print(g2)
        gsum = self.g + g2
        print(gsum)
        self.g.plot_hist()
        g2.plot_hist()
        gsum.plot_hist()
        plt.show()
        assert True