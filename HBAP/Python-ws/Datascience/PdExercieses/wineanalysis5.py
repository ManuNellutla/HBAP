import pandas as pd

reviews = pd.read_csv("../datasets/winemag-data-130k-v2.csv", index_col=0)

# understandng multi index

country_reviews = reviews.groupby(['country','province']).description.agg([len])

print(f" \n as compted: \nshape of country reviews is {country_reviews.shape} and index type is {type(country_reviews.index)}")

# reset index to get in single index
country_reviews = country_reviews.reset_index()

print(f" \nafter reset: \nshape of country reviews is {country_reviews.shape} and index type is {type(country_reviews.index)}")

