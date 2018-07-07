#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : train.py
# @Author: huyn
# @Date  : 2018/4/28
# @Desc  :
#
# def fab(n):
#     a1 = 1
#     a2 = 1
#     a3 = 1
#     if n < 1:
#         print("输入错误")
#         return -1
#     while n > 2:
#         a3 = a1 + a2
#         a1 = a2
#         a2 = a3
#         n -= 1
#     return a3
#
# result = fab(35)
# print('{}'.format(result))


# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n -2)
#
# print(fib(35))

# def hanoi(n,x,y,z):
#     if n == 1:
#         print(x+'---->'+z)
#
#     else:
#         hanoi(n-1,x,y,z)
#         print(x+'--->'+y)
#         hanoi(n-1,z,x,y)
#
#
# n = int(input("please input a num:"))
#
# hanoi(n,"x",'y','z')

# try:
#     sum = 1 + '1'
#     f = open("这还一个不存在的文档.txt")
#     print(f.read())
#     f.close()
# # except OSError as reason:
# #     print("文件出错了 T_T\n 错误原因是:" + str(reason))
# # except TypeError as reason:
# #     print("类型出错了 T_T \n错误原因是:" + str(reason))
#
# except (OSError,TypeError) as reason:
#     print('出错了 T_T\n错误原因是:' + str(reason))
# try:
#     int("abc")
#
# except ValueError as reason:
#     print("出错了:" + str(reason))
#
# else:#如果没有问题,就执行这条语句
#     print("there is no error")

# try:
#     with open("record2.txt",'w') as f:
#         f.write("""小客服：小甲鱼，今天有克服问你有没有女朋友？
# 小甲鱼：咦？
# 小客服：我跟她说你有女朋友了！
# 小甲鱼：。。。。。。。
# 小客服：她让你分手后考虑下她！然后我说：“您要买个优盘，我就帮您留意下~”
# 小甲鱼：然后呢？
# 小客服：她买了两个，说发一个货就好~
# 小甲鱼：呃。。。。。。你真牛！
# 小客服：谁让我是鱼C最可爱的小客服嘛~
# 小甲鱼：下次有人想调戏你我不阻止~
# 小客服：滚！！！
# ======================================================================================
# 小客服：小甲鱼，有个好评很好笑哈。
# 小甲鱼：哦？
# 小客服：“有了小甲鱼，以后妈妈再也不用担心我的学习了~”
# 小甲鱼：哈哈哈，我看到丫，我还发微博了呢~
# 小客服：嗯嗯，我看了你的微博丫~
# 小甲鱼：哟西~
# 小客服：那个有条回复“左手拿着小甲鱼，右手拿着打火机，哪里不会点哪里，so easy ^_^”
# 小甲鱼：T_T
# =======================================================================================
# 小客服：小甲鱼，今天一个会员想找你
# 小甲鱼：哦？什么事？
# 小客服：他说你的一个学生月薪已经超过12K了！！
# 小甲鱼：哪里的？
# 小客服：上海的
# 小甲鱼：那正常，哪家公司？
# 小客服：他没说呀。
# 小甲鱼：哦
# 小客服：老大，为什么我工资那么低啊？？是时候涨工资了！！
# 小甲鱼：啊，你说什么？我在外边呢，这里好吵吖。。。。。
# 小客服：滚！！
# """)
#
# except OSError as reason:
#     print('出错了:' + str(reason))


# import urllib.request
# import urllib
# req = urllib.request.Request('http://www.fishc.com/ooxx.html')
# try:
#     urllib.request.urlopen(req)
# except urllib.error.HTTPError as e:
#     print(e)
#     print(e.reason)
#     print(e.code)
#     print(e.read())
#     print(e.geturl())
#     print(e.info())
def delString(string):
    l = list(set(string))
    s =''
    for i in range(len(l)):
        s = s+l[i]
    return s

co_str = 'sdfadsfasdfasfdasfasdfasfasdfasdfasdfasdf'
print(delString(co_str))