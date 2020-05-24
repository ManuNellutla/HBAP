import pandas  as pd

mafs = pd.read_csv("mafs.csv")

print(f" \nColumn names of the Data set \n {mafs.columns}")

print(f"\nNull Data summary  \n {mafs.isnull().sum()}")

print(f"\n rows and columns :  {mafs.shape}")

print(f"\n summary of the mafs  data  is  \n {mafs.describe().transpose()}")

print(f"\ntop few rows of dataframe \n {mafs.head()}")