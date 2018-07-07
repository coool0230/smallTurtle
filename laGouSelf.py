#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : laGouSelf.py
# @Author: huyn
# @Date  : 2018/5/8
# @Desc  :


import urllib.request
import urllib.parse
import json


def open_url(url,page_num,key_word):

    try:
        page_data = urllib.parse.urlencode([
            ('pn',page_num),
            ('kd',key_word)
        ])

        page_headers = {}