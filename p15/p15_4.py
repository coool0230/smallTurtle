#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_4.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  :


from tkinter import *

root = Tk()
photo = PhotoImage(file='bg.gif')
theLabel = Label(root,text="学 python\n 到 FishC",
                 justify = LEFT,
                 image = photo,
                 compound = CENTER,
                 font = ("华康少女字体",20),
                 fg = "white"
                 )
theLabel.pack()
mainloop()