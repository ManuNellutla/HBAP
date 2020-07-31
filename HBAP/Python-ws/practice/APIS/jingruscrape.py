#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    jingruscrape.py
# @Author:      manunellutla
# @Time:        6/27/20 4:23 PM

import requests
from bs4 import BeautifulSoup

my_url = "https://www.newegg.com/VR-Games/SubCategory/ID-3722?Tid=245657"
# my_url = input("Enter URL to scrape:")
print("Grabbing...", my_url)

response = requests.get(my_url)
print("Status is", response.status_code)

if (response.status_code != 200):
    print("You can't scrape this", response.status_code)
else:
    print("Scraping...")
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    items_ = soup.find_all("div", attrs={"class": "item-container"})
    print("found items:", len(items_))
    for i in range(len(items_)):
        item = items_[i]
        title = item.find("a", attrs={"class": "item-title"}).text
        price = item.find("li", attrs={"class": "price-current"})
        if price.find("strong") is not None:
            price = float(price.find("strong").text.replace(',', '') + price.find("sup").text)
        else:
            price = "$0.00"
        print("Title:", title, "\nPrice: ", price)
