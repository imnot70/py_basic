#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l=['a','b','c','d','e','f','g']
# 取前三个元素
print(l[0:3])
# 可以省略写作
print(l[:3])
# 取第2，3个元素
print(l[1:3])
# 倒序取值
print(l[-2:])
print(l[-2:-1])

l1=list(range(100))
# 取前10个
print(l1[:10])
# 取后10个
print(l1[-10:])
# 前10个，每2个数取1个
print(l1[:10:2])
# 后10个，第2个数取1个
print(l1[-10::2])
# 所有数
print(l1[:])
# 所有数，每5个取一个
print(l1[::5])

t=(1,2,3,4,5)[:3]
print(t)

str='abcdefg'
print(str[:3])
print(str[::2])