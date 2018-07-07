#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_9.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :

from tkinter import *

root = Tk()
LANGS = [
    ("python",1),
    ("perl",2),
    ("Ruby",3),
    ("Lua",4)]

v = IntVar()
v.set(1)

for lang, num in LANGS:
    # b = Radiobutton(root,text=lang,variable=v,value = num)
    b = Radiobutton(root,text=lang, variable=v, value=num,indicatoron = False)
    b.pack(fill = X)
    # b.pack(anchor = W)



mainloop()