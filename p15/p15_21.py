#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_21.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :


from tkinter import *
root = Tk()


Scale(root,from_=0,to =42).pack()
Scale(root,from_=0,to =200,orient=HORIZONTAL).pack()


mainloop()
