#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    gaussiance.py
# @Author:      manunellutla
# @Time:        6/1/20 3:21 PM
import math
import matplotlib.pyplot as plt
import seaborn as sns


class Gaussiance():
    """
       Gausiance class - for Gaussian distribution class for calculating and 
    visualizing a Gaussian distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
            
    """

    def __init__(self, mu=0, sigma=1):
        """
        Constructor for gaussiance
        :param mu:
        :param sigma:
        """
        self.stddev = sigma
        self.mu = mu
        self.data = []

    def calculate_mean(self) -> float:
        """
        calculate mean based on the data with the following formula
            mean = sum(data)/len(data)
        :param:
            none
        :return:
            float - mean of the data given
        """
        self.mean = sum(self.data) / len(self.data)
        return self.mean

    def calculate_stddev(self, sample=True) -> float:
        """
        Calculate the standard deviation of the dataset
            i) calculate sigma which is the sum of
                sum(x[i] - mean)**2)
            2) stddev = sqrt(sigma/n) -> where n len(data)  if sample == false  else  len(data)-1
        :param sample:
        :return float: returns a standard deviation of the data.
        """

        # lets check if it is a sample and calculate n
        n = (len(self.data) - 1) if sample else len(self.data)
        print(f"Sample? {sample}, and size is {n}")

        mean = self.mean
        # calculating sigma
        sigma = 0
        for d in self.data:
            sigma += (d - mean) ** 2

        # stddev
        self.stddev = math.sqrt(sigma / n)
        return self.stddev

    def set_data(self, data: []) -> None:
        """
        This method  will set the a single list as data
        :param data: sending  data as a list.
        :return:
        """
        self.data = data

    def plot_hist(self) -> None:
        """

        Args:


        Returns:

        """
        sns.distplot(self.data, bins=30, hist=True, color='green', norm_hist=True)
        #plt.hist(self.data, histtype=u'step')
        plt.xlabel('count')
        plt.ylabel('data')
        plt.title('Histogram  of data')
        plt.show()
