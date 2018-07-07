#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p11_2.py
# @Author: huyn
# @Date  : 2018/4/29
# @Desc  :

import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def move(self):
        self.x -= 1
        print("my address is :",self.x,self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass



class Shark(Fish):
    def __init__(self):
        self.hungry = True


    def eat(self):
        if self.hungry:
            print('吃货的梦想就是天天有的吃')
            self.hungry = False

        else:
            print("太撑了吃不下了")