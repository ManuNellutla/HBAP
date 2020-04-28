import requests
import csv
from prettytable import PrettyTable
import numpy as np

url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo&datatype=csv"

response = requests.get(url)

t = PrettyTable()
reader = csv.DictReader(response.text.splitlines())
row = next(reader)
t.field_names=row

for row in reader:
    t.add_row([row['close'],row['open'], row['high'], row['low'], row['close'], row['volume']])


print(t)
#avgVol = (np.mean(list(row['volume'])))
print(f"average volume : {avgVol}")
