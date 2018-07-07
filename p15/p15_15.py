#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_15.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :

from tkinter import *

root = Tk()

def test1():
    if e1.get() =="小甲鱼":
        print("正确")
        return True

    else:
        print("错误")
        return False

def test2():
    print("我被调用了.....")
    return True




v = StringVar()
e1 = Entry(root,textvariable=v,validate = "focusout",validatecommand=test1,invalidcommand=test2)
e2 = Entry(root)

e1.pack(padx=10,pady=5)
e2.pack(padx=10,pady=5)

mainloop()