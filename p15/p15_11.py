#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_11.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :


from tkinter import *

root = Tk()
e = Entry(root)
e.pack(padx=20,pady=20)
e.delete(0,END)
e.insert(0,"默认文本...")

mainloop()