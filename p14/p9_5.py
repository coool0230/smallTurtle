#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p9_5.py
# @Author: huyn
# @Date  : 2018/4/26
# @Desc  :


t = set()
w = []
s = 'wewfwefadqwdqdwqdiousdafnpauwiehfwufensjahfejakslhfewnaghuegaegr'
for i in s:
    t.add(i)
    w.append(i)


for x in t:
    print("{}出现的次数是:{}".format(x,s.count(x)))


# print(t)
# print(w)