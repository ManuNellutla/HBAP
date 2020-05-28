import pandas as pd

reviews = pd.read_csv("../datasets/winemag-data-130k-v2.csv", index_col=0)

# count() returns the number of rows in the column - isnull is kind of ignored.

print(f"\n isnull by count :\n {reviews.price.isnull().count()}")

# sum() basically sums  up trues and  false ( true + true+false+fale = 2) kind of
print(f"\n isnull by sum :\n {reviews.price.isnull().sum()}")