#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : errorHandle.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  : 
from urllib.request import Request,urlopen
from urllib.error import URLError
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


req = Request(url)

try:
    response = urlopen(req)

except URLError as e:
    if hassttr(e,'reason'):
        print("We failed to reach a server")
        print("Reason:",e.reason)
    elif hasattr(e,'code'):
        print('The server could\'t fulffill the request')
        print('Error code',e.code)