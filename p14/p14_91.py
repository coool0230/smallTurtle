#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_91.py
# @Author: huyn
# @Date  : 2018/5/1
# @Desc  :

import urllib.request
import re,ssl
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context
def main():
    url = "http://baike.baidu.com/view/7833.htm"
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")


    for each in soup.find_all(href= re.compile("view")):
        print(each.text,"-->",''.join(["http://baike.baidu.com",\
                                       each["href"]]))


if __name__ == "__main__":
    main()