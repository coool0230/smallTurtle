#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_3.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  :


from tkinter import *

root = Tk()

textLabel = Label(root,\
                  text = "属性表示返回的内容数据，从这些数据中可以解析出需要的内容。",justify=LEFT,padx=10)
textLabel.pack(side = LEFT)
photo = PhotoImage(file='20.gif')
imgLabel = Label(root,image = photo)
imgLabel.pack(side=RIGHT)


mainloop()