#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 常规排序
l = sorted([36, 5, -12, 9, -21])
print(l)
# 使用元素的绝对值排序
l1 = sorted([36, 5, -12, 9, -21], key=abs)
print(l1)


def pow(n):
    return n * n


l2 = sorted([-6, 1, 2, 4, -5, 7], key=pow)
print(l2)

# 忽略大小写
l3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(l3)
# 忽略大小写，反向
l4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(l4)
