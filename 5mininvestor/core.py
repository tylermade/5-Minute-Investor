#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The Core handles API related functions
'''

import configparser
import requests
import json

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['DEFAULT']['API_KEY']

FUNCTION = "TIME_SERIES_INTRADAY"
SYMBOL = "MSFT"
INTERVAL = "1min"
API_URL = "https://www.alphavantage.co/query?outputsize=compact&function={}&symbol={}&interval={}&apikey={}"
REQUEST = API_URL.format(FUNCTION, SYMBOL, INTERVAL, API_KEY)
response = requests.get(REQUEST)
json_data = json.loads(response.text)
time_series = json_data['Time Series (1min)']
for i in time_series:
    print(i)
    print(time_series[i])
