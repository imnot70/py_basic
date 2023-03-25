#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# filter()也接收一个函数和一个序列。filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 定义一个函数，只保留数组中的奇数
def is_odd(n):
    return n % 2 == 1
l=list(filter(is_odd,range(10)))
print(l)

def not_empty(s):
    return s and s.strip()
strs = list(filter(not_empty,['A','B','C','','','D']))
print(strs)