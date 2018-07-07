#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_18.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :


from tkinter import *

root = Tk()

theLB = Listbox(root,setgrid = True)

theLB.pack()

for item in ["鸡蛋","鸭蛋","鹅蛋","李狗蛋"]:
    theLB.insert(END,item)


theButton = Button(root,text="删除",command=lambda x =theLB:x.delete(ACTIVE))
theButton.pack()


mainloop()
