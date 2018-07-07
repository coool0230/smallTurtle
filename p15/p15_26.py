#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_26.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :


from tkinter import *


root = Tk()

text = Text(root,width=30,height=10)

text.pack()


text.insert(INSERT,"I Love shishike")
photo = PhotoImage(file="20.gif")

def show():
    text.image_create(END,image=photo)




b1 = Button(text,text="clickmeclickme",command=show)
# b1.pack()

text.window_create(INSERT,window=b1)


mainloop()