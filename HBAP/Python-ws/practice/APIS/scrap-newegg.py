#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    scrap-newegg.py.py
# @Author:      manunellutla
# @Time:        6/27/20 4:12 PM


import requests
from bs4 import BeautifulSoup



url = "https://www.newegg.com/VR-Games/SubCategory/ID-3722?Tid=245657"
print("grabbind url...", url)
resp = requests.get(url)

if resp.status_code != 200:
    print("cannot scrape this url: Status: ", resp.status_code)
else:
    # print(resp.text)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    ps4_items = soup.find_all("div", attrs={"class": "item-container"})
    print("Newegg VR page screenscaping....")
    print("Prouct_Name, Price")
    ps4_price_list={}
    for i in range(len(ps4_items)):
        item = ps4_items[i]
        title = item.find("a", attrs={"class": "item-title"}).text

        if "Out Of Stock" in item.text:  # skipping an item out of stock
            continue

        price = item.find("li", attrs={"class": "price-current"})

        if price.find("strong") is not None:
            price = float(price.find("strong").text.replace(',', '') + price.find("sup").text)
        else:
            price = None

        print(title, ",", price)
