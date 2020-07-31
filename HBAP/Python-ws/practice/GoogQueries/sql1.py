#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    sql1.py
# @Author:      manunellutla
# @Time:        6/14/20 9:59 AM

from google.cloud import bigquery

client = bigquery.Client()

dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

# List all the tables in the "hacker_news" dataset
tables = list(client.list_tables(dataset))

# Print names of all tables in the dataset (there are four!)
for table in tables:
    print(table.table_id)
