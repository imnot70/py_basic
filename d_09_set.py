#!/usr/bin/env python
# -*- coding: utf-8 -*-
# set是一组key的集合，但是元素不会重复
# 要创建一个 set，需要提供一个 list 作为输入集合
s = set([1, 2, 3])
print(s)
# 重复的元素会被过滤掉
s.add(3)
s.add(4)
print(s)
# 删除元素，元素不存在会报错
s.remove(4)
print(s)
# set的交集和并集运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)