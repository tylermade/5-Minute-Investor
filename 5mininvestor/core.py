#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
The Core handles API related functions
'''

import configparser

config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['DEFAULT']['API_KEY']

print(API_KEY)
