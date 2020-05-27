import random

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("../datasets/winemag-data-130k-v2.csv", index_col=0)

# is there null values in price

print(f"number of nulls in price column \n{reviews.price.isnull().sum()}")
#print(reviews.price.describe())


# got plenty of null data. lets fill it with following logic
# random numbers of [lower_limit = Mean-std ] and [Upper_limit = mean + std]

def fill_price_nan():
    mean = reviews.price.mean()
    std = reviews.price.std()
    return round(random.uniform(mean - std, mean + std),2)


price_values = reviews['price'].values

for i, j in enumerate(price_values):
    if np.isnan(price_values[i]):
        price_values[i] = fill_price_nan()

reviews['price'] = price_values

print(f"number of nulls in price column after cleanup is  \n{reviews.price.isnull().sum()}")
reviews['price'] = reviews['price'].clip(lower=0)
print(reviews.price.describe())

reviews['stars'] = ''
reviews.loc[(reviews['points'] >= 85), 'stars'] = 2
reviews.loc[(reviews['points'] >= 95), 'stars'] = 3
reviews.loc[(reviews['points'] < 85), 'stars'] = 1
reviews.loc[(reviews.country == 'Canada'), 'stars'] = 3
reviews['stars'] = reviews['stars'].astype(int)

wineplt = reviews[['country', 'points', 'price','stars']]

wineplt2 = wineplt.dropna()
#print(wineplt2.info())

f, (ax1, ax2) = plt.subplots(1,2)
ax1.hist(wineplt2.price, bins='auto')
ax1.set_xlim(-20, 250)
box = wineplt2.boxplot(by='stars', column=['price'])
plt.show()
