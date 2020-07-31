#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    scrape.py.py
# @Author:      manunellutla
# @Time:        6/26/20 4:55 PM

import requests
from bs4 import BeautifulSoup



url = "https://www.walmart.com/browse/electronics/tvs/3944_1060825_447913?page=1"
print("grabbind url...", url)
resp = requests.get(url)

if resp.status_code != 200:
    print("cannot scrape this url: Status: ", resp.status_code)
else:
    # print(resp.text)
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    ps4_items = soup.findAll("li", attrs={"class": "Grid-col"})
    print("Walmart Tv page screenscaping....")
    print("Prouct_Name, Price")
    ps4_price_list={}
    for i in range(len(ps4_items)):
        item_ = ps4_items[i]
        title = item_.find("div", attrs={"class": "search-result-product-title gridview"}).text
        price_tag = item_.find("span", attrs={"class": "price-main-block"})
        price_block = price_tag.find("span", attrs={"class" : "visuallyhidden"})
        #price = 0 if price_block is not None price_block.text

        if price_block != None:
            p = price_block.text
        else:
            p = "$0.00"
        print(title.split("Title")[1],",", p)

    #print(ps4_price_list)
