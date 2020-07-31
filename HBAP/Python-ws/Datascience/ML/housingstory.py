#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    housingstory.py
# @Author:      manunellutla
# @Time:        6/19/20 10:06 AM

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# Function for comparing different approaches
def score_dataset(X_train, X_valid, y_train, y_valid):
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)
    preds = model.predict(X_valid)
    return mean_absolute_error(y_valid, preds)


def main():
    # import data into dataframe. Let's make 2 copies one for testing
    hdata_full = pd.read_csv("../datasets/melb_data.csv")

    # adding an id column
    hdata_test_full = hdata_full
    hdata_test_full.insert(0,'Id', range(1000, 1000+len(hdata_full)))
    hdata_test_full.reset_index()
    hdata_test_full.index.name = 'Id'
    # lets start with printing observations
    print("\n Data information :")
    hdata_test_full.info()


    # Number of missing values in each column of training data
    missing_val_count_by_column = (hdata_test_full.isnull().sum())
    print(f"\nInspecting missing values :\n{missing_val_count_by_column[missing_val_count_by_column > 0]}")


if __name__ == '__main__':
    main()
