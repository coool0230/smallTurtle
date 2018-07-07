#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_81.py
# @Author: huyn
# @Date  : 2018/5/1
# @Desc  :
import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context

url = "http://baike.baidu.com/view/284853.html"

response = urllib.request.urlopen(url)
html = response.read()

soup = BeautifulSoup(html,"html.parser")

for each in soup.find_all(href = re.compile("view")):
    print(each.text,"-->",''.join(["http://baike.baidu.com",\
                                   each["href"]]))