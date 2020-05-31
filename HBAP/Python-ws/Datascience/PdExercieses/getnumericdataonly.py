""" how to get only numeric data from a dataframe """

import pandas as pd

mafs_data = pd.read_csv("../Datasets/mafs.csv")

# let's first check what are all the dtypes we have. i will use info instead of dtypes to get a full  picture
print("MAFS Data Info:")
mafs_data.info()

# count numeric vs non numeric

