#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_22.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :


from tkinter import *
root = Tk()


s1 = Scale(root,from_=0,to=42)
s1.pack()


s2 = Scale(root,from_=0,to=200,orient=HORIZONTAL)
s2.pack()


def show():
    print(s1.get(),s2.get())



Button(root,text="获得位置",command=show).pack()

mainloop()