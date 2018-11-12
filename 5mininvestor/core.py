#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The Core handles API related functions
'''

import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['DEFAULT']['API_KEY']

FUNCTION = "TIME_SERIES_INTRADAY"
SYMBOL = "MSFT"
INTERVAL = "1min"
API_URL = "https://www.alphavantage.co/query?outputsize=compact&function={}&symbol={}&interval={}&apikey={}"
REQUEST = API_URL.format(FUNCTION, SYMBOL, INTERVAL, API_KEY)
response = requests.get(REQUEST)
print(response.text)
