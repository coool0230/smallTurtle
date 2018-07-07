#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_5.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  :


from tkinter import *
def callback():
    var.set("吹吧你,我才不信呢")



root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()

var.set("属性表示返回的内容数据，从这些数据中可以解析出需要的内容。")
textLabel = Label(frame1,textvariable = var,justify = LEFT)
textLabel.pack(side=LEFT)


photo = PhotoImage(file = '20.gif')
imgLabel = Label(frame1,image = photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2,text="满18岁",command = callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()