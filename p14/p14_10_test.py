#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_10_test.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  :


# <img class="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=946ee09dd854564ee565e43183df9cde/c116c295d143ad4b0c299a4e87025a


import urllib.request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


response = urllib.request.urlopen("http://tieba.baidu.com/p/3823765471")
html = response.read().decode("utf-8")

# print(html)
p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'

imglist = re.findall(p,html)

for each in imglist:
    print(each)