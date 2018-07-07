#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_7.py
# @Author: huyn
# @Date  : 2018/5/1
# @Desc  :


import urllib.request

url = 'http://www.whatismyip.com.tw/'

proxy_support = urllib.request.ProxyHandler({"http":"115.218.122.8:9000"})
opener = urllib.request.build_opener(proxy_support)

urllib.request.install_opener(opener)


response = urllib.request.urlopen(url)
html = response.read().decode("utf-8")
print(html)