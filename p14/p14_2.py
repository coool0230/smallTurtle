#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p14_2.py
# @Author: huyn
# @Date  : 2018/5/1
# @Desc  :
#User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36

import urllib.request
import urllib.parse
import json



content = input("please input your want fanyi:")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http//www.youdao.com/"
data = {}


# data['req'] = 'check'
# data['fanyi_src'] = 'I Love you'
# data['direction'] = 'en2zh'
# data['_'] = '1525152997809'
# data['to'] = "AUTO"
# data['from'] = "AUTO"
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
data = urllib.parse.urlencode(data).encode("utf-8")
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(html)
target = json.loads(html)
print(target)
print("翻译结果:{}".format(target['translateResult'][0][0]['tgt']))
# print(data)?
