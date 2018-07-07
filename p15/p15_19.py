#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_19.py
# @Author: huyn
# @Date  : 2018/5/3
# @Desc  :


from tkinter import *

root = Tk()


theLB = Listbox(root,setgrid = True,height =11)
# theLB =Listbox(master,height =11)
theLB.pack()


for item in range(11):
    theLB.insert(END,item)



mainloop()