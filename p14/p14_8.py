#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_8.py
# @Author: huyn
# @Date  : 2018/5/1
# @Desc  :


import urllib.request
import random

url = 'http://www.whatismyip.com.tw/'
print("添加代理 IP 地址,多个 IP 地址间用英文的分号隔开")
iplist = input("请开始输入:").split(sep=';')
while True:
    ip = random.choice(iplist)
    proxy_support = urllib.request.ProxyHandler({'http':ip})
    opner = urllib.request.build_opener(proxy_support)
    opner.addheaders = [('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')]
    urllib.request.install_opener(opner)
    try:
        print("正在使用{}访问...".format(ip))
        response = urllib.request.urlopen(url)

    except urllib.error.URLError:
        print("访问出错")

    else:
        print("访问成功")

    if input("请问是否继续?( Y/N)") == 'N':
        break