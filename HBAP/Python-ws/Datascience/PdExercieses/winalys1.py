import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# print(f"\nmean price of the wine bottles {reviews.price.mean()}")
#
# print(f"\nlist of unique countries \n {reviews.country.unique()}")
#
# print(f"\nnumber of reviews by country \n {reviews.country.value_counts()}")

# review_price_mean = reviews.price.mean()
# centered_price = reviews.price.map(lambda p: p - review_price_mean)
#
# print(f"\ncentered_pricing \n {centered_price.describe()}")

# wineplt = reviews[['country', 'points', 'price']]
# print(wineplt.shape)
# print(wineplt.isnull().sum())
# print(wineplt.head())
# wineplt2 = wineplt.dropna()
# print(wineplt2.shape)
# plt.xlim(0,200)
# wineplt2.hist()
# plt.show()

# n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
# n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
# descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
# print(descriptor_counts)

# A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1
# star. Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should
# automatically get 3 stars, regardless of points. Create a series star_ratings with the number of stars
# corresponding to each review in the dataset.

reviews['stars'] = ''
reviews.loc[(reviews['points'] >= 85), 'stars'] = 2
reviews.loc[(reviews['points'] >= 95), 'stars'] = 3
reviews.loc[(reviews['points'] < 85), 'stars'] = 1
reviews.loc[(reviews.country == 'Canada'), 'stars'] = 3
reviews['stars'] = reviews['stars'].astype(int)
print(reviews.stars.describe())


def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1


star_ratings = reviews.apply(stars, axis='columns')
print(star_ratings.describe())
# html= reviews.to_html()
#
# text_file = open("test.html", "w")
# text_file.write(html)
# text_file.close()
