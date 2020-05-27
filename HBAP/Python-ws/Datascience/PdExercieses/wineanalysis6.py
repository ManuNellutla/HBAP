import pandas as pd

reviews = pd.read_csv("../datasets/winemag-data-130k-v2.csv", index_col=0)

#this is right also
country_variety_counts = reviews.groupby(['country', 'variety']).apply(lambda df: df.variety.count().max())

# lambda trying

##rint(country_variety_counts2)

reviews.country = reviews.country.replace('US', 'United States')

print(reviews.country.unique())