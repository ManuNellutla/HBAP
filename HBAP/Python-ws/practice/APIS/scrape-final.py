#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    scrape-final.py
# @Author:      manunellutla
# @Time:        6/27/20 11:23 AM

import requests
from bs4 import BeautifulSoup
import csv

# Part 1: initialization

# base url
my_url = "https://www.newegg.com/PS4-Systems/SubCategory/ID-3102/Page-"
# my_url = input("Enter URL to scrape: ")

# page number to attach to the base url
page = 1
# create a csv file
csvfile = open('egg2.csv', 'w', newline='')
# create a writer to convert data into delimited strings
eggwriter = csv.writer(csvfile)
# header
eggwriter.writerow(["Title", "Price", "Rating", "RatingNum"])

no_error = True

# loop over html pages
while no_error:
    url = my_url + str(page)
    page = page + 1
    print("Grabbing...", url)
    response = requests.get(url, allow_redirects=False)  # go to the URL and get it
    print(response.url)
    print("Status is", response.status_code)  # 200, 403, 404, 500, 503
    for resp in response.history:
        print(resp.status_code, resp.url)
    # https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

    # Part 2
    if (response.status_code != 200):
        print("You can't scrape this", response.status_code)
        no_error = False
        continue
    else:
        print("Scraping...")
    # print(response.text)

    # Part 3
    # Add from bs4 import BeautifulSoup
    html = response.text
    # print (html)
    soup = BeautifulSoup(html, "html.parser")  # convert raw html to something I can use with BeautifulSoup

    # Part 4
    # Grab specific div on the web page
    # items = soup.find_all("a", attrs={"class":"item-title"})
    items = soup.find_all("div", attrs={"class": "item-container"})

    for i in range(len(items)):
        item = items[i]

        title = item.find("a", attrs={"class": "item-title"}).text

        if "Out Of Stock" in item.text:  # skipping an item out of stock
            continue

        price = item.find("li", attrs={"class": "price-current"})

        if price.find("strong") is not None:
            price = float(price.find("strong").text.replace(',', '') + price.find("sup").text)
        else:
            price = None

        # rating = item.find('i', attrs={"class": "rating"})
        # if rating is not None:
        #     rating = rating['class'][1].split('-    ')[1]
        #
        # ratingNum = item.find('span', attrs={"class": "item-rating-num"})
        # if ratingNum is not None:
        #     ratingNum = ratingNum.text.lstrip('(').rstrip(')')

        # write to csv
        eggwriter.writerow([title, price])

    if page > 10:
        break

