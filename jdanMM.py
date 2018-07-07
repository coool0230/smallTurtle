#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : jdanMM.py
# @Author: huyn
# @Date  : 2018/5/5
# @Desc  :


import urllib.request
import re
import ssl
import os
from analysisPicUrl import get_urls


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode("utf-8")
    return html
    # print(html)

def get_img(html):
    # p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'
    # p = r'</span><p><a href="(.+?)" target="_blank" class="view_img_link"'
    # # imglist = re.findall(p,html)
    # print(imglist)
    imglist = get
    try:
        os.mkdir("JdanMPics")

    except FileExistsError:
        #如果该文件已保存则覆盖该文件
        pass

    os.chdir("JdanMPics")
    for each in imglist:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename,None)



# def createUrl(n):
#     url = []
#     for i in range(int(n)):
#         url.append("http://jandan.net/ooxx/page-{}#comments".format(i))
#
#     for eachurl in url:
#         return eachurl

url = []
for i in range(60):
    url.append("http://jandan.net/ooxx/page-{}#comments".format(i))


if __name__ == "__main__":
    url = "http://jandan.net/ooxx/page-1#comments"
    get_img(open_url(url))
