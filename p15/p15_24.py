#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_24.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :


from tkinter import *
root = Tk()

text = Text(root,width=30,height=2)

text.pack()

text.insert(INSERT,"I Love\n")
text.insert(END,"shishike.com")

mainloop()