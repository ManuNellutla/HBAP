"""
  understanding pyplt
"""

import matplotlib.pyplot as plt
import pandas as pd
import requests
import os

# url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo&datatype=csv"
#
# response = requests.get(url)

# df = pd.read_csv(response.text.splitlines())
#
# print(df.head(5))
#
# df.plot(x='timestamp', y='close', kind='line')
#
# plt.show()

print(os.getenv("AV_API_KEY"))


