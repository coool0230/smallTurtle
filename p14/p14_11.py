#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_11.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  : 

import urllib.request
import re
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")
    return html


def get_ip(html):
    p = r'(?:(?:[01]{0,1}\d{0,1}\d|d[0-4]\d|25[0-5])\.){3}(?:[01]{0,1}\d{0,1}\d|d[0-4]\d|25[0-5])'
    img_ip = re.findall(p,html)
    for each in img_ip:
        print(each)



if __name__ == "__main__":
    url = "https://www.kuaidaili.com/free/"
    get_ip(open_url(url))


