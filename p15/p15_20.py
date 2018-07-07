#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_20.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :

from tkinter import *

root = Tk()

sb = Scrollbar(root)
sb.pack(side=RIGHT,fill = Y)
lb = Listbox(root,yscrollcommand=sb.set)

for i in range(1000):
    lb.insert(END,str(i))



lb.pack(side=LEFT,fill=BOTH)
sb.config(command=lb.yview)

mainloop()