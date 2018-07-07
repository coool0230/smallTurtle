#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p9_8.py
# @Author: huyn
# @Date  : 2018/4/29
# @Desc  :

def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("{}的最大公约数是{}".format(num,count))
            break
        count -=1

    else:
        print("{}是素数".format(num))


num = int(input("please input a num:"))
showMaxFactor(num)