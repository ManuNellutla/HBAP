import random

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

reviews = pd.read_csv("../datasets/winemag-data-130k-v2.csv", index_col=0)


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
