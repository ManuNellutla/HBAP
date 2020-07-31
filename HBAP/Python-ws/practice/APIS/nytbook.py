#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    nytbook.py
# @Author:      manunellutla
# @Time:        6/26/20 10:34 AM

import json
import pprint
from urllib.request import urlopen
from pandas.io.json import json_normalize
import pandas as pd

if __name__ == '__main__':

        api_key = "YrUCmeLkR8s7Ak0M3Bgsaj5LEgW2XYhR"
        url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=" + api_key

        with urlopen(url) as resp:
            project_info = json.loads(resp.read().decode())
            pprint.pprint(project_info)

        bookd = pd.json_normalize(project_info['results'])
        print(bookd.info())