#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : trainFile.py
# @Author: huyn
# @Date  : 2018/4/29
# @Desc  :



# count = 1
# boy = []
# girl = []
#
# f = open("record2.txt")
# for eachLine in f:
#     if eachLine[:6] != "======":
#         (role,lineSpoken) = eachLine.split("：",1)
#         if role == "小甲鱼":
#             boy.append(lineSpoken)
#         if role == "小客服":
#             girl.append(lineSpoken)
#
#     else:
#         boy_file_name = "boy_" + str(count) + ".txt"
#         girl_file_name = "girl_" + str(count) + '.txt'
#         boy_file = open(boy_file_name,'w')
#         girl_file = open(girl_file_name,'w')
#         boy_file.writelines(boy)
#         girl_file.writelines(girl)
#         boy = []
#         girl = []
#         count += 1
#
#
#
#
# boy_file.close()
# girl_file.close()
# f.close()

def trainFile(boy,girl,count):
    boyFileName = "boy_" + str(count) + ".txt"
    girlFilename = "girl_" + str(count) + ".txt"
    boyFile = open(boyFileName,"w")
    girlFile = open(girlFilename,"w")
    boyFile.writelines(boy)
    girlFile.writelines(girl)
    boyFile.close()
    girlFile.close()



def fileSplit(filename):
    boy = []
    girl = []
    count = 1
    f = open(filename,'r')
    for eachline in f:
        if eachline[:6] != "======":
            (role,spoken) = eachline.split('：',1)
            if role == "小甲鱼":
                boy.append(spoken)
            if role == "小客服":
                girl.append(spoken)


        else:
            trainFile(boy,girl,count)
            boy = []
            girl = []
            count += 1

    f.close()



fileSplit("record2.txt")
