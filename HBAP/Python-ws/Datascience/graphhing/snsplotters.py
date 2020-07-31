#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    snsplotters.py
# @Author:      manunellutla
# @Time:        6/12/20 6:46 PM

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
if __name__ == '__main__':
    insdata = pd.read_csv("../datasets/insurance.csv")
    print(insdata.head())
    print(insdata.info())

    # understanding correlation between BMI and charges
    fig, axs = plt.subplots(2,2)
    sns.scatterplot(x=insdata.bmi, y= insdata.charges,hue=insdata.age, ax=axs[0][0])
    sns.regplot(x=insdata.age, y= insdata.charges, ax=axs[0][1])
    sns.scatterplot(x=insdata.bmi, y=insdata.charges, hue=insdata.smoker, ax=axs[1][0])
    sns.swarmplot(x='smoker', y='charges', hue='smoker', data=insdata)
    sns.lmplot('bmi', 'charges', hue='smoker', data=insdata)
    plt.show()

    st.button("Re-run")