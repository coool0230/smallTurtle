#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_6.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  :

from tkinter import *

root = Tk()
v = IntVar()

c = Checkbutton(root,text = "测试一下",variable = v)
c.pack()
l = Label(root,textvariable = v)
l.pack()

mainloop()