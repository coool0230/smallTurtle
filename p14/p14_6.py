#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_6.py
# @Author: huyn
# @Date  : 2018/5/1
# @Desc  :

import urllib.request
import urllib.parse
import json
import time




url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http//www.youdao.com/"

# head = {}
# head['Referer'] = "http://www.youdao.com"
# head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
while True:
    content = input("please input your want fanyi:")
    if content == 'q!':
        break
    data = {}
    data[type] = 'AUTO'
    data["i"] = content
    data['doctype'] = 'json'
    data['version'] = '2.0'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = "UTF-8"
    # data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'true'
    # data['smartresult'] = 'dict'
    # data['client'] = 'fanyideskweb'
    # data['salt'] = '1525150848449'
    # data['sign'] = '6af7be05099dca14985d8bc54716dc34'
    data = urllib.parse.urlencode(data).encode("utf-8")#利用 parse.urlencode(data)将字符串转换格式 encode 将数据编码设置为" utf-8"
    req = urllib.request.Request(url,data)          #初始化成 Request 对象
    req.add_header('Referer',"http://www.youdao.com")
    req.add_header('User-Agent','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')
    # head['Referer'] = "http://www.youdao.com"
    # head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    response = urllib.request.urlopen(req)#urlopen 如果直接传入一个字符串,则会自动将字符串 处理为为一个 Request 对象 也可以直接传入一个 Request 对象
    html = response.read().decode('utf-8')
    print(html)
    target = json.loads(html)
    print(target)
    print("翻译结果:{}".format(target['translateResult'][0][0]['tgt']))
    # print(data)?
    print(req.headers)
    time.sleep(5)