#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_25.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :

from tkinter import *


root = Tk()

text = Text(root,width=20,height=2)

text.pack()


text.insert(INSERT,"I Love shishike")

def show():
    print("ouy, sfadfafafaf")




b1 = Button(text,text="clickmeclickme",command=show)
b1.pack()

# text.window_create(INSERT,window=b1)


mainloop()