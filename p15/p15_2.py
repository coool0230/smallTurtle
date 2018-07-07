#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p15_2.py
# @Author: huyn
# @Date  : 2018/5/2
# @Desc  :



import tkinter as tk


class App:
    def __init__(self,root):
        frame = tk.Frame(root)
        frame.pack()
        self.hi_there = tk.Button(frame,text="打招呼",fg='blue',command=self.say_hi)
        self.hi_there.pack(side = tk.LEFT)


    def say_hi(self):
        print("good moring Fridends")




root = tk.Tk()
app = App(root)

root.mainloop()