import pandas as pd
from datetime import datetime

filename = "../datasets/melb_data.csv"

home_data = pd.read_csv(filename)
print(home_data.columns)
avg_lot_size = round(home_data['Landsize'].mean())

newest_home = int(home_data['YearBuilt'].max())
current_year  = datetime.now().year

newest_home_age = current_year - newest_home

print(f"Average lot size is {avg_lot_size} and newest home was built in {newest_home} and its age is {newest_home_age}")

