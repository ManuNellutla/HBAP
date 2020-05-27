import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("../datasets/winemag-data-130k-v2.csv", index_col=0)

print(f"\nmean price of the wine bottles {reviews.price.mean()}")

print(f"\nlist of unique countries \n {reviews.country.unique()}")

print(f"\nnumber of reviews by country \n {reviews.country.value_counts()}")

review_price_mean = reviews.price.mean()
centered_price = reviews.price.map(lambda p: p - review_price_mean)

print(f"\ncentered_pricing \n {centered_price.describe()}")


n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
print(descriptor_counts)




