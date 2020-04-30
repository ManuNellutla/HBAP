"""
get stock price based on the input from Alpha vantage api
"""

# for api requests
import requests
import csv
from prettytable import PrettyTable


# ask user for a valid ticker symbol

stkSymbol = input(" Please Enter a valid Stock ticker symbol : ")

# url pieces
avUrl = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY"
urlSymbol = "&symbol="+stkSymbol
avApiKey = "&apikey=3PCZEURZNO81FFXS"
avformat = "&datatype=csv"
url = avUrl + urlSymbol + avApiKey + avformat

print(f"Close price by date for  :{stkSymbol}")

# call the api and store output in the response
response = requests.get(url)

data = {}
# setup a CVS dict reader so we call call by header names
reader = csv.DictReader(response.text.splitlines())
# this is the header row
#row = next(reader)
t = PrettyTable(["Date", "Close Price"])
for row in reader:
    date = row["timestamp"].split(" ")[0]
    t.add_row([date, row["close"]])

# print the output in table format
print(t)
