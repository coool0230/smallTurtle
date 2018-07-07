#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p12_1.py
# @Author: huyn
# @Date  : 2018/4/30
# @Desc  :


class Rectangle():
    """
    定义一个矩形类
    需要长和宽两个参数
    拥有计算周长和面积的两个方法
    需要对象在初始化的时候拥有长和宽两个参数
    因此需要重写__ init__()方法,因为我们说过
    __init__() 方法是类在实例化成对象的时候首先会调用的一个方法
    understand?
    """
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getPerl(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y