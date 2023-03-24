#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 上面的第一行注释是为了告诉 Linux/OS X 系统，这是一个 Python 可执行程序，Win会忽略这个注释
# 第二行注释是为了告诉 Python 解释器，按照 UTF-8 编码读取源代码
print("中文")

# this is comments,这是注释
# python中的数据类型：整数，浮点，字符串，布尔(True/False)，空值(None)
# 多行字符串
print('''abc
abc
abc\n''')
print("r123\nr123\n")

# 布尔
print(1>3)

# 变量
a='123'
b=a
a='456'
c=a
# 可以对已经是字符串的c赋值数字
c=456
print(b)
print(c)

# 除法
na=10/3
nb=9/3
# 地板除，结果为整数(取整数位)
nc=10//3
nd=10//6
print(na)
print(nb)
print(nc)
print(nd)

# ord()函数获取字符的整数表示
print(ord('A'))
# chr()函数把编码转换为对应的字符
print(chr(65))

# byte型数据，每个字符都会占用一个字节
x=b'abc'
print(x)
# len()函数计算的是 str 的字符数，如果换成 bytes，len()函数就计算字节数
print(len(b'ABC'))

# 占位符，%s：字符串，%d：整数，%f：浮点数，%x：十六进制数
print('hell %s' %'world')
print('this %s a %s' %('is','test'))
# %d补齐，前面补空格
print("%4d" %3);
# 前面补0
print("%05d" %3);
# %f格式化
print("%.4f" %3.1415926535)

s1=72
s2=85
print('improve: %.1f' % ((s2/s1 - 1) * 100))