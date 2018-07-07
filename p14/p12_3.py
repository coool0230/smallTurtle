#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p12_3.py
# @Author: huyn
# @Date  : 2018/4/30
# @Desc  :

import time as t

class MyTimer():
    """
    localtime()返回的是一个时间元祖的结构,只需要前面6个元素,然后将 stop 的元素一次减去 start 对应的元素,将差值存放在一个
    新的列表里"""

    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = '未开始计时'
        self.lasted = []
        self.begin = 0
        self.end = 0
    #开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示:请先调用 stop() 结束计时"
        print("计时开始")

    #停止计时

    def stop(self):
        if not self.begin:
            print("提示:请先调用 start() 开始计时")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束")

    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # return self.prompt
        self.begin = 0
        self.end = 0c.x =



    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])

        return prompt


    def __str__(self):
        return self.prompt
    __repr__ = __str__