#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : p10_1.py
# @Author: huyn
# @Date  : 2018/4/29
# @Desc  :

import easygui as eg
import sys
eg.msgbox("hi,welcome the first game")
msg = "what want you to learn"
title = "small game"
choices = ["谈恋爱","编程","OOXX","琴棋书画"]
choice = eg.choicebox(msg,title,choices)
eg.msgbox("your choice is :"+ str(choice),"reason")
msg = "do you want again small game"
title = "please choice"
if eg.ccbox(msg,title):
    pass
else:
    sys.exit(0)