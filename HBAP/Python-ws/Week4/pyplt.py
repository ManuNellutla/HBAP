"""
  understanding pyplt
"""

import matplotlib.pyplot as plt
import pandas as pd
import requests
import os

url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&interval=5min&apikey=3PCZEURZNO81FFXS&datatype=csv"

df = pd.read_csv(url)

print(df.head(5))


df.plot(x='timestamp', y='close', kind='line', style='.-', xticks=d['timestamp'])
plt.xticks(rotation=45)
#df.plot(style='.-')
plt.show()




