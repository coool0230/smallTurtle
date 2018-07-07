#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_10.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :

from tkinter import *

root = Tk()
group = LabelFrame(root,text="best is",padx=5,pady=5)
group.pack(padx=10,pady=10)
LANGS = [
    ("python",1),
    ("Perl",2),
    ("RUby",3),
    ("Lua",4)
]

v = IntVar()
v.set(1)

for lang,num in LANGS:
    b = Radiobutton(group,text=lang,variable =v,value = num)
    b.pack(anchor = W)


mainloop()